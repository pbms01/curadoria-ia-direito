CURADORIA DIARIA IA E DIREITO, 2026-11-05

CABECALHO
Data de coleta: 2026-11-05 (inicio 05:50 America/Sao_Paulo)
Janela aplicada: 72h (escalonada a partir de 36h)
Buscas WebSearch executadas: 15
Feeds RSS consumidos com sucesso: 9 de 13 (mais consulta complementar a API do arXiv e a base de Damien Charlotin)
Candidatos coletados: 96 (93 itens de feeds, API arXiv e base Charlotin dentro da janela de 72h, mais 3 resultados de busca checados individualmente)
Candidatos apos filtro deterministico: 11 (apos descarte de itens fora do tema, duplicatas de curadorias anteriores, entrevistas de fornecedor, anuncios de investimento e opiniao sem dado)
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional 33% / Substack-RSS 0% / social 0% (os 67% restantes sao fontes primarias: decisao judicial publicada e preprint academico)


1. Vokshi v. Canada (Citizenship and Immigration), 2026 FC 1346, Reasons and Judgment

Fonte: Federal Court of Canada, via AI Hallucination Cases Database (Damien Charlotin) | URL primaria: https://www.damiencharlotin.com/documents/3393/2026fc1346.pdf

Data de publicacao: 2026-11-03

Categoria: (b) erro ou fracasso documentado

Sintese: A juiza Ferron, da Federal Court of Canada (Montreal), julgou pedido de judicial review contra indeferimento de visto de super visa para uma cidada albanesa. Apos a audiencia, a Corte conferiu a jurisprudencia do memorial de fato e de direito e constatou que, exceto Vavilov (2019 SCC 65), Baker (1999) e Hassani (2006 FC 1283), todas as citacoes neutras remetiam a decisoes que nao sustentam os principios alegados e cujos nomes de partes nao correspondem a referencia, o que, segundo a decisao, indica geracao por IA (com remissao a Ahmed, 2026 FC 1202). A Corte invocou a practice direction de 7 de maio de 2024, que exige declaracao de uso de IA, e afirmou que a condicao de autorrepresentada na epoca da peca nao afasta as consequencias do descumprimento (Arora, 2026 FC 82; Okogun, 2026 FC 722). Registrou ainda que o advogado constituido depois nao tratou das citacoes inexistentes na audiencia. O pedido foi indeferido sem custas e, segundo a base de Charlotin, sem sancao profissional ou pecuniaria.

Por que entrou: Caso concreto com decisao publicada que mostra o mecanismo de deteccao (conferencia pos-audiencia pela propria Corte) e consolida uma linha de precedentes da FC canadense (Hussein, Arora, Okogun, Ahmed) tratando citacao fabricada como causa suficiente de esvaziamento do memorial. Relevante para quem desenha verificacao automatica de citacoes antes do protocolo.


2. Liminar impede Meta de coletar dados de sites jornalisticos para treinamento de IA

Fonte: JOTA (reportagem de Carolina Maingue Pires) | URL primaria: https://www.jota.info/justica/liminar-impede-meta-de-coletar-dados-de-sites-jornalisticos-para-treinamento-de-ia

Data de publicacao: 2026-11-04

Categoria: (c) risco novo importante (regulatorio e de propriedade intelectual)

Sintese: Em 3 de novembro de 2026, o juiz Guilherme Madeira Dezem, da 44a Vara Civel de Sao Paulo (processo 4214874-21.2026.8.26.0100), concedeu liminar em acao movida por ABERT, ANJ e ANER contra o Facebook Servicos Online do Brasil. A decisao suspende clausula dos novos Termos Comerciais (vigencia prevista para 20 de novembro) que condicionava a manutencao de contas de veiculos de imprensa a autorizacao para a Meta rastrear, coletar e armazenar conteudo, inclusive protegido por direito autoral, para treinar a Meta AI. A Meta fica impedida de indexar, armazenar em cache, coletar ou rastrear os dominios dos associados e de usar esse conteudo para alimentar IA, devendo manter as contas ativas sem tratamento diferenciado. O fundamento e a Lei 9.610/1998: o juiz qualificou raspagem, copia tecnica, tokenizacao e armazenamento para treino de LLMs como reproducao e utilizacao de obra protegida, e apontou que os veiculos nao detem poder de sublicenciar conteudo de terceiros (agencias, ilustradores, colaboradores). Multa diaria de R$ 1 milhao. A Meta nao comentou.

Por que entrou: Decisao judicial brasileira que descreve tecnicamente o pipeline de treino (scraping, tokenizacao, armazenamento) e o enquadra como reproducao sob a LDA, com efeito concreto sobre coleta de corpus. O argumento da cadeia de licencas (conteudo de terceiros sem sublicenca) e diretamente transponivel para quem monta bases de documentos juridicos para RAG ou fine-tuning.


3. LegalEvolver: Agentic Legal Judgment Prediction via Rubric-Guided Self-Evolution

Fonte: arXiv (cs.AI), Renmin University of China | URL primaria: https://arxiv.org/abs/2611.06381

Data de publicacao: 2026-11-04

Categoria: (d) solucao para gargalo em pipelines juridicos

Sintese: Xinyu Yang, Zhicheng Dou e coautores identificam a formulacao da query de busca como gargalo de agentes de retrieval para legal judgment prediction (artigo de lei, tipo penal e pena): agentes costumam montar a consulta direto do pedido e ignoram questoes juridicas latentes e fatos juridicamente salientes. O LegalEvolver gera queries otimizadas como sementes, resume rollouts em rubricas e alterna refinamento de rubrica com RL guiado por rubrica (co-evolucao). O agente usa quatro ferramentas de busca, entre elas precedentes do China Judgments Online, com encoder SAILER-zh de 768 dimensoes e busca exata FAISS. Sobre Qwen3-8B, em conjuntos balanceados de 1.000 casos do CAIL2018 e 2.000 do CMDL (201 tipos penais), a media geral foi 61,5, contra 60,4 do SmartSearch, 59,9 do GRPO padrao, 58,5 do SFT simples, 54,7 do GLARE e 45,2 de Agentic RAG generico. Predicao de pena continua o ponto fraco: acuracia de 22,1 no CAIL2018 e 25,6 no CMDL. Codigo anunciado em github.com/yxy-919/LegalEvolver.

Por que entrou: Ataca de forma mensuravel um gargalo recorrente em RAG juridico, a qualidade da query, com ablacao contra GRPO e SFT no mesmo checkpoint. A ideia de rubricas que premiam se a query cobre a questao juridica ainda aberta e transponivel para recuperacao de jurisprudencia em portugues, embora os ganhos sobre o baseline pos-treinado mais forte sejam de cerca de 1 ponto.


REVISAO ADVERSARIAL

Item 1 (Vokshi). Fonte primaria: sim, PDF da decisao com citacao neutra 2026 FC 1346 e marca CanLII, hospedado na base de Charlotin. Autor identificado: juiza Ferron, Federal Court. URL resolve: curl 200 em 2026-11-05. Dominio: damiencharlotin.com, oficial da base (sem typosquat). Nao verificado em segunda fonte: o resultado "sem sancao profissional ou pecuniaria" vem do resumo da base de Charlotin; o trecho do PDF lido confirma o indeferimento e a analise das citacoes, mas nao li o dispositivo integral sobre custas [nao verificado de forma independente]. Nao localizei a mesma decisao diretamente no canlii.org nesta execucao. Linguagem promocional: nenhuma. Categoria (b) resiste: erro documentado com consequencia processual. Ressalva de relevancia: litigante autorrepresentada, caso de baixo valor isolado; entrou pelo padrao jurisprudencial que consolida.

Item 2 (Meta/ABERT). Fonte: terceiros (JOTA), com autora identificada e numero do processo informado. URL resolve: curl 200. Dominio jota.info oficial. Nao verificados em segunda fonte: data da liminar (3/11), valor da multa (R$ 1 milhao/dia), numero do processo e a citacao literal do juiz; busca complementar nao encontrou outro veiculo cobrindo a decisao ate o momento da coleta. Recomenda-se conferir no e-SAJ do TJSP pelo numero 4214874-21.2026.8.26.0100. Linguagem promocional: nenhuma. Categoria (c) resiste: risco regulatorio emergente com decisao concreta, ainda liminar e sujeita a agravo.

Item 3 (LegalEvolver). Fonte primaria: preprint no arXiv, sem revisao por pares. Autores identificados com afiliacao institucional (Renmin University of China). URL do arXiv resolve: curl 200; numeros extraidos da versao HTML (Tabela 1). O repositorio GitHub retornou 403 no ambiente de coleta (provavel bloqueio do proxy), entao a disponibilidade do codigo nao foi confirmada [nao verificado]. Numeros nao reproduzidos de forma independente; datasets e baselines sao chineses, e a transferencia para portugues nao e testada. Linguagem promocional residual: o abstract fala em "extensive benchmarks", mas a avaliacao cobre dois datasets. Categoria (d) resiste, com a ressalva de ganho marginal sobre o baseline pos-treinado mais forte.

Origem social: nenhum item entregue tem origem em redes sociais.


AUDITORIA

Nivel de janela: 36h produziu apenas 2 itens qualificados com data seguramente dentro da janela (JOTA de 04/11 17:51 UTC e arXiv de 04/11). A decisao Vokshi tem data de 03/11 sem hora de publicacao, entao a janela foi escalonada para 72h, onde 3 itens se qualificaram. Nao houve escalonamento para 7 dias.

Feeds que falharam: Stanford CodeX, HTTP 404 (feedparser sem entradas); Migalhas, HTTP 404; Above the Law tag IA, HTTP 200 mas XML mal formado (bozo, 0 entradas); Damien Charlotin Substack e Adam Unikowsky, HTTP 200, sem posts na janela; 3 Geeks e Harvard Law Review Blog, HTTP 200, sem posts na janela. ConJur respondeu HTTP 200 (sem desafio Cloudflare nesta execucao), sem itens de IA na janela; busca site:conjur.com.br executada mesmo assim, sem resultado na janela. LawSites e LawNext retornaram o mesmo conteudo (redirecionamento para lawnext.com), contados uma vez.

Deduplicacao: arquivo de ontem (2026-11-04) lido; excluidos PROSE (arXiv 2611.04921) e as duas postagens do Volokh de 03/11 (handwritten opposition; Meta Moderation Assist). Por causa da janela de 72h, dedupe tambem contra 2026-11-02 e 2026-11-03: excluidos NitiBench+, Unlocking Criminal Court Decisions e ICJ-Graph.

Descartes com motivo:
Artificial Lawyer, "Litera Owner Hg + Anthropic Invest in AI Transformation Venture": parceria e investimento sem caso de uso mensuravel.
Artificial Lawyer, "Copilot for Legal, AL Interview": entrevista de fornecedor sem auditoria independente.
Artificial Lawyer, "Ex-Legorans Bag $2.4m For Real Estate AI Native": rodada de investimento, sem resultado.
Artificial Lawyer, "A Brief History of Generative Legal AI" e "Will AI Change the Identity of Law Firm Partners?": opiniao sem dado verificavel.
Artificial Lawyer, "Legal Innovators UK Starts Tomorrow": divulgacao de evento.
LawNext, entrevista com CPO da NetDocuments: fornecedor descrevendo o proprio produto.
LawNext, guest post sobre fixed fees: opiniao.
LawNext, Maine Bar troca Decisis por Clio Library: fato verificavel, mas sem resultado mensuravel nem dimensao tecnica.
Volokh, artigo do Journal of Free Speech Law sobre "forum interstitiale" (02/11): ensaio teorico sem caso concreto.
Korea Herald/Yonhap, pesquisa da Suprema Corte coreana (360 juizes, 80,7% ja viram precedentes inexistentes): publicado em 02/11 06:23 UTC, fora da janela de 72h; forte candidato, mas a regra de parada impede o escalonamento para 7 dias. Observacao: o texto atribui a 164 juizes terem citado precedentes falsos eles proprios, dado que parece inconsistente e precisa de conferencia na fonte coreana.
Law360, sancao de cerca de US$ 39 mil por citacoes de IA (S.D.N.Y.): publicado em 09/10, fora da janela; paywall.
Bloomberg Law, DOJ repreendido por citacao inexistente (Daghra v. Hinkley, W.D. Mich.): publicado em 16/07, fora da janela.
Bloomberg Law, sancoes aos dois lados em caso no Mississippi: junho de 2026, fora da janela.
Charlotin, The King v DPP (UK, 29/10), Nabors v. Nabors (Indiana, 29/10) e Estate of Ford (Texas, 29/10): fora da janela de 72h.
arXiv DeliverBench e EEFA: nao especificos de dominio juridico.
Buscas em X/Twitter, Reddit e Hacker News: nenhum post na janela com fonte primaria localizavel; resultados eram agregadores ou material antigo.
Resultados de busca de vendors e listas (azumo, nexlaw, attorneyaitools, "6 ferramentas de IA para advogados"): filtro deterministico (listas, conteudo de fornecedor, autoria nao identificavel).

Substituicoes: nenhuma.
Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
