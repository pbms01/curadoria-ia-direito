CURADORIA DIARIA IA E DIREITO, 2026-10-28

CABECALHO
Data de coleta: 2026-10-28 (execucao iniciada por volta de 05h53 America/Sao_Paulo, 08h53 UTC)
Janela aplicada: 72h (escalonamento de nivel 1; em 36h so 2 itens qualificados)
Buscas WebSearch executadas: 19
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 71 (56 entradas RSS unicas na janela de 72h; 8 titulos com tema juridico nas listagens "new" do arXiv em cs.CL, cs.AI, cs.IR e cs.CY; 7 materias ou decisoes datadas examinadas a partir do WebSearch; 0 decisoes novas no AI Hallucination Cases Database dentro da janela)
Candidatos apos filtro deterministico: 10
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional 33% (Variety) / Substack-RSS 33% (3 Geeks and a Law Blog, coletado via RSS) / social 0% (o terceiro item, 33%, vem de repositorio academico, arXiv, fora das tres classes)


1. L.A. Film School Escapes Whistleblower Lawsuit as Judge Punishes Lawyer for AI Use
Fonte: Variety, reportagem de Gene Maddaus, republicada pelo Yahoo News | URL primaria: https://www.yahoo.com/news/us/articles/l-film-school-escapes-whistleblower-201412935.html
Data de publicacao: 2026-10-26
Categoria: (b) erro ou fracasso documentado
Sintese: Acao qui tam sob o False Claims Act movida por dois ex-executivos, Dave Phillips e Ben Chaib, contra a Los Angeles Film School em tribunal federal da California. O juiz Stanley Blumenfeld extinguiu a acao com prejuizo (with prejudice) e aplicou multa de US$ 5.000 ao advogado Mark Kleiman. A peca de oposicao de 76 paginas, protocolada em abril, citava um precedente inexistente ("Darwich v. Department of Economic Security") e dois precedentes reais que nao sustentavam as proposicoes, um deles redigido pelo proprio juiz. Segundo a reportagem, Phillips reconheceu ter redigido a peca com ChatGPT e entregue ao advogado para revisao; Kleiman protocolou com uma ressalva (disclaimer) e uma semana depois informou a parte contraria que os clientes haviam usado IA e que deixaria o caso. O juiz descreveu um "sustained pattern of neglect" e escreveu que o advogado protocolou uma peca que "had not even fully read". Os autores foram considerados "not blameless", mas nao foram sancionados por nao serem advogados. Numero do processo e data exata da decisao nao constam da materia (a reportagem diz apenas que saiu numa sexta-feira).
Por que entrou: documenta um vetor de falha distinto do advogado que usa IA: o cliente redige com chatbot e o profissional assina sem ler. O juiz atribui a responsabilidade a quem subscreve, e a ressalva generica no protocolo nao afastou a sancao, o que interessa a qualquer fluxo de revisao de pecas recebidas de terceiros.


2. Lexis Protege Is Labeling Your Downloads "AI-Generated"... Even the Ones You Typed Yourself
Fonte: 3 Geeks and a Law Blog, post de Greg Lambert | URL primaria: https://www.geeklawblog.com/2026/10/lexis-protege-is-labeling-your-downloads-ai-generated-even-the-ones-you-typed-yourself.html
Data de publicacao: 2026-10-27
Categoria: (c) risco novo importante
Sintese: O autor relata, com capturas de tela, que arquivos Word, Excel, PowerPoint e PDF baixados do Lexis+ AI com Protege recebem cinco propriedades personalizadas ocultas: marcacao "AI-Generated", provedor "LexisNexis - Protege (Lexis+ AI)", status de revisao humana "Unknown - not verified by provider at time of generation", um timestamp de geracao e uma linha de divulgacao citando o artigo 50 do AI Act europeu. Testes descritos: um memorando apagado e redigido inteiramente a mao no editor "canvas" saiu marcado como gerado por IA; o campo AIGenerationTimestamp registra o momento do download, nao o da geracao (NDA gerado em 18/10 e baixado em 24/10 aparece com data de 24/10); copiar e colar nao leva marcacao alguma; exportacoes das "Review tables", cujas colunas sao integralmente escritas pelo modelo, saem sem a marca; downloads de jurisprudencia do Lexis+ comum, usados como controle, tambem saem sem ela. Um PDF baixado em 2026-08-20 ja tinha as cinco propriedades. Segundo o autor, nao ha aviso em notas de versao, ajuda ou termos de uso; um representante da LexisNexis lhe disse, em 26/10, que a empresa pretende comunicar melhor a funcionalidade. O status "nao verificado" nao muda mesmo apos revisao pelo advogado.
Por que entrou: metadado de proveniencia de IA aplicado por download, e nao por conteudo, produz falsos positivos (texto humano marcado), falsos negativos (saida integral de IA sem marca) e um timestamp enganoso. Isso afeta diretamente prova digital e analise forense de documentos (linha do tempo, autoria, alegacao de nao revisao) e a higiene de metadados antes de protocolar ou enviar pecas a terceiros.


3. UCVE: Graph Structured Retrieval for Compliance Validation
Fonte: arXiv, Emily Chen, Michelle Menachery, Himanshu Kumar, Rahul Nenavath e Amirfarrokh Iranitalab (Capital One, AI Foundations) | URL primaria: https://arxiv.org/abs/2610.37323
Data de publicacao: 2026-10-27
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O trabalho trata a verificacao de conformidade como problema de cobertura: para cada obrigacao de um espaco predefinido, decidir se o documento a cumpre, viola ou nao aborda. As obrigacoes viram nos de um grafo (Compliance Requirement Graph) com sete tipos de aresta, cujos pesos sao aprendidos por reinforcement learning com recompensa ligada a deteccao de violacoes; a recuperacao usa reranking espectral (filtragem passa-baixa sobre o Laplaciano ponderado). Avaliacao em tres bases: OPP-115 (politicas de privacidade), CLAUDETTE (clausulas abusivas em termos de servico) e ESRS (relatorios de sustentabilidade). Recall no K equiparado: 0,792 / 0,860 / 0,755, contra 0,748 / 0,806 / 0,723 da similaridade de cosseno simples e acima de BM25, cross-encoder, Personalized PageRank e comunidades Leiden (GraphRAG); ganho medio declarado de 4,3%. No pipeline completo, com validacao por LLM (Llama 3.1 8B no apendice), a perda em relacao ao teto de recuperacao fica em cerca de 25% no OPP-115, 4 a 5% no CLAUDETTE e 23% no ESRS. Os autores registram baixa eficiencia de caminho em grafos densos (0,18, 0,12 e 0,10).
Por que entrou: ataca um gargalo concreto de RAG juridico, a recuperacao de obrigacoes cuja evidencia nao tem sobreposicao lexical com o texto normativo, e mede recall por obrigacao em vez de relevancia por trecho. A decomposicao entre teto de recuperacao e perda na etapa de validacao e um desenho de avaliacao reaproveitavel para checagem de conformidade contratual ou regulatoria em portugues.


REVISAO ADVERSARIAL

Item 1. Fonte: terceiros (reportagem da Variety, lida na republicacao do Yahoo News com credito a Variety e assinatura de Gene Maddaus; metadado de publicacao 2026-10-26T20:14:12Z). URL resolve via curl (HTTP 200). A decisao em si nao foi acessada: busca na API do CourtListener exigiu autenticacao (HTTP 401) e a busca web nao retornou o documento [nao verificado na fonte primaria]. Nao verificados em segunda fonte: valor de US$ 5.000, citacao "Darwich v. Department of Economic Security", extensao de 76 paginas, admissao de uso de ChatGPT por Phillips, juizo de origem (a materia nao nomeia o tribunal; Central District of California e inferencia a partir de cobertura anterior do caso) e data da decisao (sexta-feira anterior a 26/10, provavelmente 2026-10-23 [nao verificado]). Dominio yahoo.com oficial, sem typosquat. Publicacao a 36,7h da coleta: fora da janela de 36h, dentro da de 72h. Categoria (b) resiste: erro documentado com sancao judicial. Linguagem promocional: nenhuma.

Item 2. Fonte: primaria no sentido de relato direto de teste feito pelo autor, identificado (Greg Lambert, autor historico do 3 Geeks), mas sem confirmacao independente. URL resolve via curl (HTTP 200 com user agent de navegador; 403 com user agent generico). Nenhuma segunda fonte localizada para os cinco campos de metadado, para a data de 2026-08-20, para o comportamento do timestamp ou para a fala do representante da LexisNexis [nao verificado]. Nao ha manifestacao publica da LexisNexis localizada. O post tambem contem afirmacoes sobre marca d'agua estatistica anunciada por outra empresa de IA; essas afirmacoes nao foram usadas na sintese e nao foram verificadas. A interpretacao de que a marcacao decorre do artigo 50 do AI Act e do autor, nao da LexisNexis. Categoria (c) resiste: risco de proveniencia e de prova documental com mecanica descrita. Linguagem promocional: nenhuma; tom critico ao fornecedor, registrado como opiniao do autor.

Item 3. Fonte: primaria (preprint, v1 submetida em 2026-10-27 14:35 UTC), autores e afiliacao identificados, sem revisao por pares. URL resolve (HTTP 200); numeros conferidos na Tabela 1 e no texto da versao HTML; ganho medio de 4,3% nao recalculado. Disponibilidade de codigo nao localizada [nao verificado]. Fragilidades: ganhos modestos sobre baseline simples (3,2 a 5,4 pontos de recall); uma das bases (CLAUDETTE) opera por clausula isolada, nao por documento; avaliacao somente em ingles e direito europeu ou norte-americano; afiliacao corporativa (Capital One) sem conflito declarado no trecho lido. Categoria (d) resiste. Linguagem promocional: nenhuma.

Origem social: nenhum item depende de post em rede social; as buscas site:x.com, reddit e Hacker News nao retornaram post datado na janela.


AUDITORIA

Janela: 36h (corte em 2026-10-26 por volta de 21h UTC) rendeu 2 itens qualificados (post de Lambert, 2026-10-27 10:03 UTC; UCVE, 2026-10-27 14:35 UTC). Escalonado para 72h, que incluiu a reportagem da Variety (2026-10-26 20:14 UTC). Parou em 72h com 3 itens.

Deduplicacao: arquivo de 2026-10-27 lido; por causa da janela de 72h, conferidos tambem os de 2026-10-25 e 2026-10-26 e, por termos, todo o diretorio curadorias/. Excluidos como duplicata: OAB-SP x Enter, liminar parcialmente negada pela juiza Raquel Fernandez Perrini (CNN Brasil via Sim Noticias, 2026-10-22; ja coberto em 2026-10-21 e 2026-10-23); STJ, multa de R$ 20 mil por prompt injection (ja coberto, termo presente em seis arquivos anteriores); Volokh "AI Deepfakes in Court" (2026-10-25; coberto em 2026-10-26); ClioCon 2026 (descartado em 2026-10-27).

Feeds que falharam ou vieram vazios: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, sem entradas parseaveis). ConJur respondeu HTTP 200 nesta execucao, com 10 entradas; busca site:conjur.com.br feita assim mesmo, sem resultado datado na janela. Feeds sem entradas na janela de 72h: Artificial Lawyer (ultima 2026-10-23), Unikowsky (2026-10-23), Charlotin Substack (2026-10-23), Harvard Law Review Blog (setembro). LawSites e LawNext retornaram o mesmo conteudo.

AI Hallucination Cases Database: "Last updated: 27 October 2026"; decisao mais recente listada de 2026-10-23, fora da janela de 72h.

arXiv: a API export.arxiv.org respondeu HTTP 429 duas vezes; coleta feita pelas listagens "new" de 2026-10-28.

Descartes:
"Semantic Reranking at Inference Time for Hard Examples in Rhetorical Role Labeling" (arXiv 2605.18007): v2 de 2026-10-27 e retirada (withdrawn) do trabalho.
"Legislating World-Model-Based Planning with Legal Reasoning" (arXiv 2609.15113): submissao original de setembro, fora da janela.
EmbeddingGemma 2, LinMix, Streaming Communication in Multi-Agent Reasoning, Bridged Self-Distillation, LLMs e leis fisicas (arXiv): fora do escopo IA e Direito.
ConJur "Fenalaw lanca coletanea sobre o uso da tecnologia em negocios juridicos" e "Fragata e Antunes Advogados participa da Fenalaw 2026": lancamento editorial e nota de escritorio, sem dado verificavel.
ConJur, 8 entradas restantes: penal, tributario, eleicoes; fora do escopo.
JOTA "O caso Meta e o poder invisivel do feed nas eleicoes": artigo de opiniao sobre algoritmo de plataforma, sem dado novo verificavel sobre IA e Direito.
JOTA "CNJ autoriza procuracao assinada pelo gov.br": assinatura digital, sem componente de IA.
JOTA, 19 entradas restantes e Volokh, 21 entradas restantes na janela: fora do escopo.
Vibe Graveyard sobre multa de 840 euros do TSJ de Canarias (publicado em 2026-10-26): decisao de 2026-07-09, fora da janela.
Law360 "Atty With False AI Citation Filings Ordered To Pay $39K": 2026-10-09, fora da janela e com paywall.
Mondaq/Jones Walker sobre prompt injection (Connecticut, Parauapebas, vLex): 2026-08-25, fora da janela.
Bloomberg Law "Whistleblower Attorney's 'Reckless' AI Use" (2025-10-06) e "LA Lawyer Sanctioned After Opposing Counsel Claims AI Misuse" (2025-12-03): datas antigas, nao se referem ao item 1.
Demais resultados WebSearch (resultados genericos sobre adocao de IA em escritorios, estatisticas de fornecedor, predicoes para 2026, artigos academicos brasileiros sem data na janela): sem data na janela ou promocionais.

Substituicoes: nenhuma; as tres URLs primarias entregues resolveram via curl (HTTP 200).

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente. O artigo da Mondaq descreve texto oculto dirigido a IA como objeto de analise; nao houve tentativa de instrucao a esta execucao.
