#!/usr/bin/env python3
"""Gera o reel narrado do dia a partir de posts/AAAA-MM-DD/post.json.

Uso (na raiz do repositorio, depois do render.py):
    python3 instagram/reel.py instagram/posts/AAAA-MM-DD [--conferir]

Decisao de arquitetura: o mesmo principio do render.py. O agente escreve so o
texto da narracao (campo "narracao" do post.json, um trecho por slide); voz,
ritmo, quadros e codificacao moram aqui, fixos. Os quadros sao os mesmos
slides do template v3, renderizados em 1080x1920 com margens livres da
interface do Reels; cada slide fica na tela pelo tempo exato do seu trecho.

Voz: Piper (offline, sem chave de API), modelo pt_BR-cadu-medium, dataset CC0,
baixado do Hugging Face numa revisao fixa e conferido por sha256. A narracao e
sintetica: a legenda do reel recebe o aviso e a publicacao marca is_ai_generated.

--conferir transcreve o audio gerado com Whisper e mede a distancia entre o que
foi escrito e o que se ouve, trecho a trecho. O agente nao escuta o audio; esta
e a forma de ele saber que uma sigla ou um nome virou ruido.

Saida na pasta do post: reel.mp4 (H.264/AAC conforme a especificacao de Reels
da API), legenda-reel.txt e reel.json (voz, tempos por slide, sha256).
Codigo de saida 2 = narracao fora dos limites ou slide estourado no formato
vertical: o agente corrige o texto e roda de novo. Codigo 3 = falha de ambiente
(voz, ffmpeg, navegador): o carrossel segue sem reel.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import LIMITE_LEGENDA, TEMPLATE, montar_html  # noqa: E402

LARGURA, ALTURA = 1080, 1920
FPS = 30
# cadencia apertada em 2026-11-21, a pedido: menos ar entre slides e frases
TRANSICAO = 0.15        # fusao curta entre slides
ENTRADA_PRIMEIRO = 0.05  # o gancho comeca de imediato
ENTRADA = 0.18          # maior que TRANSICAO: a fala so comeca com o slide novo inteiro na tela
SAIDA = 0.15
SAIDA_ULTIMO = 1.0      # o CTA fica na tela depois da ultima palavra
PAUSA_FRASE = 0.06
DURACAO_MIN, DURACAO_MAX = 15.0, 90.0
PALAVRAS_TRECHO_MAX = 45
PALAVRAS_TOTAL = (70, 145)  # ~170 palavras/min: 145 palavras dao cerca de 53 s
LIMIAR_CONFERENCIA = 0.30  # distancia por trecho acima da qual o agente reescreve

VOZ = {
    "nome": "pt_BR-cadu-medium",
    "repositorio": "rhasspy/piper-voices",
    "revisao": "e929968c3761f1c281875787685a745863db838d",
    "caminho": "pt/pt_BR/cadu/medium",
    "sha256": {
        ".onnx": "d5a662e3f606d5a49dd29ba9ce90c304ae45dd9543f8b0c773bcb0de282499de",
        ".onnx.json": "28c27ae86debf5e304176c5be533bbb3a483e456f42272eeb7dbfede48dae741",
    },
    # escolhida entre as tres vozes medium pt_BR por menor erro de transcricao
    # (Whisper) no mesmo texto juridico, em 2026-11-20. Velocidade medida em
    # 2026-11-21 sobre a narracao daquele dia: 0.95 = 144 palavras/min,
    # 0.80 = 163, 0.75 = 170, todas com a mesma inteligibilidade no Whisper
    "length_scale": 0.75,
}
AVISO_VOZ = "Narração em voz sintética."

# siglas que se dizem como palavra; as demais sao soletradas
SIGLAS_PALAVRA = {"ONU", "OTAN", "SUS", "CADE", "PROCON", "ANATEL", "ANVISA", "ANEEL", "UNESCO",
                  "FIFA", "NASA", "RAG", "OIT", "INMETRO", "DETRAN", "FUNAI", "IBAMA", "PIX"}
LETRAS = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  "á bê cê dê é éfe gê agá i jota cá éle ême ene ó pê quê érre ésse tê u vê dáblio xis ípsilon zê".split()))
# trocas fixas antes da sintese; testadas com a voz acima (a sigla IA, por
# exemplo, sai como interjeicao se nao for expandida)
TROCAS = [
    (r"\bIAs\b", "inteligências artificiais"),
    (r"\bI\.?A\.?(?=[\s,.;:!?)]|$)", "inteligência artificial"),
    (r"\bEUA\b", "Estados Unidos"),
    (r"\bUE\b", "União Europeia"),
    (r"\bChatGPT\b", "Chat gê pê tê"),
    (r"\bOpenAI\b", "Open ei ai"),
    (r"\barXiv\b", "arcaive"),
    (r"(?i)\banti-?hype\b", "antirraipe"),
    (r"(?i)\bhype\b", "raipe"),
    (r"(?i)\bpremium\b", "prêmium"),
]
# o que a voz le mal e o agente deve reescrever (nao ha conversao automatica segura)
PROIBIDO_NA_FALA = [
    (r"\d\s*/\s*\d", "data ou numero com barra: escreva por extenso (\"17 de novembro\")"),
    (r"\d{5,}", "numero longo (processo, protocolo): omita na fala"),
    (r"https?://|www\.", "endereco web"),
    (r"[@#]", "arroba ou hashtag"),
    (r"(R|US)\$|€", "simbolo de moeda: escreva \"cinco mil reais\""),
    (r"\bn[º°o]\.?\s*\d", "abreviatura de numero: escreva \"numero\" ou omita"),
    (r"[—–]", "travessao"),
]


def falhar(msg: str, codigo: int) -> int:
    print(f"ERRO: {msg}")
    return codigo


def soletrar(m: re.Match) -> str:
    sigla = m.group(0)
    if sigla in SIGLAS_PALAVRA or re.fullmatch(r"[IVXLC]+", sigla):
        return sigla
    return " ".join(LETRAS[c] for c in sigla)


def preparar_fala(texto: str) -> str:
    """Texto do post.json -> texto que a voz le bem. Nao altera o post.json."""
    t = texto.replace("*", "")
    for padrao, troca in TROCAS:
        t = re.sub(padrao, troca, t)
    t = re.sub(r"\b[A-Z]{2,6}\b", soletrar, t)
    return re.sub(r"\s+", " ", t).strip()


def validar_narracao(post: dict) -> list[str]:
    erros = []
    narr = post.get("narracao")
    if not isinstance(narr, list) or len(narr) != len(post["slides"]):
        return [f"\"narracao\" precisa ser uma lista com {len(post['slides'])} trechos, um por slide"]
    total = 0
    for i, trecho in enumerate(narr, 1):
        if not isinstance(trecho, str) or not trecho.strip():
            erros.append(f"trecho {i} vazio")
            continue
        n = len(trecho.split())
        total += n
        if n > PALAVRAS_TRECHO_MAX:
            erros.append(f"trecho {i} com {n} palavras (maximo {PALAVRAS_TRECHO_MAX})")
        for padrao, motivo in PROIBIDO_NA_FALA:
            if re.search(padrao, trecho):
                erros.append(f"trecho {i}: {motivo}")
    if not PALAVRAS_TOTAL[0] <= total <= PALAVRAS_TOTAL[1]:
        erros.append(f"narracao com {total} palavras (faixa {PALAVRAS_TOTAL[0]} a {PALAVRAS_TOTAL[1]})")
    return erros


def legenda_reel(legenda: str) -> str:
    """Legenda do carrossel com o aviso de voz sintetica antes das hashtags."""
    linhas = legenda.rstrip().split("\n")
    if linhas and linhas[-1].lstrip().startswith("#"):
        return "\n".join(linhas[:-1]).rstrip() + f"\n\n{AVISO_VOZ}\n\n" + linhas[-1]
    return legenda.rstrip() + f"\n\n{AVISO_VOZ}"


def sha256(arq: Path) -> str:
    h = hashlib.sha256()
    with open(arq, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def obter_voz() -> Path:
    """Baixa (uma vez por ambiente) o modelo de voz na revisao fixa e confere o sha256.

    Revisao fixa + hash: o modelo e codigo executado no ambiente; um arquivo
    trocado na origem nao entra sem que o hash denuncie.
    """
    cache = Path.home() / ".cache" / "curadoria-voz"
    cache.mkdir(parents=True, exist_ok=True)
    base = (f"https://huggingface.co/{VOZ['repositorio']}/resolve/{VOZ['revisao']}/"
            f"{VOZ['caminho']}/{VOZ['nome']}")
    for ext, esperado in VOZ["sha256"].items():
        destino = cache / f"{VOZ['nome']}{ext}"
        if not destino.exists() or sha256(destino) != esperado:
            tmp = destino.with_suffix(destino.suffix + ".part")
            subprocess.run(["curl", "-sSfL", "--retry", "2", "--max-time", "300", "-o", str(tmp), base + ext],
                           check=True)
            if sha256(tmp) != esperado:
                tmp.unlink(missing_ok=True)
                raise RuntimeError(f"sha256 divergente em {VOZ['nome']}{ext}")
            tmp.replace(destino)
    return cache / f"{VOZ['nome']}.onnx"


def ffmpeg_bin() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    import imageio_ffmpeg  # binario estatico via pip, se o ambiente nao tiver ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def sintetizar(trechos: list[str]) -> tuple[list[np.ndarray], int]:
    from piper import PiperVoice, SynthesisConfig
    voz = PiperVoice.load(str(obter_voz()))
    cfg = SynthesisConfig(length_scale=VOZ["length_scale"])
    audios, taxa = [], None
    for trecho in trechos:
        partes = []
        for bloco in voz.synthesize(preparar_fala(trecho), syn_config=cfg):  # um bloco por frase
            taxa = bloco.sample_rate
            if partes:
                partes.append(np.zeros(int(PAUSA_FRASE * taxa), np.float32))
            partes.append(bloco.audio_float_array.astype(np.float32).reshape(-1))
        audios.append(np.concatenate(partes))
    return audios, taxa


def renderizar_quadros(post: dict, pasta_tmp: Path) -> list[int]:
    from playwright.sync_api import sync_playwright
    arq_html = pasta_tmp / "reel.html"
    arq_html.write_text(montar_html(post, reel=True), encoding="utf-8")
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    estouros = []
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        pag = nav.new_page(viewport={"width": LARGURA, "height": ALTURA}, device_scale_factor=1)
        pag.goto(arq_html.as_uri())
        pag.evaluate("document.fonts.ready")
        for i in range(1, len(post["slides"]) + 1):
            sobra = pag.evaluate(
                "(id)=>{const c=document.querySelector('#'+id+' .corpo');return c.scrollHeight-c.clientHeight}", f"s{i}")
            if sobra > 0:
                estouros.append(i)
            # PNG, nao JPEG: o quadro vai ser comprimido uma vez so, pelo H.264
            pag.locator(f"#s{i}").screenshot(path=str(pasta_tmp / f"q{i:02d}.png"), type="png")
        nav.close()
    return estouros


def conferir_mp4(arq: Path, duracao: float) -> list[str]:
    """Confere o arquivo contra a especificacao de Reels da API do Instagram."""
    problemas = []
    sonda = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(arq)],
        capture_output=True, text=True, check=True).stdout) if shutil.which("ffprobe") else None
    if sonda:
        v = next(s for s in sonda["streams"] if s["codec_type"] == "video")
        a = next((s for s in sonda["streams"] if s["codec_type"] == "audio"), None)
        if (v["codec_name"], v["width"], v["height"], v["pix_fmt"]) != ("h264", LARGURA, ALTURA, "yuv420p"):
            problemas.append(f"video fora do padrao: {v['codec_name']} {v['width']}x{v['height']} {v['pix_fmt']}")
        if not a or a["codec_name"] != "aac" or int(a["sample_rate"]) > 48000 or int(a["channels"]) > 2:
            problemas.append("audio fora do padrao (AAC, ate 48 kHz, ate 2 canais)")
        if abs(float(sonda["format"]["duration"]) - duracao) > 0.5:
            problemas.append(f"duracao {sonda['format']['duration']}s diverge da prevista {duracao:.2f}s")
    # caixas de topo: moov antes de mdat (faststart) e nenhuma lista de edicao
    dados = arq.read_bytes()
    ordem, pos = [], 0
    while pos + 8 <= len(dados):
        tam = int.from_bytes(dados[pos:pos + 4], "big")
        tipo = dados[pos + 4:pos + 8].decode("latin-1")
        if tam == 1:
            tam = int.from_bytes(dados[pos + 8:pos + 16], "big")
        ordem.append((tipo, pos, tam))
        if tam < 8:
            break
        pos += tam
    tipos = [t for t, _, _ in ordem]
    if "moov" not in tipos or "mdat" not in tipos or tipos.index("moov") > tipos.index("mdat"):
        problemas.append("moov nao esta antes de mdat")
    else:
        _, ini, tam = ordem[tipos.index("moov")]
        if b"elst" in dados[ini:ini + tam]:
            problemas.append("arquivo tem lista de edicao (elst)")
    if len(dados) > 300 * 1024 * 1024:
        problemas.append("arquivo acima de 300 MB")
    return problemas


def montar_video(pasta_tmp: Path, blocos: list[float], audio_wav: Path, saida: Path) -> None:
    n = len(blocos)
    cmd = [ffmpeg_bin(), "-y", "-v", "error"]
    for i, b in enumerate(blocos, 1):
        # cada slide dura o seu bloco; os que nao sao o ultimo ganham a fusao,
        # que se sobrepoe ao inicio do bloco seguinte
        dur = b + (TRANSICAO if i < n else 0)
        cmd += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.3f}", "-i", str(pasta_tmp / f"q{i:02d}.png")]
    cmd += ["-i", str(audio_wav)]
    filtros = [f"[{i}:v]fps={FPS},format=yuv420p,setsar=1[v{i}]" for i in range(n)]
    atual, deslocamento = "v0", 0.0
    for i in range(1, n):
        deslocamento += blocos[i - 1]
        filtros.append(f"[{atual}][v{i}]xfade=transition=fade:duration={TRANSICAO}:offset={deslocamento:.3f}[x{i}]")
        atual = f"x{i}"
    # -14 LUFS integrado, teto de -1,5 dBTP: o nivel usual das plataformas sociais
    filtros.append(f"[{n}:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,aformat=channel_layouts=stereo[a]")
    total = sum(blocos)
    cmd += ["-filter_complex", ";".join(filtros), "-map", f"[{atual}]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-tune", "stillimage",
            "-profile:v", "high", "-level", "4.1", "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-g", str(2 * FPS), "-maxrate", "8M", "-bufsize", "16M",
            "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2",
            "-t", f"{total:.3f}", "-movflags", "+faststart", "-use_editlist", "0", str(saida)]
    subprocess.run(cmd, check=True)


def conferir_fala(trechos: list[str], audios: list[np.ndarray], taxa: int) -> list[dict]:
    """Transcreve cada trecho e mede a distancia de palavras contra o texto escrito."""
    from faster_whisper import WhisperModel
    try:
        from num2words import num2words
    except ImportError:
        num2words = None

    def normalizar(s: str) -> list[str]:
        # compara texto com texto, sem soletrar siglas: o Whisper escreve "STF"
        s = s.replace("*", "")
        for padrao, troca in TROCAS:
            s = re.sub(padrao, troca, s)
        s = s.lower()
        if num2words:
            s = re.sub(r"\d+", lambda m: num2words(int(m.group(0)), lang="pt_BR"), s)
        return re.sub(r"[^\w\s]", " ", s).split()

    def distancia(ref: list[str], hip: list[str]) -> float:
        d = list(range(len(hip) + 1))
        for i, r in enumerate(ref, 1):
            ant, d[0] = d[0], i
            for j, h in enumerate(hip, 1):
                ant, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, ant + (r != h))
        return d[len(hip)] / max(len(ref), 1)

    modelo = WhisperModel("small", device="cpu", compute_type="int8")
    resultado = []
    for i, (trecho, audio) in enumerate(zip(trechos, audios), 1):
        # reamostragem linear para 16 kHz: suficiente para reconhecimento de fala
        x = np.interp(np.arange(0, len(audio), taxa / 16000), np.arange(len(audio)), audio).astype(np.float32)
        segs, _ = modelo.transcribe(x, language="pt", beam_size=5)
        ouvido = " ".join(s.text for s in segs).strip()
        resultado.append({"slide": i, "ouvido": ouvido,
                          "distancia": round(distancia(normalizar(trecho), normalizar(ouvido)), 3)})
    return resultado


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--conferir", action="store_true", help="transcreve o audio e mede a inteligibilidade")
    args = ap.parse_args()
    pasta = Path(args.pasta).resolve()
    post = json.loads((pasta / "post.json").read_text(encoding="utf-8"))

    erros = validar_narracao(post)
    legenda = legenda_reel(post["legenda"])
    if len(legenda) > LIMITE_LEGENDA:
        erros.append(f"legenda do reel com {len(legenda)} caracteres, limite {LIMITE_LEGENDA}")
    if erros:
        for e in erros:
            print(f"ERRO: {e}")
        return 2

    trechos = post["narracao"]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        try:
            estouros = renderizar_quadros(post, tmp)
            audios, taxa = sintetizar(trechos)
        except Exception as e:  # ambiente: navegador, rede, modelo de voz
            return falhar(f"ambiente: {type(e).__name__}: {e}", 3)
        if estouros:
            for i in estouros:
                print(f"ERRO: slide {i} estourou a area util no formato vertical; encurte o texto")
            return 2

        # linha do tempo: cada bloco = entrada + fala + saida; o slide i ocupa o bloco i
        blocos, pedacos, tempos, t = [], [], [], 0.0
        for i, audio in enumerate(audios):
            entrada = ENTRADA_PRIMEIRO if i == 0 else ENTRADA
            saida = SAIDA_ULTIMO if i == len(audios) - 1 else SAIDA
            fala = len(audio) / taxa
            pedacos += [np.zeros(int(round(entrada * taxa)), np.float32), audio,
                        np.zeros(int(round(saida * taxa)), np.float32)]
            bloco = (int(round(entrada * taxa)) + len(audio) + int(round(saida * taxa))) / taxa
            blocos.append(bloco)
            tempos.append({"slide": i + 1, "inicio": round(t, 2), "fala_inicio": round(t + entrada, 2),
                           "fala_fim": round(t + entrada + fala, 2), "fim": round(t + bloco, 2),
                           "palavras": len(trechos[i].split())})
            t += bloco
        total = sum(blocos)
        if not DURACAO_MIN <= total <= DURACAO_MAX:
            return falhar(f"reel com {total:.1f}s (faixa {DURACAO_MIN:.0f} a {DURACAO_MAX:.0f}s); ajuste a narracao", 2)

        wav = tmp / "narracao.wav"
        pcm = np.clip(np.concatenate(pedacos) * 32767, -32768, 32767).astype(np.int16)
        with wave.open(str(wav), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(taxa)
            w.writeframes(pcm.tobytes())

        saida = pasta / "reel.mp4"
        try:
            montar_video(tmp, blocos, wav, saida)
        except Exception as e:
            return falhar(f"ambiente: ffmpeg: {e}", 3)
        problemas = conferir_mp4(saida, total)
        if problemas:
            for p in problemas:
                print(f"ERRO: {p}")
            return 3

        # folha de quadros fora do repositorio, para o agente conferir o layout
        # com uma unica leitura de imagem
        folha = Path(tempfile.gettempdir()) / f"reel-quadros-{pasta.name}.jpg"
        n = len(blocos)
        entradas = sum((["-i", str(tmp / f"q{i:02d}.png")] for i in range(1, n + 1)), [])
        escala = ";".join(f"[{i}:v]scale=300:-1[e{i}]" for i in range(n))
        subprocess.run([ffmpeg_bin(), "-y", "-v", "error", *entradas, "-filter_complex",
                        escala + ";" + "".join(f"[e{i}]" for i in range(n)) + f"hstack=inputs={n}",
                        "-frames:v", "1", "-q:v", "3", str(folha)], check=False)

        conferencia = None
        if args.conferir:
            try:
                conferencia = conferir_fala(trechos, audios, taxa)
            except Exception as e:  # a conferencia ajuda, mas nao bloqueia o reel
                conferencia = {"erro": f"{type(e).__name__}: {e}"}

    (pasta / "legenda-reel.txt").write_text(legenda, encoding="utf-8")
    (pasta / "reel.json").write_text(json.dumps({
        "template": TEMPLATE, "formato": f"reel {LARGURA}x{ALTURA} {FPS}fps",
        "voz": f"{VOZ['nome']}@{VOZ['revisao'][:12]}", "length_scale": VOZ["length_scale"],
        "duracao_s": round(total, 2), "slides": tempos, "bytes": saida.stat().st_size,
        "sha256": sha256(saida), "conferencia_fala": conferencia,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: reel de {total:.1f}s ({saida.stat().st_size / 1e6:.1f} MB) em {saida}")
    if folha.exists():
        print(f"quadros: {folha}")
    if isinstance(conferencia, list):
        for c in conferencia:
            marca = "  << reescreva este trecho" if c["distancia"] > LIMIAR_CONFERENCIA else ""
            print(f"conferencia slide {c['slide']}: distancia {c['distancia']:.2f}{marca} | ouvido: {c['ouvido']}")
    elif conferencia:
        print(f"AVISO: conferencia da fala nao rodou: {conferencia['erro']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
