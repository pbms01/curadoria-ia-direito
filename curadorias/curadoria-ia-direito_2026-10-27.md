CURADORIA DIARIA IA E DIREITO, 2026-10-27

CABECALHO
Data de coleta: 2026-10-27 (execucao iniciada por volta de 05h55 America/Sao_Paulo, 08h55 UTC)
Janela aplicada: 7 dias (escalonamento de nivel 2; em 36h so 1 item qualificado, em 72h 2 itens)
Buscas WebSearch executadas: 19 (acima das 8 a 10 previstas, para compensar coleta fraca na semana do segundo turno eleitoral no Brasil)
Feeds RSS consumidos com sucesso: 9 de 13
Candidatos coletados: 59 (37 entradas RSS unicas na janela de 72h; 11 decisoes datadas entre 2026-10-20 e 2026-10-23 no AI Hallucination Cases Database; 7 preprints do arXiv com tema juridico via API; 4 materias datadas na janela vindas do WebSearch)
Candidatos apos filtro deterministico: 17 (dos 59: 36 fora do escopo IA e Direito, 1 cobertura de anuncios de fornecedor, 5 duplicatas de dias anteriores)
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional 0% / Substack-RSS 33% (decisao localizada pela base de Damien Charlotin, coletada via RSS e curl da base) / social 0% (os outros dois itens, 67%, vem de repositorio academico, arXiv, fora das tres classes)


1. Chilingarian v. Blanche, Nos. 25-9591, 25-9592 e 25-9593 (Order and Judgment)
Fonte: United States Court of Appeals for the Tenth Circuit; copia do documento hospedada pelo AI Hallucination Cases Database (Damien Charlotin) | URL primaria: https://www.damiencharlotin.com/documents/3312/Chilingarian_v._Blanch_USA_20-10-2026.pdf
Data de publicacao: 2026-10-20
Categoria: (b) erro ou fracasso documentado
Sintese: Peticao de revisao contra decisao do BIA em pedido de protecao pela Convencao contra a Tortura (CAT), apresentada por tres membros da familia Chilingarian, representados por advogado. O painel (voto do Circuit Judge Scott M. Matheson, Jr.) negou as peticoes. No argumento de devido processo, o tribunal considerou o brief inadequado sob a Rule 28(a) e deixou de examinar o merito por waiver; somou a deficiencia uma citacao atribuida a Goldberg v. Kelly que nao consta do acordao e dois precedentes inexistentes, "Sameeh v. Gonzales, 453 F.3d 1150 (10th Cir. 2006)" e "Naranjo Garcia v. Garland, 990 F.3d 1177 (9th Cir. 2021)". Em nota de rodape, a corte diz que os erros "appear to be the product of generative artificial intelligence", registra que o governo ja havia apontado um deles no brief de resposta, que o reply brief nao corrigiu o problema e que o advogado nao apresentou Notice of Errata, e cita Lichfield v. Kubler, 183 F.4th 1248 (10th Cir. 2026). Nao houve sancao pecuniaria nem encaminhamento disciplinar. A base de Charlotin classifica o caso como "Lawyer", ferramenta "Implied", sem resultado (outcome) registrado.
Por que entrou: mostra o custo processual da alucinacao alem da multa: a citacao inventada entra no juizo de inadequacao do brief e contribui para que o tribunal deixe de examinar uma tese constitucional, com prejuizo direto ao cliente. Tambem documenta o padrao de responsabilizacao por nao corrigir depois do alerta da parte contraria, nao so por errar.


2. Officially corrected errors persist in AI training data: preregistered measurements on EU law, Internet standards and retracted science
Fonte: arXiv, Sebastien Gracia | URL primaria: https://arxiv.org/abs/2610.34379
Data de publicacao: 2026-10-25
Categoria: (c) risco novo importante
Sintese: O estudo mede se correcoes oficiais publicadas depois do texto original (corrigenda de atos da UE, errata verificada de RFCs, retratacoes cientificas) chegam aos datasets usados para treinar modelos. No EurlexResources, dataset juridico, 1.989 de 2.082 correcoes testaveis de atos da UE em lingua unica (95,5%, IC 94,6 a 96,3) continuam na forma errada; numa amostra aleatoria de 100, 46 alteram sentido, numero, remissao, autoridade competente ou escopo. Pelo menos 124 erros corrigidos de direito da UE aparecem na forma errada no FineWeb-2 e numa amostra do FineWeb. Em 59 perguntas sem documentos de apoio, cinco modelos deram a versao errada em 45% das respostas em que se comprometeram com uma versao (53% nas correcoes de escopo); so 1 resposta em 295 disse nao saber. Com as duas versoes lado a lado, escolheram a corrigida em 53% dos casos; quando cada versao trazia data e o rotulo de corrigendum, os quatro maiores modelos escolheram a corrigida em 99 a 100%. A comparacao entre um masked language model juridico e seu modelo base deu resultado nulo, e o autor declara que nao demonstra que as respostas venham dos datasets medidos. Pre-registro com hashes ancorados via OpenTimestamps; seis controles falharam e os desvios estao reportados. Dados em doi:10.5281/zenodo.23642239.
Por que entrou: identifica um vetor de erro silencioso para pipelines juridicos: o texto normativo "certo" no corpus pode ser a versao anterior a retificacao, e o modelo responde com confianca sem sinalizar duvida. O resultado de 99 a 100% com data e rotulo de corrigendum e um criterio operacional direto para ingestao em RAG: versionar a norma e expor metadado de retificacao ao modelo.


3. PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites
Fonte: arXiv, Yijie Hu, Wei Li, Junjie Zhou e outros (9 autores) | URL primaria: https://arxiv.org/abs/2610.35031
Data de publicacao: 2026-10-26
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: Benchmark com 510 instancias em oito suites de pratica de patentes: novelty search, freedom-to-operate (FTO), design FTO, invalidity search, claim charting, redacao de patente, resposta a office action e traducao. As instancias vem de registros reais e materiais profissionais, com anotacao revisada por especialistas; nas tarefas de busca o agente precisa pesquisar a colecao sem pool de candidatos fornecido, usando um servico MCP comercial de busca de patentes. Foram avaliados sete modelos (GPT-5.6-Sol, Qwen3.8-Max, Kimi K3, DeepSeek-V4-Pro, MiniMax-M3, GLM-5.3, Claude Opus 5) em quatro harnesses (Codex, Claude Code, Openclaw, Hermes). Melhor par modelo-harness: Claude Opus 5 com Hermes, media 52,8 de 100; o mesmo modelo cai para 31,2 no harness OpenClaw, o que isola o efeito do harness. Design FTO ficou entre 0,0 e 3,8 nas 27 combinacoes da tabela principal; em invalidity search, sob o mesmo harness, nenhum modelo recupera mais de um terco das referencias anotadas. Os autores relatam que minutas seguem a estrutura esperada mas sem camadas uteis de reivindicacoes dependentes, e que respostas a office action combinam alta taxa de conclusao com argumentacao juridica fraca. Avaliacao das tarefas redacionais por LLM judge (GPT 6 sol).
Por que entrou: e um eval que testa o gargalo real de agentes juridicos, recuperar evidencia sem candidato pre-selecionado e alinha-la a elementos de reivindicacao, e separa conclusao formal de qualidade substantiva. O desenho (tarefa de busca aberta mais rubrica de qualidade documental) e transponivel para pesquisa de jurisprudencia e minutas processuais.


REVISAO ADVERSARIAL

Item 1. Fonte: primaria (o proprio Order and Judgment, com cabecalho "Date Filed: 10/20/2026" e assinatura do painel), porem obtida em copia hospedada por terceiro (damiencharlotin.com). A URL resolve via curl (HTTP 200) e o PDF foi lido integralmente com pdftotext. Tentativa de URL no dominio oficial ca10.uscourts.gov devolveu 404: a localizacao no site oficial do tribunal fica [nao verificado]. Dominio damiencharlotin.com e o usado historicamente pela base; sem typosquat aparente. Nao verificado em segunda fonte: Lichfield v. Kubler, 183 F.4th 1248 (10th Cir. 2026), e a inexistencia dos dois precedentes, afirmada pelo tribunal mas nao checada de forma independente nesta execucao. O documento e Order and Judgment, em regra nao vinculante como precedente no 10th Circuit. A propria corte diz que os erros "appear to be" de IA: a autoria por IA nao esta estabelecida. Categoria (b) resiste: erro documentado em decisao judicial. Linguagem promocional: nenhuma.

Item 2. Fonte: primaria (preprint), autor unico identificado, sem revisao por pares. URL resolve (HTTP 200). Numeros extraidos do abstract via API do arXiv; tabelas e scripts nao conferidos [nao verificado no corpo do paper]. O DOI do Zenodo redireciona para zenodo.org, que respondeu 403 ao curl desta execucao: deposito dos dados [nao verificado]. Fragilidades declaradas pelo proprio autor: nao demonstra ligacao causal entre dataset e resposta do modelo; IC de 31 a 60% na taxa de 45% por agrupamento por pergunta; amostra de 59 perguntas. O escopo e direito da UE, nao brasileiro: a transposicao para DOU e retificacoes de normas nacionais e inferencia. Categoria (c) resiste. Linguagem promocional: nenhuma.

Item 3. Fonte: primaria (preprint), autores identificados, sem revisao por pares; afiliacoes nao conferidas [nao verificado]. URL resolve (HTTP 200). Numeros conferidos na versao HTML do arXiv (abstract e tabela principal), mas disponibilidade publica do dataset e do codigo nao localizada [nao verificado]. Fragilidades: LLM judge para tarefas redacionais; dependencia de servico comercial de busca nao nomeado no trecho lido; nomes e versoes de modelos citados como reportados pelos autores, nao checados. A media de 52,8 (Claude Opus 5 com Hermes) e a faixa de Design FTO foram conferidas na Tabela 3; a media por linha nao foi recalculada. Dominio patentario e parte do Direito, mas distante do contencioso brasileiro. Categoria (d) resiste. Linguagem promocional: nenhuma.

Origem social: nenhum item depende de post em rede social; as buscas site:x.com e reddit nao retornaram post datado na janela.


AUDITORIA

Janela: 36h rendeu 1 item qualificado (PatentAgentBench, 2026-10-26 08:44 UTC). Escalonado para 72h, que incluiu o preprint 2610.34379 (2026-10-25 15:34 UTC, fora do corte de 36h). Ainda 2 itens; escalonado para 7 dias, que incluiu Chilingarian v. Blanche (2026-10-20). Parou em 7 dias com 3 itens.

Deduplicacao: arquivo de 2026-10-26 lido; por causa da janela ampliada, tambem conferidos os arquivos de 2026-10-20 a 2026-10-25 (URLs e termos). Excluidos como duplicata: "AI Deepfakes in Court" (Volokh, 2026-10-25; item 2 de 2026-10-26); decisao da FLRA 74 FLRA No. 87 (ja citada em dias anteriores); arXiv 2610.30822, 2610.29961, 2610.28799 e 2610.32608 (ja citados); Law360 Pulse "Scholar Warns AI Pitfalls Can Go Beyond Hallucinations" (2026-10-26, paywall, trata da mesma analise de Charlotin que foi o item 1 de 2026-10-26).

Feeds que falharam ou vieram vazios: Stanford CodeX (HTTP 404); Above the Law tag IA (HTTP 200, sem entradas parseaveis); ConJur (HTTP 403, desafio Cloudflare; compensado com busca site:conjur.com.br, que so trouxe materias de outros veiculos e sem data na janela); Migalhas (HTTP 404). Feeds sem entradas na janela de 72h: Artificial Lawyer (ultima 2026-10-23), Unikowsky (2026-10-23), Charlotin Substack (2026-10-23), 3 Geeks (2026-10-14), Harvard Law Review Blog (2026-09-07).

Descartes:
"ClioCon 2026: A Quick Wrap-Up of Everything Clio Announced Today" (LawNext/LawSites, 2026-10-26): anuncios de fornecedor sem auditoria independente.
JOTA "Soberania digital: sonhos que poderemos viver" (2026-10-27): artigo de opiniao sobre agenda digital, sem dado verificavel sobre IA e Direito.
JOTA, 20 entradas restantes: eleicoes 2026, tributario, STF sem IA; fora do escopo.
Volokh, 15 entradas restantes: Woodward e a Suprema Corte, Guarda Nacional, tarifas, open threads; fora do escopo.
AI Hallucination Cases Database, 9 decisoes restantes de 2026-10-20 a 2026-10-23 (entre elas Moore v. Jackson Walker LLP, S.D. Texas, 2026-10-21, 13 citacoes ficticias e US$ 7.500, pro se): litigantes pro se ou advertencias sem elemento novo; Moore foi o candidato mais forte preterido por envolver parte sem advogado.
West Virginia, Supreme Court of Appeals, caso 25-425 (advogada questionada sobre syllabus points fabricados): sustentacao oral de 2026-09-22, cobertura de ABA Journal (2026-10-13), WV News (2026-10-08) e Gazette-Mail (2026-10-07); tudo fora da janela de 7 dias.
STJ, roundup sobre prompt injection e jurisprudencia inexistente (REsp 2.256.731, multa de 10% na Segunda Turma, 11 enunciados): republicado pelo Jornal Grande Bahia em 2026-10-24, mas a materia primaria do STJ e de 2026-10-18 e os julgamentos de setembro, fora da janela.
TSE, remocao de 20 publicacoes com deepfake contra a campanha de Lula (News Rondonia, 2026-10-22): fonte primaria no tse.jus.br respondeu 403 ao curl, sem confirmacao independente do ato; a Representacao 0600695-85.2026.6.00.0000 ja havia sido avaliada em 2026-10-20.
arXiv 2610.33605 (livro sobre governanca de dados para IA generativa, foco em direito indiano): texto de sintese, sem dado empirico novo.
Demais resultados WebSearch (JD Supra e ComplexDiscovery sobre sancoes do 1o trimestre, Bloomberg Law Mississippi de junho, Daily Journal sobre promotoria na California com HTTP 403, CNJ, TJSC, OAB, materias de previsoes para 2026, aivortex.io com estatisticas de fornecedor): sem data na janela, inacessiveis ou promocionais.

Substituicoes: nenhuma; as tres URLs primarias entregues resolveram via curl (HTTP 200).

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
