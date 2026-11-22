CURADORIA DIARIA IA E DIREITO, 2026-11-22

Data de coleta: 2026-11-22 (America/Sao_Paulo), inicio por volta de 05h50
Janela aplicada: 7 dias (escalonada a partir de 36h, depois 72h)
Buscas WebSearch executadas: 19
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 92 (65 entradas RSS unicas na janela de 7 dias, apos remover 17 duplicatas LawSites/LawNext; 12 papers juridicos na listagem arXiv; 14 resultados de WebSearch com data e tema pertinentes; 1 consulta a base Charlotin)
Candidatos apos filtro deterministico: 83
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional e fontes institucionais/academicas 100% (comunicado oficial da CEDH, 2 preprints arXiv) / Substack-RSS 0% / social 0%


1. Romanian lawyer barred for two years from representing applicants before the European Court of Human Rights over unverified AI-generated citations
Fonte: Corte Europeia de Direitos Humanos, comunicado do Registrar ECHR 290 (2026) | URL primaria: https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations
Fonte secundaria: https://www.irishlegal.com/articles/ecthr-bars-romanian-lawyer-for-two-years-over-ai-generated-citations (Irish Legal News, 19/11/2026)
Data de publicacao: 2026-11-18
Categoria: (b) erro ou fracasso documentado
Sintese: Em 13/11/2026, o Presidente da CEDH, acolhendo proposta fundamentada de uma Camara, excluiu por dois anos, com base na Rule 44D §§ 1 e 2 do Regimento, uma advogada romena de representar ou assistir partes perante a Corte. As observacoes que ela apresentou continham casos inexistentes, paragrafos ficticios atribuidos a julgados reais e precedentes reais irrelevantes ou contrarios a tese defendida. Ela admitiu ter usado ferramentas de IA e chamou os erros de "inaccuracies" e "citation errors". A Camara qualificou a conduta como padrao de erros repetidos e substantivos, afirmou que parte das referencias nao passou por checagem alguma e que muitos erros seriam detectaveis por "cursory check of HUDOC". Antes da decisao, foram ouvidos a advogada, o Governo romeno e a Ordem Nacional dos Advogados da Romenia; a Ordem de Iasi foi convidada e nao se manifestou. A Camara registrou prejuizo a administracao da justica (tempo de verificacao, instauracao do procedimento, correspondencia com terceiros). A exclusao atinge apenas uma das duas representantes no caso e pode ser revista pela Rule 44D § 3. O comunicado nao identifica a advogada nem o numero da demanda.
Por que entrou: Sancao de exclusao de representacao por alucinacao de IA aplicada por tribunal internacional de direitos humanos e anunciada em comunicado oficial; o criterio usado (padrao repetido mais ausencia de checagem contra a base oficial HUDOC) e operacionalizavel como regra de verificacao em pipeline. A sancao recai sobre o direito de postular perante a Corte, nao sobre multa, o que muda o calculo de risco para quem litiga em Estrasburgo.


2. HireWatch: Evaluating LLM Compliance with U.S. Employment Law Under Contextual Pressure
Fonte: arXiv (cs.CL), Huy Nghiem, Maria Kostylew, Noam Kolt | URL primaria: https://arxiv.org/abs/2611.24970
Data de publicacao: 2026-11-16
Categoria: (c) risco novo importante
Sintese: O benchmark pede a 18 LLMs (GPT-4o-mini a GPT-5.4, Haiku 3.5 a Opus 4.7, Gemini 2.5 e 3, Llama, Qwen, DeepSeek, Mistral) que escolham 25 perguntas de entrevista de emprego em um banco de 200 itens, sendo 50 ilicitas pela legislacao federal norte-americana de emprego e antidiscriminacao. A classificacao foi auditada por nove advogados licenciados nos EUA (concordancia de 97,7% nos itens licitos e 86,7% nos ilicitos). Em cerca de 100.000 trials, a metrica e a Illegal Selection Rate (ISR). Contexto ocupacional (cargo, funcoes, requisito) mantem a ISR baixa; memorandos organizacionais (gerente, diretoria, politica interna, seguradora) elevam a ISR de forma significativa, com os modelos menos aderentes acima de 40% nos niveis de politica e seguro. O Gemini 2.5 Pro sai de 0,0% para 63,4% sob memorando de politica interna. Instrucao explicita de cumprir a lei reduz a ISR mediana em 10,59 pontos percentuais nesse nivel, mas nao elimina violacoes; anexar o texto legal integral acrescenta pouco. Profissionais de RH humanos vao de 1,20% para 11,63% sob a mesma pressao; 9 dos 18 modelos ficam acima desse patamar. Codigo e dados declarados publicos em repositorio GitHub [nao verificado].
Por que entrou: Mede, com rotulagem por advogados e controle humano, um vetor de falha que nao depende de ataque: contexto organizacional ordinario (um memorando interno) desloca o modelo para condutas ilicitas. O achado de que o texto legal no prompt pouco ajuda contraria a premissa de muitos pipelines RAG de compliance de que injetar a norma basta.


3. Modeling Document and Section Hierarchies in Embedding Space
Fonte: arXiv (cs.CL), Kriste Krstovski, Sharyn O'Halloran, Kshitij Chandna | URL primaria: https://arxiv.org/abs/2611.21980
Data de publicacao: 2026-11-16
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O paper propoe o Hierarchical Embedded Topic Model (hETM), que acopla a distribuicao de topicos do documento a de cada secao por meio de prior hierarquica gaussiana no espaco de embeddings, com inferencia variacional amortizada. A motivacao declarada e juridica: leis e projetos se dividem em secoes e contratos em clausulas, e uma secao trata de um tema mas tem sentido dependente do diploma em que esta inserida. A avaliacao usa quatro corpora, dois juridicos (U.S. Trade Statutes e EUR-Lex), um financeiro (relatorios anuais Edgar) e 20 Newsgroups. O hETM atinge a menor perplexidade held-out em todas as configuracoes no U.S. Trade Statutes e a melhor clusterizacao (ARI) em U.S. Trade Statutes e Edgar; no EUR-Lex fica competitivo, mas o SawETM vence em ARI. Foram testados embeddings pre-treinados (LegalBERT, InCaseLawBERT, FinBERT, ModernBERT) e embeddings aprendidos: o LegalBERT-base vence so no EUR-Lex, o maior corpus; nos demais, embeddings aprendidos superam os pre-treinados.
Por que entrou: Ataca diretamente o problema de representar peca ou diploma longo sem perder o vinculo entre trecho e documento, que e o gargalo de chunking em RAG juridico. O resultado de que embeddings de dominio so ganham em corpus grande e com vocabulario sobreposto e diretamente aplicavel a decisao de usar ou nao modelos juridicos pre-treinados em portugues com corpus pequeno.


REVISAO ADVERSARIAL

Item 1. Fonte primaria institucional (comunicado do Registrar, pagina em echr.coe.int com HTTP 200 e PDF no HUDOC, id 003-8699897-12417749, HTTP 200, texto conferido). Dominio oficial do Conselho da Europa, sem typosquat. Autoria: Registry da Corte; o proprio comunicado declara que nao vincula a Corte, de modo que a decisao de exclusao em si nao foi lida. Nao verificados em segunda fonte independente do comunicado: identidade da advogada, numero da demanda, quais ferramentas de IA foram usadas e quantos erros havia (o comunicado diz apenas "numerous"). A Irish Legal News (19/11) reproduz os mesmos fatos sem acrescentar dado. Linguagem promocional: nenhuma. Categoria (b) resiste. Ponto de atencao: o fato e de 13/11 e o comunicado de 18/11, por isso so entra com janela de 7 dias; foi registrado como candidato fora da janela na curadoria de 19/11 e nao entregue em nenhum arquivo anterior.

Item 2. Fonte primaria (preprint arXiv, pagina abs e HTML v1 com HTTP 200, submissao em 16/11/2026). Autores identificados; afiliacoes nao conferidas. Preprint sem revisao por pares. Numeros extraidos do HTML do paper (97,7%, 86,7%, 41,7% para GPT-4o-mini sob memorando de seguradora, 63,4% Gemini 2.5 Pro, 10,59 pp, 1,20% e 11,63% humanos), sem segunda fonte. O repositorio GitHub citado no resumo devolveu HTTP 403 pelo proxy desta execucao, portanto disponibilidade de codigo e dados nao confirmada. Os nomes de modelos reportados pelos autores nao foram conferidos. Categoria (c) resiste: risco com dado, nao opiniao. Limite: escopo restrito a selecao de perguntas de entrevista sob direito norte-americano, generalizacao para outras tarefas juridicas nao demonstrada.

Item 3. Fonte primaria (preprint arXiv, pagina abs e HTML v1 com HTTP 200, submissao em 16/11/2026). Autores identificados; afiliacoes nao conferidas. Preprint sem revisao por pares. Resultados conferidos no HTML (tabela de ARI e tabela 5 de embeddings vencedores), sem segunda fonte. Categoria (d) resiste parcialmente: o trabalho e de topic modeling, nao de retrieval, e nao mede impacto em recall de RAG; a aplicacao a chunking e inferencia do curador, sinalizada como tal no "Por que entrou". Linguagem promocional: nenhuma. Mantido por falta de candidato (d) mais forte na janela.

Nenhum item de origem social. Nenhuma substituicao foi necessaria apos o adversarial.


AUDITORIA

Janela: 36h (desde aproximadamente 05h50 de 20/11) sem nenhum item qualificado: as 35 entradas RSS da janela vinham de ConJur, JOTA e Volokh sem tema de IA (salvo as excecoes abaixo) e Artificial Authority "AI & Law Stuff" ja entregue em 21/11. Escalado para 72h: os candidatos de IA restantes (LawNext ROSS/Clio, Litera) ja haviam sido descartados em 20/11 e 21/11, e o comunicado da CEDH (18/11) ficava fora do limite de 72h. Escalado para 7 dias, nivel em que 3 itens qualificaram. Parada no nivel de 7 dias.

Deduplicacao: arquivo de ontem (curadoria-ia-direito_2026-11-21.md) lido; URLs e titulos extraidos (Spanish Fort/FOX10, Artificial Authority, OAB-RJ/Startups). Com o escalonamento, conferidos os arquivos de 15/11 a 21/11 por titulo e por busca textual (Romanian, 44D, HireWatch, hETM, AULA, TUSI, GPBam, Docket Minutes, Arraignment, AAA, Aderant, MinuteBox, iManage, Baker McKenzie, Penn Law, Delaware). Excluidos como ja entregues: OpenAI Astra for Law (19/11), Penn Law "Can AI Ace Your Exam?" (20/11), Fox10 Spanish Fort (21/11), Artificial Authority (21/11), TUSI-Bench (18/11), Docket Minutes e Arraignment to Resolution (19/11), AULA (20/11), Dutch rhetorical segmentation e SG-LegalClarify (17/11).

Feeds que falharam: Stanford CodeX (HTTP 404); Above the Law tag IA (HTTP 200, mas pagina HTML em vez de RSS, 0 entradas); Migalhas (HTTP 404). ConJur respondeu HTTP 200 nesta execucao (10 entradas). LawSites e LawNext servem o mesmo conteudo (100 entradas cada, sobreposicao integral na janela). Charlotin Substack, Unikowsky, 3 Geeks, Harvard Law Review Blog e Artificial Lawyer sem entradas na janela de 36h.

Camada C: base Charlotin (https://www.damiencharlotin.com/hallucinations/, HTTP 200) com "Last updated: 20 November 2026" e 2.313 decisoes no total (102 no 4o trimestre de 2026 ate a atualizacao); a lista de casos e carregada dinamicamente e nao foi possivel isolar entradas por data via curl. Hacker News: busca sem itens na janela. Buscas de X/Twitter e Reddit nao retornaram itens datados na janela.

Descartes no filtro deterministico: Legora, nomeacao de CLO e acordo global com BDO (comunicados da propria empresa, 19/11); Harvey, integracao com DeepJudge (post da fornecedora sem auditoria, 19/11); LawNext "Exclusive: MinuteBox Launches AI Agent" (lancamento de produto, 16/11); LawNext "How It Works: iManage" (demo de fornecedor, 17/11); LawNext Aderant Milana (metrica autodeclarada, 16/11); LawNext Litera (metricas autodeclaradas, 19/11); Artificial Lawyer "How a Matter Is Staffed Decides AI's Commercial Value" (artigo de executivo da BigHand, 18/11); FourWeekMBA sobre a CEDH (agregador sem autoria identificavel).

Descartes na triagem qualitativa: JOTA "Duas horas para agir: o que ja vale para proteger mulheres da violencia digital" (21/11; violencia digital sem componente de IA verificavel no trecho acessivel, corpo atras de paywall); JOTA "Uma analise sobre o artigo 'Services: The New Software'" (21/11; ensaio sem dado verificavel); LawNext "As ROSS Seeks to Come Back from the Dead, Clio Sues..." (19/11; disputa contratual de licenca de feed, ja avaliada e descartada em 20/11); LawNext AAA AI arbitrator (17/11; ja avaliado em 18/11 a 20/11); STF, multa por prompt oculto na AP 2822 (01/10/2026) e deteccao pela Maria Shield no ARE 1608713 (25/09/2026), fora da janela e tema ja coberto no repositorio; Migalhas "O STJ e a nulidade de decisoes judiciais por uso de IA" (03/11/2026, fora da janela); NY Daily Record "Your expert used AI. Now what?" (20/11; HTTP 403 Cloudflare, conteudo nao verificavel); Bloomberg Government, sancao no Delaware Chancery (data nao confirmada e paywall); Law360 "How Well Can AI Predict Supreme Court Decisions?" (paywall, data nao confirmada); arXiv "Law at the Speed of AI" (AULA, ja entregue em 20/11); arXiv "General progress substitutes for specific training data" e "MemMend" (18/11 e 19/11, nao juridicos).

Substituicoes: nenhuma.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
