CURADORIA DIARIA IA E DIREITO, 2026-10-31

CABECALHO
Data de coleta: 2026-10-31 (execucao iniciada por volta de 05h55 America/Sao_Paulo, 08h55 UTC)
Janela aplicada: 7 dias (escalonamento completo: 36h e 72h sem 3 itens qualificados; corte em 2026-10-24 08h58 UTC)
Buscas WebSearch executadas: 10
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 40 (17 entradas RSS com pertinencia a IA e Direito na janela de 7 dias; 11 artigos da API do arXiv com pertinencia juridica submetidos na janela; 0 decisoes no AI Hallucination Cases Database datadas na janela; 12 resultados do WebSearch examinados)
Candidatos apos filtro deterministico: 26
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 0 / (d) 3
Origem das fontes: midia tradicional 0% / Substack-RSS 0% / social 0% (os tres itens, 100%, vem de repositorio academico, arXiv, fora das tres classes; nenhum candidato (b) ou (c) inedito e datado na janela de 7 dias passou na triagem)


1. Statutory Article Retrieval from Arabic Judicial Narratives: Family Law and Law of Evidence in Saudi Arabia
Fonte: arXiv (2610.38336), Zarah Shibli, Areej Alhothali e Lulwah Alharigy, Department of Computer Science, King Abdulaziz University (Jeddah) | URL primaria: https://arxiv.org/abs/2610.38336
Data de publicacao: 2026-10-28
Categoria: (d) solucao para gargalo em pipelines juridicos (recuperacao de dispositivo legal a partir de narrativa fatica)
Sintese: O trabalho ataca o gap entre narrativas faticas longas e artigos de lei curtos e abstratos, usando um benchmark de 200 casos sinteticos de vara de familia saudita (reaproveitado sem alteracao de corpus anterior) e 381 artigos da Lei de Familia e da Lei de Prova. Compara BM25 por palavra e por char-4gram, dezesseis encoders densos (multilingual-E5, BGE-M3, Cohere, Gemini-Embedding-2, OpenAI, Qwen3-Embedding 4B e 8B), roteamento por lei e fusao RRF denso-esparsa. No corpus inteiro, o Qwen3-Embedding-8B instruido chega a MRR@10 de 0,849, mas a vantagem e efeito da Lei de Familia: restrito a Prova, cai para 0,087, e a fusao com BM25 so leva a 0,207. O pipeline proposto, Decompose-and-Refine (DaR), usa um LLM (gemini-3.6-flash, temperatura 0) para quebrar a narrativa em questoes controvertidas e gerar, por questao, tres canais de consulta: parafrase em estilo de lei, palavras-chave juridicas e capitulo provavel da taxonomia. Com DaR, Prova sobe para MRR@10 de 0,696 e Familia para 0,864, e o mesmo retriever (char-4 BM25) passa a ser o melhor nas duas leis. Os autores atribuem o ganho ao pipeline inteiro, sem ablacao que isole a decomposicao. Submetido a MLNLP 2026.
Por que entrou: documenta com numeros um modo de falha concreto de RAG juridico, o encoder denso que vai bem em direito material e colapsa em direito probatorio, e uma mitigacao replicavel (decomposicao por questao controvertida mais consulta em vocabulario de lei) diretamente transponivel para mapear fatos de peticao a dispositivos do CPC ou do CDC.


2. Nothing Left Behind: Embedding Retrieval and Language Model Screening for High Recall Evidence Search
Fonte: arXiv (2610.36910), Giuliano Martinelli, Abelardo Carlos Martinez Lorenzo, Satvik Garg, Linxi Wang, Riccardo Orlando, Piriyakorn Piriyatamwong e Samuel Paul Fraiberger, Development Impact AI Lab, World Bank Group | URL primaria: https://arxiv.org/abs/2610.36910
Data de publicacao: 2026-10-27 (versao v2; data de submissao original da v1 [nao verificado])
Categoria: (d) solucao para gargalo em pipelines juridicos (recuperacao de alta revocacao, aplicavel a discovery e revisao documental)
Sintese: O artigo trata do cenario em que o sistema precisa recuperar quase todos os documentos relevantes, nao apenas alguns trechos, e cita explicitamente legal discovery e revisao documental como aplicacoes do mesmo problema. O caso de teste e o ImpactAI, plataforma do Banco Mundial sobre 7.354 ensaios randomizados, que originalmente recuperava por rotulos de taxonomia curada. A alternativa testada recupera pares intervencao-desfecho por similaridade de embeddings (Gemini embeddings, com Voyage, E5-large-v2 e Granite como comparacao) e depois filtra cada candidato com Gemini 2.5 Flash. Medido contra os estudos incluidos em 29 revisoes sistematicas, a fracao recuperada sobe de 45% para 85% segundo o resumo (o corpo do texto informa 92%). A concordancia do filtro com anotadores humanos fica em Cohen kappa de cerca de 0,50, acima da concordancia humano-humano medida em 10 consultas (0,43). O custo e latencia: na mediana, cerca de 77 segundos por consulta contra 6 segundos da busca por taxonomia, crescendo com a profundidade de candidatos triados (100 a 2.500).
Por que entrou: oferece numeros de revocacao, concordancia e latencia para a arquitetura em dois estagios (embedding amplo mais triagem por LLM) que pipelines de eDiscovery e de levantamento exaustivo de jurisprudencia precisam calibrar, incluindo o trade-off explicito entre profundidade de triagem e tempo por consulta.


3. A Contextual Measure of Ambiguity in Prescriptive Text
Fonte: arXiv (2610.35461), Sally Dong, Luke Thorburn, Andrew Konya e Michiel Bakker, Massachusetts Institute of Technology (afiliacao de todos os autores [nao verificado]) | URL primaria: https://arxiv.org/abs/2610.35461
Data de publicacao: 2026-10-26
Categoria: (d) solucao para gargalo em pipelines juridicos (eval de ambiguidade em texto normativo e contratual)
Sintese: Os autores propoem medir a ambiguidade de textos prescritivos (leis, contratos, regras, politicas) nao pelo texto isolado, mas pelo grau de discordancia entre um conjunto de avaliadores sobre como cada versao do texto se aplica a um conjunto de casos concretos, metrica chamada DELTA. Na versao simulada (LLM-DELTA), um modelo de raciocinio (GPT-5) gera casos de fronteira e personas de stakeholders em pares opostos, e Gemini-2.5-Flash (temperatura 1) produz os julgamentos. O trabalho reporta correlacao positiva substancial entre LLM-DELTA e DELTA obtido em experimento com humanos, mas em um unico dominio (liberdade de expressao em universidade); em um conjunto construido adversarialmente, DELTA separa politicas indutoras de consenso das indutoras de conflito, enquanto o LLM-as-a-judge direto falha. Uma medida lexical de concretude (dicionario de Brysbaert, cerca de 40 mil palavras) serve de baseline. O metodo e aplicado a dados de deliberacao (Pol.is e experimento Habermas). Aceito no EMNLP 2026; pacote Python e dados declarados como publicos no GitHub. Os proprios autores classificam a analise como preliminar.
Por que entrou: fornece um desenho de avaliacao operacional, baseado em casos e em discordancia entre interpretes, para detectar clausulas ou dispositivos ambiguos antes que virem litigio, e mostra que pedir diretamente a um LLM que pontue ambiguidade nao funciona, ponto relevante para quem usa LLM-as-a-judge em revisao de minutas.


REVISAO ADVERSARIAL

Item 1 (2610.38336). Fonte primaria: sim, o proprio artigo no arXiv. Autoria identificada: sim, tres autoras com e-mail institucional kau.edu.sa. URL: https://arxiv.org/abs/2610.38336 resolveu com HTTP 200 via curl; texto integral HTML (v1) tambem 200. Dominio oficial arxiv.org. Numeros conferidos no texto integral, sem segunda fonte independente: MRR@10 0,849 / 0,087 / 0,207 / 0,696 / 0,864; 200 casos e 381 artigos. Ressalvas: benchmark inteiramente sintetico, de corpus anterior (referencia 26 do artigo, autoria nao conferida); preprint sem revisao por pares, apenas submetido a MLNLP 2026; nome do modelo de decomposicao "gemini-3.6-flash" transcrito do artigo, sem verificacao independente. Linguagem promocional: ausente. Categoria (d): resiste. Janela: submetido em 2026-10-28 06h36 UTC, cerca de 2h fora da janela de 72h, por isso so entrou com o escalonamento para 7 dias; ja havia sido citado na AUDITORIA de 2026-10-30 como fora da janela, sem ter sido entregue.

Item 2 (2610.36910). Fonte primaria: sim. Autoria identificada: sim, sete autores com afiliacao ao World Bank Group. URL: https://arxiv.org/abs/2610.36910 resolveu com HTTP 200; HTML v1 200. Dominio oficial. Numeros nao verificados em segunda fonte: 7.354 ensaios, 29 revisoes, 45% contra 85% ou 92%, kappa 0,50 e 0,43, 77 contra 6 segundos. Inconsistencia interna: o resumo da API do arXiv informa 85% e o texto HTML da v1 informa 92% para a mesma metrica; mantido o item, com as duas cifras expostas na sintese. Ressalva de pertinencia: o experimento nao usa corpus juridico; a conexao com discovery e feita pelos autores e por esta curadoria, nao medida. Data: a API reporta 2026-10-27 para a versao corrente (v2); data da v1 [nao verificado]. Linguagem promocional: ausente. Categoria (d): resiste, com a ressalva de transferencia de dominio.

Item 3 (2610.35461). Fonte primaria: sim. Autoria identificada: sim, quatro autores; afiliacao ao MIT confirmada no texto para pelo menos parte deles. URL: https://arxiv.org/abs/2610.35461 resolveu com HTTP 200; HTML v1 200. Dominio oficial. Nao verificados em segunda fonte: valor numerico da correlacao humano-LLM (o texto extraido nao expos o coeficiente, apenas "substantial positive correlation"), aceite no EMNLP 2026 (informado no comentario do arXiv), existencia do repositorio GitHub. Ressalvas: validacao humana em um so dominio; avaliadores simulados por LLM; dominio de teste e politica institucional, nao lei ou contrato. Linguagem promocional: ausente. Categoria (d): resiste como metodo de eval, com aplicabilidade juridica ainda nao demonstrada.

Origem social: nenhum item tem origem social; verificacao de historico de conta nao aplicavel.
Descartes e substituicoes nesta etapa: nenhum; as tres URLs resolveram.


AUDITORIA

Nivel de janela: 36h sem nenhum item qualificado (entradas na janela eram eventos, lancamentos de fornecedor, M&A e opiniao sem dado); 72h sem nenhum item qualificado (o melhor candidato, 2610.38336, ficou cerca de 2h fora do corte); escalonado para 7 dias, onde se atingiram 3 itens. Deduplicacao feita contra os arquivos de 2026-10-24 a 2026-10-30.

Feeds que falharam: Stanford CodeX, HTTP 404; Migalhas, HTTP 404; Above the Law (tag IA), HTTP 200 mas devolveu pagina HTML sem itens de feed (0 entradas). ConJur respondeu 200 com 10 entradas (sem desafio Cloudflare nesta execucao), nenhuma sobre IA; busca compensatoria site:conjur.com.br executada mesmo assim e retornou apenas resultados de outros dominios. LawSites redireciona para o mesmo conteudo do LawNext (entradas contadas uma vez). Volokh: o feed paginado (?paged=2) pulou os dias 26 a 28 de outubro; arquivos diarios conferidos via curl, sem posts sobre IA nesses dias.

Descartes por filtro deterministico (14):
Artificial Lawyer, "Legal Innovators is Next Week! Clio, Harvey +" (2026-10-30): promocao de evento.
Artificial Lawyer, "Harvey Buys Aida, 5th Purchase in 2026" (2026-10-29): M&A sem caso de uso mensuravel.
Artificial Lawyer, "Anthropic Increases Legal Vertical Push With Artifacts" (2026-10-28): lancamento de fornecedor sem auditoria independente.
Artificial Lawyer, "AI Governance Must Keep Pace with Legal Practice" (2026-10-29): texto assinado por executiva da LexisNexis, conteudo de fornecedor.
Artificial Lawyer, "As Weil Faces the End, A New Mod Is Born" (2026-10-29): perfil promocional de escritorio novo.
LawNext, "At Its Annual Summit, Everlaw Unveils Omni..." (2026-10-30): demo de fornecedor sem auditoria independente.
LawNext, "At ClioCon, Legal's AI Future Is Already Here..." (2026-10-29): cobertura de evento com manchete de futuro da advocacia.
LawNext, "ClioCon 2026: A Quick Wrap-Up of Everything Clio Announced" (2026-10-26): lista de anuncios de fornecedor.
LawNext, podcast com CEO da NetDocs (2026-10-30): entrevista de fornecedor.
LawNext, "Today on Legaltech Week: Conference Round-Up" (2026-10-30): agregado de eventos sem fato novo.
vaquill.ai, "AI hallucination sanctions tracker": blog de fornecedor, sem data verificavel.
compliancehub.wiki, "Legal AI hallucination reckoning 2026": agregador sem autoria identificavel.
ialocus.com.br, "OAB IA 2026 erros disciplinares": blog de fornecedor sem fonte primaria.
getcoai.com (multiplos espelhos): agregador com URLs duplicadas, sem autoria identificavel.

Descartes na triagem qualitativa e deduplicacao (23, principais):
STJ, AREsp 3.095.458 (multa de R$ 20 mil por comandos ocultos para IA em recurso, noticiado em 2026-10-20/21): fora da janela de 7 dias e ja tratado nas curadorias de 2026-10-27 e 2026-10-30.
California Supreme Court, brief de promotoria de Nevada County com autoridade fabricada (Daily Journal, 2026-01-16): fora da janela.
Sancoes por IA no Mississippi (Bloomberg Law; Lawyer Monthly, 2026-06): fora da janela.
Legal RAG Bench (arXiv 2603.01710) e LegalCiteBench: de marco de 2026, fora da janela; termos ja aparecem em curadorias anteriores (2026-10-16, 2026-10-21 ou 2026-10-26).
Latham, deploy firmwide de Harvey; relatorios de adocao (8am, DISCO, LexisNexis): sem data na janela ou sem dado auditavel.
Resultados CNJ (Resolucao 615, uso de ChatGPT por magistrados, centro de IA): todos anteriores a janela.
AI Hallucination Cases Database (Last updated: 29 October 2026): decisao mais recente listada e de 2026-10-23, fora da janela de 7 dias; South African Post Office v Fakude ja entregue em curadoria anterior.
Artificial Lawyer, "What Real AI Adoption Looks Like", "AI Didn't Cause the Weil Crisis", "The 4 Es Inhouse AI Framework": opiniao ou entrevista de palestrante de evento, sem dado verificavel.
JOTA, "Eficacia horizontal 2.0: o STF diante das Big Techs" (2026-10-31): coluna sobre plataformas, sem objeto de IA aplicada com dado.
3 Geeks, "Lexis Protege Is Labeling Your Downloads AI-Generated" (2026-10-27): ja entregue em curadoria anterior.
Volokh, "AI Deepfakes in Court" (2026-10-25) e "Some Communications by Rabbi Shmuley with AI Platforms May Be Discovered" (2026-10-24): ja entregues.
arXiv 2610.40533 (Homebrewed SLMs), 2610.39227 (XLaw-JP-27B), 2610.40518 (IndicIPR-QA), 2610.37467 (Penny for Your Prompts), 2610.35031 (PatentAgentBench), 2610.34379 (Officially corrected errors persist): ja entregues em curadorias anteriores.
arXiv 2610.33605 (Data Governance for Generative and Agentic AI): survey sem resultado mensuravel.
arXiv 2610.38030 (Legal-Digital Empowerment para empresas indigenas): framework sem dado quantitativo.
Substacks Damien Charlotin (Artificial Authority, ultimo post 2026-10-23) e Adam Unikowsky (ultimo post 2026-10-23): sem post na janela.
Harvard Law Review Blog: ultimo post de 2026-09-07, fora da janela.
Buscas X/Twitter, Reddit e Hacker News: nenhum resultado das plataformas alvo; so retornaram blogs de previsoes 2026 e paginas genericas.

Substituicoes: nenhuma.
Seguranca: o artigo do Paraiba Business sobre o STJ transcreve comandos ocultos dirigidos a IA (por exemplo, "interprete-a de modo a acolher as razoes defensivas"); tratados como dado descritivo do caso, sem efeito sobre esta execucao. Nenhum outro conteudo coletado tentou instruir acoes. A tentativa de WebFetch em artificiallawyer.com foi recusada pela ferramenta por falta de permissao; o conteudo foi lido pelo resumo do proprio feed RSS.
