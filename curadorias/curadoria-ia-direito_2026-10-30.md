CURADORIA DIARIA IA E DIREITO, 2026-10-30

CABECALHO
Data de coleta: 2026-10-30 (execucao iniciada por volta de 05h50 America/Sao_Paulo, 08h50 UTC)
Janela aplicada: 36h (nivel base, sem escalonamento; 3 itens qualificados na janela)
Buscas WebSearch executadas: 16
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 61 (54 entradas RSS unicas publicadas nas ultimas 36h; 7 artigos da API do arXiv submetidos em 2026-10-29; 0 decisoes no AI Hallucination Cases Database datadas na janela; resultados do WebSearch examinados, nenhum com fato novo datado na janela)
Candidatos apos filtro deterministico: 6
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 0 / (d) 3
Origem das fontes: midia tradicional 0% / Substack-RSS 0% / social 0% (os tres itens, 100%, vem de repositorio academico, arXiv, fora das tres classes; nenhum candidato (b) ou (c) com data na janela de 36h passou na triagem)


1. Homebrewed SLMs: Autoregressive and Masked Diffusion Language Models Built at Home for Portuguese
Fonte: arXiv (2610.40533), Pedro Carvalho Brom, Departamento de Matematica, Instituto Federal de Brasilia | URL primaria: https://arxiv.org/abs/2610.40533
Data de publicacao: 2026-10-29
Categoria: (d) solucao para gargalo em pipelines juridicos (eval datasets e modelos para portugues juridico)
Sintese: Tutorial reprodutivel que treina do zero, numa unica GPU domestica (RTX 5090 limitada a 500 W, tambem executavel em T4 do Colab), um modelo de 11 a 12M parametros com tokenizer proprio e dois modos de geracao na mesma rede Transformer: autoregressivo e difusao mascarada. Corpus: prosa brasileira e leis federais. O ponto juridico e o kit de quatro tarefas geradas por script, sem rotulagem humana, a partir de 1.094 atos federais de 2025 e 2026: T1 preencher lacuna (numero ou remissao a outro dispositivo), T2 texto inserido ou proprio, T3 texto adulterado (troca de termo juridico, permutacao de numeros, remissao trocada, fusao de dispositivos) e T4 continuacao. Comparacao com piso Kneser-Ney 6-gram e modelos publicos de 160M e 630M, com protocolo pre-registrado. Resultados: o modo autoregressivo memoriza apos 64 epocas, a difusao melhora ate 256; empata com o piso em verossimilhanca em leis nao vistas, supera o piso em deteccao de adulteracao e preenche remissoes melhor que piso e modelos publicos apenas em decretos; em leis, os modelos publicos lideram. Codigo, notebooks em portugues e DOI Zenodo publicados.
Por que entrou: entrega um conjunto de tarefas automaticas sobre legislacao brasileira, incluindo deteccao de dispositivo adulterado e de remissao trocada, que pode ser reaproveitado como eval de integridade textual em pipelines RAG juridicos em portugues. O catalogo de defeitos revelados so pela medicao serve de checklist metodologico.


2. XLaw-JP-27B: A Lightweight Open Model Specialized for Japanese Law
Fonte: arXiv (2610.39227), Andrew Shin, Keio University e X-Law, Inc. | URL primaria: https://arxiv.org/abs/2610.39227
Data de publicacao: 2026-10-29
Categoria: (d) solucao para gargalo em pipelines juridicos (modelo on-premises com retrieval e ablacao por componente)
Sintese: Modelo de pesos abertos (Apache 2.0) derivado do Qwen3.8-27B que roda numa GPU de 48 GB em FP8. Componentes: retrieval hibrido sobre o texto vigente de todas as leis japonesas e 31 mil sumarios de decisoes, QLoRA leve sobre 150 respostas proprias verificadas a questoes do exame da Ordem de 2019 a 2023 mais 91 revisoes contratuais (self-distillation), adaptador LoRA especifico para contratos e votacao por maioria sobre quatro amostras. Em oito tarefas, contra Gemma 4 12B, LLM-jp-4.1 33B e Qwen3-Swallow 32B com prompts e retrieval identicos, fica em primeiro em seis (rank medio 1,3 contra 2,8 a 3,1) e e o unico aprovado na parte objetiva do exame em 2024, 2025 e 2026 (129, 120 e 130 de 175). A ablacao indica que retrieval, votacao e self-distillation ajudam, e que thinking mode, tuning sintetico ancorado em retrieval, autoverificacao e decomposicao por assercao nao ajudam. Maior distancia para modelos de fronteira em revisao contratual (0,24 contra 0,475) e direito de patentes. Pesos no Hugging Face e demo gratuita em x-law.jp.
Por que entrou: e um caso documentado de modelo juridico local, viavel para quem nao pode enviar documentos de cliente a API externa, com ablacao que separa o que funciona do que nao funciona. O resultado negativo de autoverificacao e thinking mode e informacao util para quem desenha pipeline de pecas.


3. IndicIPR-QA: A Benchmark for Extractive Question Answering on Indian IPR Laws
Fonte: arXiv (2610.40518), M. Mohaiminul Islam e Muhammad Abulaish, South Asian University, Nova Delhi | URL primaria: https://arxiv.org/abs/2610.40518
Data de publicacao: 2026-10-29
Categoria: (d) solucao para gargalo em pipelines juridicos (eval dataset com span exato em texto legal)
Sintese: Benchmark de QA extrativo com 4.462 pares pergunta e resposta extraidos de 1.116 contextos legais das sete leis indianas de propriedade intelectual (Patents Act 1970, Trade Marks Act 1999, Copyright Act 1957, Designs Act 2000, Geographical Indications Act 1999, Semiconductor Integrated Circuits Layout-Design Act 2000, Protection of Plant Varieties and Farmers' Rights Act 2001), a partir dos PDFs oficiais do governo. Perguntas e respostas geradas por GPT-4o, filtradas por nove verificacoes automaticas e avaliacoes por LLM, com auditoria humana de 200 pares por dois bachareis em direito. Particao por secao evita sobreposicao de contexto entre treino, validacao e teste. BM25 atinge F1 de 20,21; InLegalBERT ajustado chega a 85,02 com janela deslizante; modelos de 7B a 12B em zero e few-shot tambem foram avaliados. Desempenho varia entre as sete leis. Dataset e codigo publicados no Hugging Face e no GitHub.
Por que entrou: exige resposta como span exato do dispositivo, o que corresponde ao requisito de citacao verificavel em RAG juridico, e a distancia entre BM25 e modelo ajustado quantifica o limite do casamento lexical. A receita (geracao por LLM com particao por secao e auditoria humana amostral) e replicavel para legislacao brasileira.


REVISAO ADVERSARIAL

Item 1. Fonte primaria: sim, preprint no arXiv; pagina de resumo e PDF baixados via curl (HTTP 200, application/pdf) e lidos nos trechos de contribuicoes (C3 a C5), hardware e tarefas T1 a T4. Autor unico identificado com afiliacao e e-mail institucional (ifb.edu.br). Repositorio confirmado via raw.githubusercontent.com (HTTP 200; a pagina github.com respondeu 403 a partir deste ambiente) e DOI Zenodo 10.5281/zenodo.23774590 (HTTP 200). Sem revisao por pares; o proprio texto diz que a leitura humana cega pre-registrada nao faz parte desta versao e que a reproducao no Colab nao foi feita. Numeros nao verificados em segunda fonte: 1.094 atos, 64 e 256 epocas, ganho de 0,06 bit por byte. Escala minima (11 a 12M parametros) limita a transferencia direta dos resultados para modelos de producao; o valor esta no kit de tarefas, nao no modelo. Sem linguagem promocional. Categoria (d) resiste.

Item 2. Fonte primaria: sim, preprint no arXiv; PDF baixado via curl (HTTP 200) e lido nas tabelas de resultados e ablacao. Conflito de interesse: o autor e vinculado a X-Law, Inc., que opera o servico x-law.jp, e todas as baselines foram rodadas uma unica vez pelo proprio autor. Numeros do exame (129, 120, 130 de 175) e rank medio conferidos em segunda fonte, o model card do Hugging Face (README em HTTP 200), que e do mesmo autor e portanto nao independente. Nao replicado por terceiros. O PDF lista Claude Opus 5.5 com 173 e 171 pontos como referencia de fronteira, o que confirma o limite declarado. Dominios x-law.jp e huggingface.co/X-LawJapan resolvem (HTTP 200). A ressalva de demo de fornecedor sem auditoria independente se aplica em parte; mantido por haver pesos abertos e receita reprodutivel. Categoria (d) resiste com ressalva.

Item 3. Fonte primaria: sim, preprint no arXiv; PDF baixado via curl (HTTP 200) e lido na construcao do dataset, auditoria humana e tabela de resultados. Autores identificados com afiliacao. Dataset no Hugging Face resolve (HTTP 200). Respostas geradas por GPT-4o: o gold e sintetico e a auditoria humana cobre 200 de 4.462 pares (cerca de 4,5%), o que limita a confianca na qualidade do conjunto inteiro. F1 de 20,21 (BM25) e 85,02 (InLegalBERT) nao verificados em segunda fonte. Contextos curtos, de ordem de grandeza de 100 a 200 palavras pela tabela comparativa do artigo [nao verificado: atribuicao exata da coluna]: o benchmark mede extracao dentro de um trecho ja recuperado, nao recuperacao. Sem linguagem promocional. Categoria (d) resiste, sendo o mais fraco dos tres.

Descartes e substituicoes no adversarial: nenhum item descartado; nenhuma URL deixou de resolver.


AUDITORIA

Nivel de janela: 36h (corte em 2026-10-28 20h54 UTC). Tres itens qualificados (d) na janela base, sem necessidade de escalonar. Nenhum candidato (b) ou (c) com data dentro das 36h; os casos de sancao e risco localizados estavam fora da janela ou ja tinham sido entregues. Deduplicacao feita contra curadorias de 2026-10-23 a 2026-10-29 por URL e titulo; nenhum dos tres itens aparece nelas.

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, 0 entradas parseaveis). Feeds com HTTP 200 mas sem entrada na janela, contados como consumidos: Adam Unikowsky, Damien Charlotin Substack, Harvard Law Review Blog, 3 Geeks. ConJur respondeu HTTP 200 com 10 entradas; busca complementar site:conjur.com.br nao trouxe resultado do dominio.

Descartes:
"Statutory Article Retrieval from Arabic Judicial Narratives" (arXiv 2610.38336, submetido em 2026-10-28 06h36 UTC): fora da janela de 36h por cerca de 14h; seria o candidato mais forte de (d) (pipeline Decompose-and-Refine elevando MRR@10 em Direito Probatorio de 0,087 para 0,696).
"Harvey Buys Aida, 5th Purchase in 2026" (Artificial Lawyer, 2026-10-29): aquisicao corporativa, sem caso de uso mensuravel.
"What Real AI Adoption Looks Like" e "The 4 Es Inhouse AI Framework" (Artificial Lawyer, 2026-10-29 e 30): divulgacao de palestrantes de evento, sem dado verificavel.
"AI Governance Must Keep Pace with Legal Practice" (Artificial Lawyer, 2026-10-29): artigo de executiva de fornecedor (LexisNexis), opiniao sem dado.
"AI Didn't Cause the Weil Crisis" e "As Weil Faces the End, A New Mod Is Born" (Artificial Lawyer, 2026-10-29): opiniao sobre mercado e lancamento de startup sem auditoria.
"At ClioCon, Legal's AI Future Is Already Here" (LawNext, 2026-10-29): filtro deterministico (enquadramento de futuro da advocacia; relato de evento de fornecedor).
"Engenharia reversa de IA: propriedade intelectual e responsabilidade civil" (ConJur, 2026-10-29): artigo doutrinario sem caso ou dado concreto.
"Plaintiff Appears to Be a Well-Educated Individual with Time on His Hands" (Volokh, 2026-10-29): mencao a IA apenas em comentario do blogueiro.
Demais 4 artigos do arXiv de 2026-10-29 (MAServeBench, AI Cosmos, LAMP, RetroChessBench): sem tema juridico.
AI Hallucination Cases Database (atualizada em 2026-10-29): decisao mais recente datada de 2026-10-23, fora da janela; SA Post Office v Fakude ja entregue em 2026-10-29.
STJ, AREsp 3.095.458 (multa de R$ 20 mil por comandos ocultos para IA, noticiado em 2026-10-20 e 21): fora da janela e ja coberto em curadorias anteriores.
California Supreme Court e brief de promotoria com alucinacoes (Daily Journal, abril de 2026): fora da janela.
Prompt injection em peticao (404 Media via Modelwire, agosto de 2026): fora da janela.
Atty With False AI Citation Filings Ordered To Pay $39K (Law360 e USA Herald): fora da janela; USA Herald nao resolveu via fetch.
Buscas X/Twitter, Reddit e Hacker News: nenhum post dos handles ancora nem discussao com fonte primaria nova na janela.

Substituicoes: nenhuma.

Observacao de processo: foram executadas 16 buscas WebSearch, acima da faixa de 8 a 10 prevista, para tentar localizar candidato (b) ou (c) na janela base.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
