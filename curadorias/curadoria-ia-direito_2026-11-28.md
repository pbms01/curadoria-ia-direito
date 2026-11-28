CURADORIA DIARIA IA E DIREITO, 2026-11-28

Data de coleta: 2026-11-28 (America/Sao_Paulo), inicio por volta de 05h40
Janela aplicada: 7 dias (escalonada de 36h para 72h e depois para 7 dias; corte por data de calendario em 2026-11-21)
Buscas WebSearch executadas: 14
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 40 (11 entradas RSS com tema de IA na janela de 7 dias; 9 preprints arXiv de direito e LLM submetidos entre 21/11 e 25/11; 20 candidatos via WebSearch e fontes oficiais; 0 decisoes novas na base Charlotin dentro da janela)
Candidatos apos filtro deterministico: 34 (6 removidos: lancamentos de produto, captacao de investimento, contratacao, chamada de concurso de startups e press release PRNewswire)
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional e fonte judicial primaria 33% (noticia oficial do TJDFT) / Substack-RSS 0% / social 0% / repositorio academico (arXiv) 67%


1. Justica mantem multa por uso de precedentes inexistentes gerados por inteligencia artificial
Fonte: Tribunal de Justica do Distrito Federal e dos Territorios (TJDFT), noticia institucional | URL primaria: https://www.tjdft.jus.br/institucional/imprensa/noticias/2026/novembro/justica-mantem-multa-por-uso-de-precedentes-inexistentes-gerados-por-inteligencia-artificial
Processo: 0714843-80.2025.8.07.0001 (PJe2)
Data de publicacao: 2026-11-24
Categoria: (b) erro ou fracasso documentado
Sintese: A 5a Turma Civel do TJDFT, por unanimidade, manteve o reconhecimento de litigancia de ma-fe em acao indenizatoria movida por servidora publica contra colegas da Secretaria de Saude do DF, extinta sem resolucao de merito porque os fatos se ligavam ao exercicio das funcoes dos reus (o pedido deveria ser dirigido ao ente publico). Segundo a noticia, a replica continha mais de dez decisoes judiciais inexistentes, com numeros de processo, orgaos julgadores e entendimentos que nao foram proferidos. O colegiado afirmou que o uso de IA nao afasta o dever de conferencia do advogado, mas deslocou a multa de 3% sobre o valor atualizado da causa dos advogados para a autora, por entender que a sancao por litigancia de ma-fe recai sobre a parte e nao diretamente sobre os procuradores nos proprios autos; determinou oficio a OAB/DF. A gratuidade foi negada porque a autora havia recolhido o preparo. O inteiro teor do acordao nao foi localizado em fonte aberta [nao verificado].
Por que entrou: Caso brasileiro com decisao colegiada e numero de processo, que fixa a mecanica de responsabilizacao (multa na parte, controle disciplinar via OAB) em linha com o art. 81 do CPC, divergindo de decisoes que multam o advogado diretamente. Para quem projeta trilha de verificacao de citacoes, o volume (mais de dez precedentes falsos em uma unica replica) indica ausencia total de checagem, nao erro pontual.


2. SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?
Fonte: arXiv (cs.CR, cs.CL), preprint de Asma Farajidizaji, Vyas Raina, Vatsal Raina e Ivaxi Sheth (Spark AI Research, Apta AI e pesquisador independente) | URL primaria: https://arxiv.org/abs/2611.31791
Data de publicacao: 2026-11-24
Categoria: (c) risco novo importante (vetor de ataque)
Sintese: O dataset reune 24 cenarios sinteticos de chat em grupo entre agentes LLM (saude, direito, financas e engenharia de software; tres contextos por dominio, cada um em versao horizontal e hierarquica), nos quais atacantes se passam por colegas para levar um agente vitima, com ferramenta de consulta a registros confidenciais e politica explicita de sigilo, a publicar campos protegidos (nome, sobrenome, data de nascimento e dois campos do contexto, como numero de processo judicial). Com GLM 5.2 como atacante, sete estrategias conversacionais (urgencia, handoff de rotina, verificacao, reciprocidade, dependencia de tarefa, recomendacao direcionada, armadilha de consistencia) e orcamento de 200.000 tokens, um atacante isolado iguala ou supera um enxame de quatro em todas as vitimas; a diferenca na taxa de vazamento entre as duas configuracoes e de no maximo 14,3 pontos, enquanto trocar a vitima move a taxa de 0% a 99,4%. Quatro das cinco vitimas vazaram apesar da politica; em Nemotron 3.5 Lightning, o atacante isolado expoe 85,4% dos campos protegidos na primeira revelacao, contra 68,1% do enxame. GLM 5.2 como vitima consultou dados protegidos em 64,3% das execucoes e vazou em 0,6%. Os autores ressalvam que nomes e valores sao sinteticos e que as taxas sao provavelmente conservadoras.
Por que entrou: Escritorios e tribunais comecam a operar agentes com acesso a bases de clientes e processos em canais compartilhados; o paper mede que a politica de sigilo no prompt nao contem engenharia social conversacional e que a escolha do modelo vitima pesa mais que o tamanho do adversario, o que e um criterio objetivo de selecao de modelo para agentes com dados sob segredo profissional.


3. Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study
Fonte: arXiv (cs.LG, cs.IR), preprint de Sayed Amir Karim (Pelloran Research) | URL primaria: https://arxiv.org/abs/2611.31442
Codigo e dados: DOI https://doi.org/10.5281/zenodo.24345474 (pacote pelloran-safety-lens, AGPL-3.0)
Data de publicacao: 2026-11-23
Categoria: (d) solucao para gargalo em pipelines juridicos (retrieval e citacao verificavel)
Sintese: O trabalho mede a falha de retrievers densos diante de "armadilhas": documento quase identico ao correto, mas com edicao que inverte o sentido (must e must not, valores, partes, direcao). Com cosseno bruto sobre E5-Large-v2, a armadilha entra no top-10 em 82% a 100% das consultas num pool de 5.000 documentos. A proposta e uma projecao linear aprendida de 1.024 para 11 ou 32 dimensoes, treinada sobre um conjunto declarado de casos, que zera a presenca da armadilha no top-10 (HN@10 = 0) nos doze cenarios (quatro dominios, pools de ate 100.000) mantendo a parafrase correta em 93% a 99% dos casos, sob busca exata. No dominio juridico o conjunto tem 299 casos gerados por script em 23 tipos de inversao, com distratores extraidos do LexGLUE e lente de 11 dimensoes; uma auditoria interna encontrou 22% de duplicatas numa versao inicial do corpus juridico, que inflavam a metrica em 16 pontos. Com consulta reescrita contra corpus inalterado, a taxa de acerto cai para cerca de 0,79, com a supressao da armadilha mantida. A cobertura vale so para os casos declarados, sem garantia probabilistica; o acelerador espectral (Cell D) e componente comercial reservado.
Por que entrou: Ataca um gargalo especifico de RAG juridico: recuperar a versao errada de um dispositivo ou clausula que difere da correta por uma negacao ou um valor, falha que verificacao de existencia de citacao nao detecta. O protocolo de armadilhas e o gate de duplicatas sao reaproveitaveis como teste de regressao para indices de normas, sumulas e clausulas em portugues.


REVISAO ADVERSARIAL

Item 1 (TJDFT). Fonte primaria institucional (portal oficial tjdft.jus.br, dominio legitimo), autoria da noticia registrada apenas como "BEA" (assessoria). URL resolveu via curl (HTTP 200) e a data 24/11/2026 consta da propria pagina. Nao verificados em segunda fonte: o numero "mais de dez decisoes inexistentes", o percentual de 3% e o deslocamento da multa para a autora, pois o acordao nao foi localizado em fonte aberta e a busca pelo numero do processo nao retornou outra cobertura. Nenhuma linguagem promocional. A categoria (b) resiste: ha decisao colegiada e sancao aplicada. Ressalva de leitura: a noticia nao informa se houve confissao de uso de IA ou apenas inferencia do colegiado.

Item 2 (SwarmLeak). Fonte primaria (preprint), autores identificados com afiliacoes declaradas. URL do abstract e versao HTML resolveram via curl (HTTP 200). Nao revisado por pares. Numeros conferidos contra o abstract e o corpo do texto HTML (85,4% vs 68,1%, 64,3% vs 0,6%, 0 a 99,4%, 14,3 pontos); algumas taxas por modelo constam em notacao matematica que nao foi extraida, por isso nao foram citadas. O cenario juridico e um de quatro dominios, com dados sinteticos: o claim nao e de vazamento real em escritorio. Categoria (c) resiste como vetor de ataque mensurado; risco de sobreleitura caso se trate o resultado como especifico do direito.

Item 3 (projecoes anti-armadilha). Fonte primaria (preprint), autor unico ligado a empresa (Pelloran Research) que reserva comercialmente o acelerador: conflito de interesse declarado pela propria estrutura do trabalho. URL resolveu via curl (HTTP 200); DOI Zenodo nao foi resolvido nesta execucao [nao verificado]. Corpus juridico sintetico, gerado por script, em ingles e com distratores do LexGLUE: nao ha teste em portugues. O resultado HN@10 = 0 e restrito aos casos declarados e a busca exata, o que o proprio autor afirma. Linguagem promocional residual moderada no titulo ("Spectral Acceleration") e na secao de footprint de implantacao; a sintese manteve apenas os numeros. Na curadoria de 26/11 este preprint foi descartado por "sem corpus juridico identificado no resumo"; a leitura do texto completo mostra dominio juridico com 299 casos, o que reverte aquele descarte. Categoria (d) resiste, com a ressalva de que a solucao depende de declarar previamente os pares sensiveis.

Nenhum item de origem social. Nenhuma substituicao por URL quebrada.


AUDITORIA

Janela: 36h (desde 26/11 ~18h) retornou apenas entradas RSS sem tema de IA qualificavel e uma entrevista do ConJur ("Presidente da OAB-SP fala sobre gestao publica e IA nos Estados Unidos", sem dado verificavel). 72h (desde 25/11 ~06h) acrescentou apenas itens do Artificial Lawyer de 25/11, todos lancamentos de produto ou ja entregues. Escalonado para 7 dias (corte 21/11). Periodo coincide com o feriado de Thanksgiving nos EUA, com baixa producao nos feeds americanos.

Feeds com falha: Stanford CodeX HTTP 404; Migalhas HTTP 404; Above the Law (tag IA) HTTP 200 com 0 entradas (corpo nao reconhecido como feed). Artificial Lawyer respondeu com 0 entradas na primeira chamada e 10 na segunda, ambas HTTP 200. ConJur respondeu HTTP 200 com 10 entradas, sem necessidade de compensacao por WebSearch, embora uma busca site:conjur.com.br tenha sido executada. LawSites e LawNext retornaram o mesmo item na janela.

Base Damien Charlotin: "Last updated: 27 November 2026"; a decisao mais recente listada e de 20/11/2026 (Kavanagh v Atlassian, Garner v. Mendelsohn, Lingle v. Subaru), fora da janela de 7 dias e parcialmente ja entregue em 24/11.

Deduplicacao: arquivo de ontem (curadoria-ia-direito_2026-11-27.md) lido; pelo escalonamento, conferidos tambem os arquivos de 21/11 a 26/11. Excluidos por ja entregues ou ja auditados: arXiv 2611.29852 (GlobalHRBench, 27/11), 2611.34120 e 2611.30423 (26/11), 2611.31679 e 2611.31569 (25/11); Artificial Lawyer "A More Measured Approach to AI Fluency", "OpenAI Held Talks With AI Native Law Firm" e "Conclusive Will Review Your Legal AI Claims Slop" (25/11); suspensao de advogado pela Suprema Corte de Ohio (26/11); STJ e recurso que transcreve conversa com IA (25/11).

Descartes por filtro deterministico: Walton "Autonomous Transaction System" (lancamento de produto); Simmons & Simmons Lex-Ray (lancamento de produto); Ex-Goodwin Lawyers Raise $11m (captacao); Catherine Bamford Joins Document Drafter (contratacao); ABA TECHSHOW Startup Alley 2027 (chamada de concurso); CESA via PRNewswire (press release).

Descartes por triagem qualitativa: STF ARE 1608713 e AP 2822, prompt injection detectado pelo MARIA Shield (25/09 e 01/10/2026, fora da janela); CNJ, comite aprova medidas de seguranca de IA (28/05/2026, fora da janela); Delaware Chancery sanciona advogado por alucinacoes (Bloomberg Government, 13/11/2026, fora da janela e sem acesso ao texto integral); Law Commentary, juiz remove quatro advogados (12/11/2026, fora da janela); Bloomberg Law, advogados de patentes (16/12/2025); TJSC, multas por jurisprudencia ficticia (sem data na janela); Nota Tecnica do CNJ via TRF6 (curl sem resposta, data nao confirmada); arXiv 2611.29127, Group-Balanced SFT (relevante para fine-tuning juridico: strings de citacao absorvem 81% do peso da loss em QA juridico; preterido por ser ajuste de treinamento, menos aplicavel a pipelines RAG que o item 3; candidato reserva); arXiv 2611.28787, DiscernBench (dominios aviacao, policia e emergencia, sem cenario juridico); Artificial Lawyer "Is Going AI Native Incompatible with Big Law?" e "Right About the Law, Wrong for the Company" (opiniao sem dado verificavel); JUA, LegalBench-BR, NormasTCU e 2610.10971 (preprints de abril a outubro, fora da janela); pesquisas Wolters Kluwer e 8am sobre adocao (fora da janela, conteudo de fornecedor); paginas de ROI de Harvey e Legora (material de fornecedor). Buscas em X/Twitter, Reddit e Hacker News nao retornaram item datado na janela.

Seguranca: nenhum conteudo coletado continha instrucao dirigida ao agente.
