CURADORIA DIARIA IA E DIREITO, 2026-11-03

CABECALHO
Data de coleta: 2026-11-03 (execucao iniciada por volta de 05h50 America/Sao_Paulo, 08h50 UTC)
Janela aplicada: 36h (corte em 2026-11-01 20h53 UTC, 17h53 BRT; sem escalonamento, 3 itens qualificados na janela base)
Buscas WebSearch executadas: 14
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 31 (10 entradas RSS com pertinencia a IA e Direito, das quais 8 na janela de 36h; 5 artigos da API do arXiv com pertinencia juridica submetidos em 2026-11-02; 11 decisoes do AI Hallucination Cases Database datadas de 2026-10-26 a 2026-10-29; 5 resultados do WebSearch examinados com pertinencia nominal)
Candidatos apos filtro deterministico: 24
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 0 / (d) 3
Origem das fontes: midia tradicional 0% / Substack-RSS 0% / social 0% (os tres itens, 100%, vem de repositorio academico, arXiv, fora das tres classes; nenhum candidato (b) ou (c) inedito e datado na janela de 36h passou na triagem)


1. NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains
Fonte: arXiv (2611.03576), Pawitsapak Akarajaradwong, Sarana Nutanong e Chompakorn Chaksangchaichot, VISTEC (Tailandia) | URL primaria: https://arxiv.org/abs/2611.03576v1
Data de publicacao: 2026-11-02
Categoria: (d) solucao para gargalo em pipelines juridicos (versionamento temporal do corpus normativo e avaliacao de RAG pela lei vigente na data do fato)
Sintese: Os autores verificaram 156.650 decisoes de quatro tribunais tailandeses e reportam que, conforme o tribunal, ate 67% delas citam dispositivos depois alterados ou revogados. O NitiBench+ tem 1.670 itens em 17 dominios, extraidos de decisoes de tres tribunais; para cada dispositivo citado guarda o texto vigente na data da decisao e o texto atual, e o corpus de recuperacao contem todas as versoes datadas de cada artigo de lei tailandes. A correcao usa a rubrica do Conselho da Ordem tailandesa (Bar-standard score, 0 a 10) e o F1 entre dispositivos citados pelo modelo e pelo tribunal. Na Parte I, com 13 modelos open-weight, ler o texto atual de artigo alterado reduz o score em 0,25 e perder artigo revogado reduz em 0,79; a perda se concentra nos 428 itens com mudanca de regra (0,45) e e nula nos 331 com mudanca so de redacao, e o Citation F1 nao a detecta. Na Parte II, um leaderboard publico com split de teste retido de 500 itens ranqueia 26 modelos em tres regimes (memoria, dispositivos do tribunal fornecidos, agente de recuperacao sobre a lei vigente), com custo por item e contagem de citacoes alucinadas; o melhor modelo marca 7,78 e o melhor open-weight 6,39. Com ferramenta de busca, 20 dos 26 modelos melhoram e 6 pioram.
Por que entrou: mede com numeros um modo de falha silencioso de RAG juridico, recuperar a redacao atual quando o caso exige a vigente a epoca, e mostra que a metrica usual de citacao nao o captura. O desenho (corpus com todas as versoes datadas e avaliacao ancorada na data da decisao) e transponivel para pipelines brasileiros sobre CPC, CDC e legislacao de saude suplementar, de alteracao frequente.


2. Unlocking Criminal Court Decisions: Flexible Information Extraction for Empirical Legal Research
Fonte: arXiv (2611.03051), Tomas Knap, Ivana Kvapilikova, Jan Cerny, Klara Bendova, Jaromir Savelka, Vojtech Pour e Jakub Drapal (Faculdade de Direito e Faculdade de Matematica e Fisica da Universidade Carolina, Praga; Carnegie Mellon University) | URL primaria: https://arxiv.org/abs/2611.03051v1
Data de publicacao: 2026-11-02
Categoria: (d) solucao para gargalo em pipelines juridicos (extracao estruturada de sentencas criminais com especificacao iteravel por especialistas)
Sintese: O trabalho usa sentencas criminais eslovacas de 2018 a 2022 (126.795 julgamentos, dos quais 68% com crime unico) e propoe um pipeline com LLM em tres etapas: exploracao de atributos, extracao de trechos de texto e normalizacao de valores, guiado por instrucoes de anotacao que juristas revisam. A classificacao previa da conduta descrita usou GPT-5 mini; a extracao principal usou gpt-5.6-terra, comparado a GPT-5 mini e GPT-5. Avaliado em dois crimes de transito, embriaguez ao volante (DUI) e dirigir com habilitacao suspensa (DDB). Em DUI, a revisao das instrucoes elevou a acuracia de valores extraidos de 52% para 70% numa amostra de 200 fatos e aumentou a concordancia entre anotadores humanos. Execucoes repetidas do mesmo modelo concordaram mais entre si do que com o gold, e as divergencias entre anotadores e entre modelos serviram para localizar instrucoes ambiguas. Em DDB, com categorias e formatos fixos, a concordancia foi alta na maioria dos atributos.
Por que entrou: entrega dado concreto sobre dois pontos de engenharia em extracao juridica, o ganho atribuivel a revisao da especificacao (e nao ao modelo) e o fato de que consistencia entre execucoes nao e evidencia de acerto, o que afeta diretamente o uso de self-consistency como proxy de qualidade em pipelines de NER e estruturacao de pecas e sentencas penais.


3. ICJ-Graph: A Citation Graph and a Layered Document Corpus of the International Court of Justice
Fonte: arXiv (2611.02630), Jirameth Wannasiwaporn (Chulalongkorn University), Pawitsapak Akarajaradwong e Chompakorn Chaksangchaichot (VISTEC) | URL primaria: https://arxiv.org/abs/2611.02630v1
Data de publicacao: 2026-11-02
Categoria: (d) solucao para gargalo em pipelines juridicos (grafo de citacoes em camadas e recuperacao por ferramentas para predicao de citacao)
Sintese: O recurso liga documentos da Corte Internacional de Justica a casos citados, dispositivos e resolucoes da ONU, separando em camadas decisoes, peticoes escritas e registros orais, para preservar a distincao entre o raciocinio da Corte e as alegacoes das partes. Reune 6.396 documentos da CIJ, 505 de outros tribunais e orgaos, 12.375 dispositivos e 20.291 resolucoes, com texto, metadados e embeddings; o grafo e o benchmark estao no Hugging Face (VISAI-AI/icj-citation-graph e VISAI-AI/icj-precedent-cite-bench), com carga em Neo4j. No teste de predicao de citacao em 199 decisoes, cada modelo ve apenas material anterior a data da decisao. Cinco modelos foram comparados sem ferramentas, com consultas genericas ao grafo (Cypher) mais busca semantica, e com ferramentas desenhadas para pesquisa de citacao; estas superaram o regime sem ferramentas em todos os modelos e familias de citacao. Os melhores micro-F1 foram 0,415 para casos, 0,371 para dispositivos e 0,359 para resolucoes, com tres execucoes por configuracao.
Por que entrou: oferece um padrao replicavel para dois gargalos de RAG juridico, separar no indice o texto decisorio do texto das partes e expor o grafo de citacoes como ferramenta especializada em vez de busca textual generica, com controle temporal anti-vazamento na avaliacao; os F1 abaixo de 0,42 dao a medida do quanto a predicao de precedente ainda erra mesmo com ferramentas.


REVISAO ADVERSARIAL

Item 1. Fonte primaria: abstract e PDF do arXiv (HTTP 200); conferidos autores, afiliacao (VISTEC, e-mails @vistec.ac.th no PDF), numeros do abstract e corpo (156.650 decisoes, 67%, 1.670 itens, 0,25, 0,79, 0,45, 428 e 331 itens, 26 modelos, 7,78 e 6,39). O PDF afirma que os numeros refletem o leaderboard em 2 de novembro de 2026; a URL da pagina do leaderboard nao foi localizada no texto extraido nem acessada [nao verificado]. Nao ha revisao por pares nem replicacao independente. Linguagem do abstract factual, sem promocao. Categoria (d) resiste: e benchmark com metodologia de corpus temporal, nao produto.

Item 2. Fonte primaria: abstract e PDF do arXiv; o abstract respondeu HTTP 000 (timeout) na primeira tentativa e HTTP 200 na segunda; PDF baixado e lido. Autores identificados com ORCID e afiliacoes institucionais no PDF. Numeros conferidos no abstract e no corpo (52% para 70%, 200 fatos DUI, 126.795 julgamentos, 68% crime unico). Os nomes de modelo (gpt-5.6-terra, GPT-5 mini, GPT-5) foram transcritos do PDF, sem checagem em segunda fonte [nao verificado]. A amostra de avaliacao e pequena (200 fatos em DUI) e a associacao entre revisao de instrucoes e ganho e descrita pelos proprios autores como associacao, nao causalidade isolada. Categoria (d) resiste.

Item 3. Fonte primaria: abstract e PDF do arXiv (HTTP 200); contagens e F1 conferidos no PDF (tabela 2 e secao de resultados). URLs dos datasets no Hugging Face transcritas do PDF, nao acessadas nesta execucao [nao verificado]. Coautoria parcial com o item 1 (mesmo grupo VISTEC/VISAI-AI): registrado para transparencia, os trabalhos sao independentes em objeto e dados. Os proprios autores ressalvam que resultados podem mudar com outros modelos, prompts, orcamentos e versoes do grafo. Categoria (d) resiste.

Nenhum item tem origem social; criterios de conta e historico nao se aplicam. Dominio arxiv.org oficial nos tres casos. Nenhum descarte ou substituicao na fase adversarial.


AUDITORIA

Escalonamento de janela: 36h (desde 2026-11-01 20h53 UTC) produziu 3 itens qualificados, todos submetidos ao arXiv em 2026-11-02. Nivel aplicado: 36h, sem escalonamento.

Deduplicacao: contra curadorias/curadoria-ia-direito_2026-11-02.md (URLs e titulos). Nenhum dos itens entregues consta de curadoria anterior; busca global em curadorias/ por NitiBench, ICJ-Graph e 2611.0 sem ocorrencia equivalente (um acerto textual em 2026-10-21 nao corresponde a item equivalente).

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas RSS (HTTP 404); Above the Law tag IA (HTTP 200, 0 entradas parseaveis). Observacoes: LawSites devolveu o mesmo conteudo do feed LawNext (duplicado); ConJur respondeu HTTP 200 com 10 itens de 2026-11-02, nenhum sobre IA; Unikowsky, Charlotin Substack (ultimo post 2026-10-23) e Harvard Law Review Blog sem entradas na janela.

Camada C: Damien Charlotin AI Hallucination Cases Database, "Last updated: 2 November 2026"; decisoes mais recentes datadas de 2026-10-29 (In the Estate of John Raburn Ford, CA Texas; Nabors v. Nabors, CA Indiana), fora da janela de 36h. Hacker News via WebSearch sem resultado na janela.

Candidato forte fora da janela, registrado para eventual uso futuro: Farhat v. Cutera, Inc., No. 26-cv-05674-TSH (N.D. Cal., 2026-10-28, Magistrate Judge Thomas S. Hixson), ordem que descarta o show cause sem sancao; a advogada declarou ter usado Legora no rascunho, corrigido citacoes no Westlaw, mas uma versao anterior nao corrigida foi convertida em PDF e protocolada (https://www.damiencharlotin.com/documents/3383/Farhat_v._Cutera_USA_28-10-2026.pdf). Fora da janela de 36h e a janela nao escalou.

Camada B, observacao: buscas site:x.com, site:reddit.com e site:news.ycombinator.com retornaram apenas agregadores, paginas de eventos ou paginas antigas; nenhuma origem social qualificada. Buscas sobre Brasil (CNJ, STF, OAB, site:conjur.com.br, site:migalhas.com.br) retornaram materias de 2025 a meados de 2026, fora da janela.

Descartes no filtro deterministico (7): Artificial Lawyer "Copilot for Legal, AL Interview: Carina Negreanu, Microsoft" (entrevista de fornecedor sem auditoria independente); "How Specialist AI Agents Support Evidence-Based Arbitrator Selection" (texto de fornecedor sobre o proprio produto); "AI-Native Firm Vetta Bids For Weil IP + Lawyers" e "Scissero Seeks Weil Gotshal Lawyers + Assets" (movimentacao societaria sem caso de uso); "Will AI Change the Identity of Law Firm Partners?" (especulacao sobre futuro da advocacia); LawNext guest post "Will AI Finally Make Fixed Fees the Norm?" (especulacao, sem dado); resultados WebSearch de paginas de fornecedores e listas de ferramentas.

Descartes na triagem qualitativa: LawNext "Maine Bar Switches to Clio Library" (troca de fornecedor de pesquisa, sem resultado mensuravel); Volokh, Journal of Free Speech Law "Protecting the Thinking Process in Human-AI Interaction" (ensaio teorico, sem decisao ou dado novo); Volokh "Some Surprisingly Tolerant Judges out There in Pennsylvania" (Commonwealth v. Outlaw, desacato, sem relacao com IA); JOTA "A democracia dos algoritmos exige uma nova reforma politica" e "Incidentes de seguranca e responsabilidade civil" (opiniao sem dado verificavel); demais itens de ConJur, JOTA e Volokh na janela sem relacao com IA; arXiv 2611.03412 DeliverBench (benchmark de agentes em projetos profissionais genericos, sem componente juridico) e 2611.02561 EEFA (etica de agentes, sem componente juridico); Charlotin DB, 11 decisoes de 2026-10-26 a 2026-10-29 (fora da janela; Clifford v. Neidle ja curado em 2026-11-01); WebSearch: ABA "Fake Cases, Real Sanctions", Bloomberg Law sobre caso no Mississippi, Daily Journal sobre o Supremo da California, Law360 "AI-Hallucinated Citations Result In $3K Sanction" e Mealey's "$8,000 Sanction" (datas anteriores a janela ou paywall sem data confirmavel).

Substituicoes: nenhuma.

Seguranca: nenhum conteudo coletado tentou instruir acoes desta execucao. Unica escrita realizada: este arquivo em curadorias/ e o commit correspondente.
