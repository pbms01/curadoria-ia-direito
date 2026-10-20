CURADORIA DIARIA IA E DIREITO, 2026-10-20

CABECALHO
Data de coleta: 2026-10-20 (execucao iniciada por volta de 05h50 America/Sao_Paulo)
Janela aplicada: 36h (nivel base, sem escalonamento)
Buscas WebSearch executadas: 16
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 66
Candidatos apos filtro deterministico: 14
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 1 / (d) 2
Origem das fontes: midia tradicional 0% / Substack-RSS 33% (Volokh Conspiracy via RSS, com peticoes primarias no CourtListener) / social 0% (os outros dois itens, 67%, vem de repositorio academico, arXiv, fora das tres classes)


1. "The AI Data Will Provide an Unrivaled View into the Mind of a Defendant ..." (sobre Fontainebleau Florida Hotel, LLC v. Botach, No. 1:25-cv-20251-JTK, S.D. Fla., ECF 282 e 283)
Fonte: The Volokh Conspiracy (Eugene Volokh), com as peticoes das partes no CourtListener/RECAP | URL primaria: https://storage.courtlistener.com/recap/gov.uscourts.flsd.682106/gov.uscourts.flsd.682106.283.0.pdf (memorial do autor) ; https://storage.courtlistener.com/recap/gov.uscourts.flsd.682106/gov.uscourts.flsd.682106.282.0.pdf (memorial do reu) ; post: https://reason.com/volokh/2026/10/19/the-ai-data-will-provide-an-unrivaled-view-into-the-mind-of-a-defendant/
Data de publicacao: 2026-10-19 (post); memoriais protocolados em 2026-10-12
Categoria: (c) risco novo importante
Sintese: Em acao de difamacao movida pelo hotel Fontainebleau contra Jacob Shmuel Botach (Shmuley Boteach), com discovery reaberta por 30 dias apenas para danos (ECF 261), o autor propos quatro subpoenas a provedores de IA e um Seventh Request for Production para obter os prompts e conversas do reu. A ordem de 9/10/2026 (ECF 281) pediu memoriais sobre se esse material cabe na discovery de danos. O autor (Burstyn Law, ECF 283) sustenta que os chats sao "o estado mental do reu reduzido a escrito", relevantes para afastar o teto de punitive damages do Fla. Stat. § 768.73(1)(c), que exige intencao especifica de causar dano, e cita U.S. v. Heppner (S.D.N.Y. 2026) para afirmar que conversa de nao advogado com sistema computacional nao e privilegiada. O reu (Nicklaus, Nicklaus & Associates, ECF 282) responde que o pedido excede o escopo de danos, que o autor poderia ter buscado o material na discovery geral (Rule 26(b)(2)(C)(ii)) e que prompts e analises feitos para preparar a defesa podem ser work product sob Rule 26(b)(3)(A), apoiado em Warner v. Gilbarco (E.D. Mich. 2026). Pede, subsidiariamente, categorias delimitadas por autor, conta, assunto e periodo, com resolucao das objecoes antes de qualquer producao pelo provedor. Os memoriais nao nomeiam os quatro provedores nos trechos lidos; a decisao do magistrado ainda nao foi proferida.
Por que entrou: historico de conversas com LLM tratado como fonte direta de prova de dolo, com o provedor como terceiro intimado, e a disputa sobre privilegio e work product aplicada a prompts de parte representada. E prova digital de nova natureza, com reflexo direto em preservacao, cadeia de custodia e estrategia de quem usa IA para preparar defesa.


2. Thunder-DeID+: Boundary-Aware Korean De-identification from Court Judgments to Broader Sensitive Documents
Fonte: arXiv (cs.CL), Gyuseong Lee, Gyeongje Cho, Jongmin Kim, Heejin Kim, Yeonkyoung So, Hyunggeun Jeon, Hyunji M. Park, Sangho Kim, Yoonhee Park, Youngbin Pyo e Jaejin Lee (Seoul National University, Dept. of Data Science e Dept. of Computer Science and Engineering) | URL primaria: https://arxiv.org/abs/2610.22733
Data de publicacao: 2026-10-19 (anuncio no arXiv; submissao em 2026-10-15)
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O trabalho ataca a anonimizacao de sentencas coreanas em dois pontos: tokenizacao e taxonomia. Em lingua aglutinante, tokenizadores BPE fundem o dado pessoal com a particula adjacente, o que degrada a recuperacao exata do span. Os autores propoem um tokenizador que estende o vocabulario BPE pre-treinado com componentes de n-gramas e pontuacao de fronteira, e uma taxonomia de PII em tres niveis refinada para textos juridicos. O corpus tem 5.872 decisoes e 193.004 spans anotados; os anotadores revisaram as decisoes ja publicadas pelos tribunais com mascaras ("○○", "A") e marcaram mais spans a desidentificar segundo a Regulation No. 2809 da Suprema Corte coreana, e esses spans novos foram 15,01% das anotacoes finais. Com o novo tokenizador, o W. Strict Typed F1 em decisoes completas sobe de 0,76 a 0,77 para 0,87 a 0,88 nos quatro tamanhos de modelo (150M, 395M, 750M e 1B), ganho atribuido sobretudo a precisao, nao a escala. Com fine-tuning em 1.000 documentos sensiveis de outros dominios, o modelo treinado em sentencas chega a 0,93.
Por que entrou: NER juridico e anonimizacao de decisoes sao gargalo real de publicacao e de construcao de corpus, e o dado de 15,01% de spans perdidos em decisoes ja anonimizadas pelos tribunais mede o vazamento residual da anonimizacao oficial. O problema de fronteira token/entidade tem analogo em portugues (cliticos, contracoes, nomes compostos), embora o paper nao teste outra lingua.


3. Beyond Recall Saturation: Scaling Hard-Negative Reranker Training for Industrial Legal Retrieval
Fonte: arXiv (cs.CL), Yunhan Li, Mingjie Xie, Zeyang Shi, Gengshen Wu e Min Yang (Deli Joint Laboratory Shenzhen; City University of Macau) | URL primaria: https://arxiv.org/abs/2610.24478
Data de publicacao: 2026-10-20 (anuncio no arXiv; submissao em 2026-10-17)
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: Os autores mostram que, em benchmarks chineses de recuperacao juridica, o recall do embedding satura em torno do top-300 de candidatos: ampliar o pool rende pouco, e a perda passa a estar na ordenacao, com evidencia relevante caindo abaixo do corte de saida. O protocolo isola o reranker (embedding top-300, reranking para top-30, metricas MRR, NDCG@30 e Recall@k) e compara estrategias de hard negatives: minerados pelo embedding, auto-minerados pelo proprio reranker e variantes dinamicas por epoca e online, sobre a familia Qwen3 de embedding e reranking. A sequencia embedding-minerado seguida de auto-minerado deu o melhor equilibrio; estagios dinamicos adicionais nao melhoraram todas as metricas held-out. O pipeline escala de 0,6B para 4B, e o reranker 4B treinado supera o 4B nativo nos benchmarks STARD e CSAID e num conjunto interno, sendo preferido em 72,4% das comparacoes nao empatadas sobre 410 consultas operacionais desidentificadas, em avaliacao offline com juiz LLM. Codigo declarado no GitHub.
Por que entrou: em RAG juridico com pool grande de candidatos, o artigo indica onde investir (treino do reranker com negativos dificeis) e onde parar (aumentar top-k do embedding), com protocolo que separa as duas etapas na avaliacao. Isso responde a uma pergunta recorrente de quem dimensiona pipelines de jurisprudencia.


REVISAO ADVERSARIAL

Item 1. Fonte primaria: sim, os dois memoriais (ECF 282, 11 paginas; ECF 283, 12 paginas) baixados do CourtListener/RECAP (HTTP 200) e lidos por pdftotext; conferidos numero do caso, data de protocolo (10/12/2026), escopo da ECF 261, ordem de 9/10 (ECF 281), audiencia de 8/10, os quatro subpoenas, o § 768.73(1)(c) e os argumentos de work product. Autor do post identificado (Eugene Volokh, conta com historico longo). Dominios: reason.com e storage.courtlistener.com, oficiais. Nao verificados em segunda fonte: as citacoes U.S. v. Heppner, 820 F. Supp. 3d 292 (S.D.N.Y. 2026), e Warner v. Gilbarco, Inc., 820 F. Supp. 3d 629 (E.D. Mich. 2026), aparecem apenas como invocadas pelas partes [nao verificado]; quais provedores sao alvo dos subpoenas [nao verificado]; a referencia a magistrada Marty Fulgueira Elfenbein vem so do post e foi omitida da sintese. A pagina de docket do CourtListener devolveu 403 ao curl; os PDFs resolveram. Linguagem promocional: a frase "most potent technologies known to humankind" e retorica do autor da acao, nao reproduzida como fato. Sobreposicao tematica com o item de 2026-10-17 (Villanueva v. LVMPD, historico de IA de perito), mas fato, partes e questao juridica distintos. Categoria (c) resiste; nao ha decisao, so disputa pendente.

Item 2. Fonte primaria: sim, abstract e versao HTML do arXiv (HTTP 200); conferidos afiliacoes (snu.ac.kr), 5.872 documentos, 193.004 spans, 15,01%, faixas de F1 e a regra da Suprema Corte. Preprint sem revisao por pares declarada. Nao verificados em segunda fonte: todos os numeros sao autorreportados; a Judicial Rule No. 1778 citada junto da Regulation No. 2809 nao foi conferida [nao verificado]. A extrapolacao para o portugues esta marcada como nao testada no texto. Linguagem promocional: nenhuma. Categoria (d) resiste; poderia ler-se como (c) pelo vazamento residual medido, mantida em (d) porque a contribuicao central e o metodo.

Item 3. Fonte primaria: sim, abstract e HTML do arXiv (HTTP 200); conferidos afiliacoes, protocolo top-300/top-30, base Qwen3, escala 0,6B a 4B, 72,4% e 410 consultas. O repositorio https://github.com/lyxx3rd/beyond-recall-saturation devolveu 403 pelo proxy desta execucao [nao verificado]. Nao verificados em segunda fonte: os ganhos por metrica em STARD e CSAID nao foram extraidos das tabelas e por isso nao sao citados; a avaliacao de preferencia usa juiz LLM sobre conjunto interno nao publico e e autorreportada. Linguagem promocional: o termo "industrial" no titulo descreve o cenario, sem claim de mercado. Categoria (d) resiste.

Origem social: nenhum item entregue tem origem em rede social. Descartes e substituicoes nesta etapa: nenhum item descartado; todas as URLs primarias resolveram.


AUDITORIA

Janela: 36h atingiu 3 itens qualificados, sem escalonamento. Os dois papers do arXiv foram submetidos antes da janela (15/10 e 17/10), mas anunciados publicamente em 19/10 e 20/10, datas usadas como publicacao, criterio mantido das curadorias anteriores.

Feeds que falharam: Stanford CodeX (HTTP 404, corpo HTML, 0 entradas); Migalhas (HTTP 404, 0 entradas); Above the Law tag IA (HTTP 200, feed vazio, 0 entradas). ConJur respondeu HTTP 200 nesta execucao, sem desafio Cloudflare. Feeds sem itens na janela: 3 Geeks, Damien Charlotin Substack, Adam Unikowsky, Harvard Law Review Blog.

Contagem: 56 entradas de RSS na janela (Artificial Lawyer 6, ConJur 10, JOTA 25, LawNext 2, LawSites 2 duplicadas da LawNext, Volokh 11), mais 4 papers juridicos do arXiv cs.CL anunciados em 19 e 20/10 e 6 candidatos de busca e agregadores. Filtro: 44 entradas fora do tema IA e Direito (JOTA 25, ConJur 9, Volokh 10) e 8 pelo filtro anti-hype.

Descartes no filtro deterministico: Artificial Lawyer "Webinar: The Future of Contract Management + ACM Demo" (demo de fornecedor); Artificial Lawyer "Harvey Webinar, Agents in Legal: A Practical Guide" (conteudo de fornecedor); LawNext/LawSites "Harvey Now Connects to Legal Research Platform Midpage Through An MCP Connector" e Artificial Lawyer "Legal Research Challenger Midpage Channels Data Into Harvey" (integracao comercial sem resultado medido); LawNext/LawSites "New MCP Makes Tax Research from Blue J Available from within Legora" e Artificial Lawyer "Legora Does Tax Data Deal With Blue J" (idem).

Descartes na triagem qualitativa: Artificial Lawyer "What Happens When Lawyers Can Afford to Look Further?" e "Big Law's Greatest Gifts" (opiniao sem dado verificavel); ConJur "Uso de IA no Judiciario exige e lealdade deve preservar lado autoral" (artigo de opiniao de Marcos Pereira, retoma caso do TSE de fev/2025); Migalhas "Gol com a mao: Ministro alerta sobre IA e TST multa por precedentes inventados" (SDI-1 do TST, multa de 10% e envio a OAB e a comissao sobre prompt injection; bom item (b), mas publicado em 16/10 as 17h57, fora da janela de 36h, e a janela nao precisou ser ampliada); Damien Charlotin database, "Last updated: 19 October 2026", 2.202 casos, casos mais recentes Waushara County v. Bruning (15/10, pro se, advertencia) e Sabatini v. Pennsylvania PUC (14/10, pro se), fora da janela e de baixo impacto; arXiv 2610.25159 "Legal Guidance in the Wild" (JURIX 2026; taxonomia de 2.122 conversas WildChat, preterido pelos dois papers de pipeline); arXiv 2610.26241 "Machina Pauliana" (neuro-simbolico sobre actio pauliana holandesa, escopo estreito); arXiv 2610.10971 "When Citations Mislead?" (anunciado antes da janela); NY Daily Record "AI hallucinations may add risk to serving as local counsel" (16/10, fora da janela e ja excluido em 2026-10-17); Bloomberg Government "Ninth Circuit Warns of AI Hallucinated Briefs in Sanctions Order" (sem data confirmada e paywall).

Deduplicacao: curadorias/curadoria-ia-direito_2026-10-19.md lido no clone, junto com 2026-10-13 a 2026-10-18 para titulos. Nenhuma colisao de URL ou titulo (jaccard > 0,8) entre os itens entregues.

Busca social: consultas site:x.com/twitter.com e site:reddit.com e site:news.ycombinator.com nao retornaram posts datados na janela; nenhum candidato de origem social.

Seguranca: nenhum conteudo coletado tentou instruir acoes. Substituicoes: nenhuma.
