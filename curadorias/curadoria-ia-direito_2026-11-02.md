CURADORIA DIARIA IA E DIREITO, 2026-11-02

CABECALHO
Data de coleta: 2026-11-02 (inicio 05:53 America/Sao_Paulo)
Janela aplicada: 7 dias (2026-10-26 a 2026-11-02), apos escalonamento 36h, 72h, 7 dias
Buscas WebSearch executadas: 21
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 87 (64 itens unicos de feeds dentro da janela de 7 dias, 9 papers arXiv via API, 14 resultados web com data ou fato novo na janela)
Candidatos apos filtro deterministico: 78
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional e fonte oficial 67% / Substack-RSS-preprint 33% / social 0%


1. AI video of his victim played during trial. Arizona appeals court says he should be resentenced (sobre State v. Horcasitas, No. 1 CA-CR 25-0191, Arizona Court of Appeals, Division One)
Fonte: KJZZ (Matthew Casey) | URL primaria: https://coa1.azcourts.gov/Portals/1/OpinionFiles/Div1/2026/State%20v.%20Horcasitas%20-%201%20CA-CR%2025-0191%20-%20Opinion.pdf
Fonte secundaria (noticia do fato novo): https://www.kjzz.org/kjzz-news/2026-10-30/ai-video-of-his-victim-played-during-trial-arizona-appeals-court-says-he-should-be-resentenced
Data de publicacao: 2026-10-30 (reportagem KJZZ); opiniao do tribunal FILED 2026-09-30
Categoria: (b) erro ou fracasso documentado
Sintese: Na audiencia de sentenca de Gabriel Horcasitas, condenado por manslaughter apos matar Chris Pelkey em briga de transito, a familia exibiu como victim impact statement um video gerado por IA em que um avatar da vitima "falava" ao tribunal e ao reu, declarando perdoa-lo. O juiz Todd F. Lang (Maricopa County Superior Court) disse "I loved that AI", qualificou o video como "genuine" e fixou 10,5 anos, acima dos 9 pedidos pela acusacao. Em opiniao publicada e unanime (relator D. Steven Williams, com Anni Hill Foster e David D. Weinzweig), a Division One manteve a condenacao, mas anulou a pena sob revisao de fundamental error: o video "does not reflect actual events", "erases the interpretive distance between the family's belief about what the victim would have said and the victim's own voice" e "No disclaimer could cure that error" (paragrafos 50 a 53). O tribunal registrou que nenhum precedente do Arizona havia tratado de representacao de vitima gerada por IA e usou State v. Rose como parametro; os videos reais da vitima embutidos na peca foram considerados permissiveis. A reportagem de 2026-10-30 informa que a acusacao recorreu do resentenciamento a Suprema Corte estadual.
Por que entrou: primeiro precedente publicado que fixa a exigencia de "minimal indicia of reliability" para conteudo sintetico em sentenca e declara que disclaimer nao sana o vicio. E criterio operacional direto para prova digital e para qualquer pipeline que gere reconstituicoes audiovisuais com finalidade processual.


2. Desembargador adverte advogados por uso de IA em embargos; OAB/RS reage
Fonte: Migalhas | URL primaria: https://www.migalhas.com.br/quentes/467655/desembargador-adverte-advogados-por-uso-de-ia-em-embargos-oab-rs-reage
Fonte secundaria (confirmacao independente): https://ambitojuridico.com.br/ia-embargos-trt4-assinatura-representacao-prazo
Data de publicacao: 2026-10-31
Categoria: (c) risco novo importante (regulatorio e procedimental)
Sintese: Em sessao no TRT da 4a Regiao, o desembargador Marcal Henri dos Santos Figueiredo afirmou que a turma pretende nao conhecer embargos de declaracao abusivos produzidos com auxilio de IA e aplicar multa por litigancia de ma-fe, dizendo que "nos temos como detectar a inteligencia artificial, porque o tribunal tambem a usa". Como indicios, citou a alta de embargos em seu gabinete de uma media de 30 para 70, recursos que atacam questoes nao decididas no acordao e materias nunca debatidas no processo. O presidente da OAB/RS, Leonardo Lamachia, classificou a fala como "quase que uma intimidacao" e defendeu tratamento "no caso concreto". Nao ha numero de processo, decisao escrita nem multa aplicada identificados; o Ambito Juridico registra que a manifestacao "nao e uma proibicao geral de IA pelo TRT4" e lembra que o art. 897-A, par. 3o, da CLT ja preve hipoteses de nao interrupcao de prazo independentes do uso de IA.
Por que entrou: sinaliza deslocamento do controle de "citacao falsa" para "volume e pertinencia" como indicio de IA, com ameaca de nao conhecimento e efeito sobre prazo, e explicita a assimetria (tribunal usa IA para detectar IA). Criterio de risco: a deteccao alegada nao tem metodo publicado, o que abre litigio sobre falso positivo.


3. Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG
Fonte: arXiv (cs.CL), Ivan Kochergin (Letovo School, Moscou) e Vasily Konovalov | URL primaria: https://arxiv.org/abs/2610.40966
Data de publicacao: 2026-10-29
Categoria: (d) solucao para gargalo em pipelines juridicos (avaliacao de abstencao em RAG)
Sintese: Paper de reprodutibilidade sobre o atalho, usado em benchmarks de RAG conversacional (MTRAG, RETECO/SemEval-2027), de considerar "sem resposta" todo contexto recuperado que nao contem documento gold nas qrels. Os autores reexecutam os baselines oficiais no RECOR com quatro retrievers (nDCG@10 de 0,18 a 0,59) e tres leitores Qwen3, rotulando a suficiencia de cada contexto por conteudo com dois juizes LLM abertos, um painel de quatro modelos pequenos e auditoria cega de 250 contextos. Quanto melhor o retriever, maior a fracao de contextos sem gold que ainda contem a resposta (28% a 72%) e menor a precisao do atalho (0,68 para 0,10; 0,70 para 0,21 na auditoria). O Qwen3-4B responde corretamente 62% a 67% desses falsos "sem resposta". No MTRAG, com qrels de anotadores humanos, a precisao cai de 0,72 para 0,50, e a AUROC de answerability fica ate 0,19 abaixo do real. A causa recorrente sao hard negatives, gold de outro turno ou chunk vizinho da pagina gold. Codigo, runs e rotulos foram anunciados como publicos.
Por que entrou: em RAG juridico com abstencao ("nao encontrei fundamento"), avaliar recusas pela presenca de documento gold penaliza exatamente o retriever melhor e premia recusas indevidas; o paper da o protocolo alternativo (rotulo por conteudo) aplicavel a datasets de eval de jurisprudencia, onde precedentes equivalentes e chunks vizinhos sao a regra.


REVISAO ADVERSARIAL

Item 1. Fonte primaria oficial: PDF da opiniao baixado via curl do dominio coa1.azcourts.gov (HTTP 200, PDF valido, dominio oficial do Judiciario do Arizona, nao typosquat); numero do caso, data FILED 09-30-2026, composicao do painel, valores de pena e trechos citados conferidos no texto do PDF. A reportagem KJZZ (autor identificado, emissora publica) resolveu via fetch. Ponto de atencao: a decisao em si e de 2026-09-30, fora da janela de 7 dias; o item entrou pelo fato novo publicado em 2026-10-30 (recurso da acusacao a Suprema Corte do Arizona) e por nao constar de nenhuma curadoria anterior do repositorio. A informacao sobre o recurso a Suprema Corte vem apenas da KJZZ ("Prosecutors are appealing the decision for resentencing to the state Supreme Court") [nao verificado em segunda fonte; docket da Suprema Corte nao consultado]. A data de 2026-09-30 foi confirmada tambem por FOX 10 Phoenix. Sem linguagem promocional. Categoria (b) resiste: houve erro processual reconhecido e pena anulada; alternativa (c) foi considerada.

Item 2. Fonte de terceiros (Migalhas), sem decisao escrita ou numero de processo; a fala foi em sessao e circula em video (YouTube incorporado na materia, nao assistido). Confirmacao independente pelo Ambito Juridico (autor Gustavo Fonseca, 2026-10-31), que confirma o desembargador, a reacao da OAB/RS e a inexistencia de multa aplicada, mas nao reproduz o numero 30 para 70 embargos [nao verificado em segunda fonte; e declaracao do magistrado sem auditoria]. Turma, data exata da sessao e processo [nao verificado]. Ambas as URLs resolveram via fetch. Categoria (c) resiste como risco procedimental; nao ha caso concreto de sancao, por isso nao foi classificado como (b). Item mais fraco da selecao em termos de dado verificavel; mantido por ausencia de candidato brasileiro melhor na janela.

Item 3. Fonte primaria (preprint arXiv; abs e versao HTML resolveram com HTTP 200; data de submissao 29 Oct 2026 confirmada). Autor principal com afiliacao escolar (Letovo School); paper nao revisado por pares. O repositorio de codigo https://github.com/iskochergin/reteco-2026 citado no HTML respondeu 403 ao curl deste ambiente [nao verificado]; o dataset RETECO-SemEval2027 citado no HuggingFace nao foi aberto. Todos os numeros (28% a 72%, 0,68 para 0,10, 0,72 para 0,50, AUROC 0,19) vem apenas do proprio paper [nao verificado em segunda fonte]. O paper nao e especifico de dominio juridico: a ponte para RAG juridico e inferencia da curadoria, declarada no "Por que entrou". Sem linguagem promocional.

Descartes e substituicoes no adversarial: nenhum item foi descartado nesta etapa. Considerados como substitutos e rejeitados: California SB 574 (assinada em 2026-09-30, fora da janela, sem fato novo localizado); SRA v. Kumar (strike-off no SDT, decisao de agosto, ja descartado em 2026-11-01).


AUDITORIA

Escalonamento de janela: 36h (desde 2026-10-31 17:53 BRT) sem nenhum item qualificado; 72h produziu 2 (itens 1 e 2); 7 dias necessario para o terceiro (item 3, arXiv de 2026-10-29). Nivel aplicado: 7 dias.

Deduplicacao: contra curadorias/curadoria-ia-direito_2026-11-01.md e, pelo escalonamento, contra os arquivos de 2026-10-26 a 2026-11-01 (URLs e titulos). Nenhum dos itens entregues consta de curadoria anterior (busca por Horcasitas, Pelkey, TRT4, 2610.40966 sem ocorrencias).

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas RSS (HTTP 404); Above the Law tag IA (HTTP 200, mas devolveu HTML, 0 entradas). Observacoes: LawSites devolveu o mesmo conteudo do feed LawNext (duplicado); ConJur respondeu 200 com 10 itens, nenhum sobre IA; Unikowsky, Charlotin Substack e Harvard Law Review Blog sem entradas na janela de 7 dias.

Camada C: Damien Charlotin AI Hallucination Cases Database, "Last updated: 31 October 2026"; caso mais recente Clifford v. Neidle (2026-10-28), ja curado em 2026-11-01; os seguintes sao de 2026-10-23, fora da janela. Hacker News via WebSearch sem resultado na janela.

Camada B, observacao: buscas site:x.com, site:reddit.com e site:news.ycombinator.com retornaram apenas agregadores ou paginas antigas; nenhuma origem social qualificada.

Descartes no filtro deterministico (9): Everlaw Omni (anuncio de fornecedor sem auditoria independente); "At ClioCon, Legal's AI Future Is Already Here" (linguagem de futuro da advocacia, cobertura de evento de fornecedor); "ClioCon 2026: A Quick Wrap-Up" (lista de anuncios de fornecedor); "Harvey Buys Aida" (aquisicao, sem caso de uso); "Vetta Bids For Weil IP" e "Scissero Seeks Weil Gotshal Lawyers" (movimentacao societaria sem caso de uso); "Legal Innovators is Next Week!" (promocao de evento); haqq.ai "Best AI for Legal Work" (benchmark do proprio fornecedor); ailegalindex "The Brief, October 19 to 30" (agregado de alegacoes de fornecedores, sem fonte primaria).

Descartes na triagem qualitativa: itens de ConJur, JOTA e Volokh na janela sem relacao com IA (tributario, previdenciario, eleitoral, obituarios, Open Threads); JOTA "IA entra na conta da negociacao de Itaipu" e "A condicao humana da advocacia" (ja descartado em 2026-11-01 / opiniao sem dado); Artificial Lawyer "How Specialist AI Agents Support Evidence-Based Arbitrator Selection" (artigo do CEO da Jus Mundi sobre o proprio produto) e "What Real AI Adoption Looks Like" (entrevista promocional de evento, sem metrica); LawNext podcast NetDocs (entrevista com CEO); arXiv 2610.39398 (robustez de chatbots julgando acoes presidenciais, sem componente juridico processual), 2610.41682 e 2610.37875 (ensaios conceituais sem dado juridico), 2610.41090 (text-to-SQL); California SB 574 (assinada 2026-09-30, fora da janela); Law360 UK sobre SRA v. Kumar (decisao de agosto, paywall, ja descartado); TJPR multa de R$ 20 milhoes (Tribuna PR, 2026-06-29, fora da janela); STJ AREsp 3.095.458 e materias correlatas (2026-10-20 a 24, fora da janela e ja coberto); STJ "Os precedentes do STJ diante do avanco da IA" (2026-10-18, fora da janela); Migalhas 465636 (prompt oculto, anterior a janela); demais resultados WebSearch eram guias genericos, paginas de fornecedores ou materias de 2023 a meados de 2026.

Substituicoes: nenhuma.

Seguranca: nenhum conteudo coletado tentou instruir acoes desta execucao. Unica escrita realizada: este arquivo em curadorias/ e o commit correspondente.
