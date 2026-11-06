CURADORIA DIARIA IA E DIREITO, 2026-11-06

CABECALHO
Data de coleta: 2026-11-06 (inicio 05:50 America/Sao_Paulo)
Janela aplicada: 72h (escalonada a partir de 36h)
Buscas WebSearch executadas: 13
Feeds RSS consumidos com sucesso: 10 de 13 (mais consulta complementar a API do arXiv e a base de Damien Charlotin)
Candidatos coletados: 82 (66 itens unicos de feeds na janela de 72h, 10 preprints da API arXiv na janela, 6 resultados de busca checados individualmente; base Charlotin sem caso novo na janela)
Candidatos apos filtro deterministico: 9 (apos descarte de itens fora do tema, entrevistas de fornecedor, anuncios de investimento, agregadores sem fonte primaria e itens fora da janela)
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 1 / (d) 2
Origem das fontes: midia tradicional 0% / Substack-RSS 33% / social 0% (os 67% restantes sao fontes primarias: preprints academicos)


1. Clio Wants To Bring AI to the Judiciary, But 50-State Survey Reveals Policies Differ in Whether They Allow It

Fonte: LawNext (Bob Ambrogi) | URL primaria: https://www.lawnext.com/2026/11/clio-wants-to-bring-ai-to-the-judiciary-but-50-state-survey-reveals-policies-differ-in-whether-they-allow-it.html

Data de publicacao: 2026-11-05

Categoria: (c) risco novo importante

Sintese: Ambrogi publica levantamento das politicas de IA generativa dirigidas a juizes e servidores dos tribunais estaduais dos EUA, com corte em 30/10/2026, motivado pela entrada da Clio no mercado judiciario (contratacao de Pablo Arredondo e Bridget McCormack, aquisicao da Learned Hand). O levantamento foi feito com ChatGPT, conferido com Claude e complementado por pesquisa propria do autor, que pede correcoes publicamente. Na tabela, 12 estados aparecem como "Not identified" (sem instrumento estadual localizado) e os demais se espalham entre politica vinculante, guia etico, principios e propostas em desenvolvimento. Massachusetts e o caso mais restritivo: as Interim Guidelines de novembro de 2025 vedam IA generativa para pesquisa, redacao e outro trabalho juridico por juizes, assessores e contratados, permitindo apenas uso administrativo. Nova York fica no polo oposto, com ferramentas aprovadas e opiniao etica de setembro de 2026 admitindo IA privada para resumir transcricoes de audiencias. Arizona, Nova York, Pensilvania, Carolina do Sul, Utah e Virginia controlam quais ferramentas podem ser usadas. O ponto comum e a proibicao de delegar o julgamento a IA e o dever de verificar citacoes.

Por que entrou: Mapeia, com fontes oficiais linkadas por estado, a fragmentacao regulatoria que condiciona a entrada de fornecedores de IA no Judiciario, e separa explicitamente IA que assiste o trabalho judicial de IA que exerce juizo. Util como contraponto comparado a Resolucao CNJ 615/2025.


2. Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs

Fonte: arXiv (Md. Rafiul Biswas e George Mikros, Hamad Bin Khalifa University; Wajdi Zaghouani, Northwestern University in Qatar) | URL primaria: https://arxiv.org/abs/2611.07988

Data de publicacao: 2026-11-05

Categoria: (d) solucao para gargalo em pipelines juridicos

Sintese: O trabalho mede o efeito de adaptacao de dominio, quantizacao e destilacao em LLMs juridicos arabes usando o ArabLegalEval (benchmark de direito saudita), em dois protocolos: com contexto (passagens legais fornecidas, analogo a RAG) e sem contexto (conhecimento parametrico). Modelos avaliados: FANAR-9B, JAIS-8B e Qwen2.5-7B. Remover o contexto abre lacunas de acuracia de ate 27 pontos percentuais no modelo base. A quantizacao em 4 bits (bitsandbytes, NF4 e FP4, alem de INT8 via LLM.int8()) reduz a memoria em 64% a 71%, com variacao de -3,2 a +1,6 pontos na acuracia de multipla escolha sem contexto. A destilacao tem resultados mais instaveis e piora conforme o aluno encolhe; um aluno Qwen2.5-7B destilado do FANAR chega a 76,6% sem contexto contra 77,2% do professor. Os autores defendem a avaliacao sem contexto como complemento obrigatorio ao teste com contexto.

Por que entrou: Ataca um gargalo pratico de quem roda modelos juridicos em infraestrutura restrita (on-premise, dados sigilosos): quanto se perde ao comprimir, e como o protocolo de avaliacao com contexto pode mascarar a degradacao parametrica. O desenho com/sem contexto e diretamente replicavel em eval sets de portugues juridico.


3. KDASO: Knowledge-Data Dual-Driven Automated Skill Optimization for Liability Adjudication Tasks

Fonte: arXiv (Zi-Jian Cheng, Weiming Wu, Jie Meng, Zhen Peng, Shan Huang, Qun Li, Guobing Wu, Lan-Zhe Guo) | URL primaria: https://arxiv.org/abs/2611.06972

Data de publicacao: 2026-11-04

Categoria: (d) solucao para gargalo em pipelines juridicos

Sintese: O artigo trata de tarefas de atribuicao de responsabilidade (por exemplo, determinacao de tipo penal) em que o LLM aplica "skills" executaveis, descricoes de regras de especialista, a narrativas de fatos. Identifica tres falhas: bibliotecas de skills ficam desatualizadas, o modelo diverge da logica pretendida na execucao (semantic execution gap) e o acervo de skills excede o orcamento de contexto, causando omissao de skill relevante. O KDASO responde com inducao de skills condicionada a vizinhanca de casos recentes, refinamento alinhado a execucao a partir da analise de trajetorias do LLM, descarte de skills alucinadas por validacao empirica de acuracia, e roteamento com orcamento de contexto. A avaliacao cobre adjudicacao de disputas de transporte por aplicativo (metricas no padrao DiDi), determinacao de responsabilidade juridica (LawBench, incluindo amostra de 500 instancias do CAIL2018, e LegalBench) e raciocinio logico (ReClor, AR-LSAT). Os autores relatam superioridade sobre baselines gerais e de dominio, inclusive NodeRAG, e ganho de 8,96% ao transferir skills para cenarios conceitualmente proximos.

Por que entrou: Enfrenta dois gargalos recorrentes de pipelines juridicos com regras explicitas: a obsolescencia de playbooks e o estouro de contexto quando o acervo de regras cresce. O mecanismo de roteamento com orcamento e a validacao de skills alucinadas sao transponiveis para sistemas de triagem e enquadramento de pecas.


REVISAO ADVERSARIAL

Item 1 (LawNext). Fonte primaria do levantamento e o proprio artigo, de autor identificado (Bob Ambrogi, jornalista de legal tech com historico longo). URL resolve via curl (HTTP 200), dominio oficial lawnext.com. A tabela linka instrumentos oficiais por estado; duas fontes oficiais testadas (mass.gov e nycourts.gov) responderam 403 ao curl do ambiente de nuvem, entao o teor das Interim Guidelines de Massachusetts e da opiniao etica 26-133 de Nova York ficou [nao verificado em segunda fonte] nesta execucao. A contagem de 12 estados "Not identified" foi feita por esta curadoria a partir da tabela do artigo e o proprio autor ressalva que "not identified" nao significa inexistencia de politica. O levantamento foi produzido com auxilio de ChatGPT e Claude, o que o autor declara; erros pontuais sao possiveis e ele solicita correcoes. Linguagem promocional: a frase "judiciary-grade AI" e marca registrada da Clio citada pelo autor, nao endosso. Categoria (c) resiste: o objeto e o risco regulatorio e de conformidade de IA no Judiciario, nao o produto da Clio.

Item 2 (arXiv 2611.07988). Preprint sem revisao por pares, autores e afiliacoes identificados no proprio PDF/HTML. URL resolve (HTTP 200). Numeros extraidos do resumo e conferidos na versao HTML (27 pp, 64% a 71%, -3,2 a +1,6 pp, 76,6% vs 77,2%); nao ha segunda fonte independente, entao todos ficam [nao verificado em segunda fonte]. Escopo limitado: benchmark de multipla escolha em direito saudita, tres modelos de 7B a 9B; transferencia para portugues juridico e inferencia, nao resultado. Sem linguagem promocional. Categoria (d) resiste.

Item 3 (arXiv 2611.06972). Preprint sem revisao por pares; autores identificados, afiliacoes nao confirmadas nesta execucao [nao verificado]. URL resolve (HTTP 200). O resumo usa "significantly outperforms" sem numero agregado; a unica cifra do resumo e o ganho de 8,96% na transferencia, [nao verificado em segunda fonte]. Os dados de adjudicacao de transporte por aplicativo seguem padrao DiDi, o que sugere dataset proprietario de dificil reproducao [nao verificado]. Categoria (d) resiste com ressalva: o dominio principal e adjudicacao de plataforma, com o componente juridico concentrado em LawBench/LegalBench. Item entrou apenas no nivel de 72h (publicado em 04/11 13:05 UTC, fora da janela de 36h).

Nenhum item tem origem social. Nenhum descarte ou substituicao na fase adversarial.


AUDITORIA

Nivel de janela: 36h produziu apenas 2 itens qualificados (LawNext de 05/11 e arXiv 2611.07988 de 05/11). A janela foi escalonada para 72h, onde o KDASO (04/11) completou 3 itens. Nao houve escalonamento para 7 dias.

Deduplicacao: comparado com curadorias de 2026-11-03, 2026-11-04 e 2026-11-05. Excluidos por duplicidade: Vokshi v. Canada (unico caso novo da base Charlotin, ja entregue em 05/11), LegalEvolver (arXiv 2611.06381, ja entregue em 05/11), PROSE (arXiv 2611.04921, ja entregue em 04/11).

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, mas devolveu pagina HTML em vez de feed, zero entradas parseaveis). ConJur respondeu 200 nesta execucao, sem itens de IA relevantes na janela; busca complementar site:conjur.com.br nao trouxe item datado na janela. Volokh, JOTA, ConJur, LawSites, LawNext, Artificial Lawyer e Charlotin consumidos; Unikowsky, 3 Geeks e Harvard Law Review Blog consumidos, sem entradas na janela.

Base Charlotin: "Last updated: 5 November 2026"; caso mais recente datado de 03/11/2026 (Vokshi), ja deduplicado.

Descartes com motivo:
Withers v. City of Aberdeen (Bloomberg Law): publicado em 09/06/2026, fora da janela.
California Supreme Court e brief de promotoria com IA (Daily Journal): publicado em 16/01/2026, fora da janela e paywall.
STJ multa por julgado inventado por IA (O Cafezinho, 03/11): veiculo secundario sem autoria (Redacao), decisao de junho de 2026 (AgInt no AREsp 3.010.133/MG) [nao verificado na fonte primaria].
"Lawyer Penalized for Using AI" (go.kompas.com, 05/11): URL retornou pagina de outra materia, conteudo nao verificavel.
Legal exploits may emerge at scale (Felix Ringe e Linus Folkerts, felixringe.com): publicado em 28/10/2026, fora da janela de 72h; candidato forte de (c) caso a janela tivesse ido a 7 dias.
How AI agents shape experts' judgment calls (Anthropic Research): publicado em 27/10/2026, fora da janela e fora do dominio juridico.
AI & Law Stuff #31 (Damien Charlotin, 06/11): newsletter de comentario; seus itens primarios (Ringe, Anthropic) estao fora da janela.
STJ vai monitorar aplicacao da relevancia e de precedentes obrigatorios (JOTA, 05/11): conteudo integral sob paywall, sem dado verificavel sobre uso de IA.
Domain-specific information retrieval (arXiv 2611.08228, 05/11): monografia de revisao (Foundations and Trends in IR), sem resultado novo.
Artificial Lawyer, 03/11 a 04/11 (Litera/Hg/Anthropic, Ex-Legorans, Copilot for Legal, Brief History): anuncio de investimento, entrevista de fornecedor ou retrospectiva sem dado.
NetDocuments CPO (LawNext, 03/11): entrevista de fornecedor sem auditoria independente.
Demais itens de Volokh, JOTA e ConJur na janela: fora do tema IA e Direito.

Substituicoes: nenhuma.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
