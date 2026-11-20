# Curadoria diária IA e Direito

Acervo e definição versionada da curadoria anti-hype diária sobre IA aplicada ao Direito.

`curadorias/` guarda um arquivo por dia. `prompt/` guarda os prompts das tarefas agendadas. `tarefa.json` guarda a configuração delas. Para restaurar qualquer parte, ver [RECUPERACAO.md](RECUPERACAO.md).

`instagram/` guarda o post diário derivado da curadoria: `render.py` e o template fixo (fontes e foto em `fonts/` e `assets/`), `reel.py`, que transforma os mesmos slides num reel vertical narrado por voz sintética, e uma pasta por dia em `posts/` com o texto (`post.json`, que inclui a narração), os slides, o `reel.mp4` e as legendas. A tarefa `Post Instagram curadoria` prepara carrossel e reel às 06h07 e só publica depois de um "publicar" na sessão da execução.

O reel usa a voz Piper `pt_BR-cadu-medium` (dataset CC0), baixada do Hugging Face numa revisão fixa e conferida por sha256, e sai marcado com o rótulo de IA do Instagram (`is_ai_generated`). Cada reel ocupa cerca de 4 MB; no ritmo diário, o repositório cresce perto de 1,5 GB por ano só com vídeo, e passado 1 GB convém mover os vídeos para anexos de release.
