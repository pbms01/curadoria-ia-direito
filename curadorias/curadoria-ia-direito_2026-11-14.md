CURADORIA DIARIA IA E DIREITO, 2026-11-14

CABECALHO
Data de coleta: 2026-11-14 (America/Sao_Paulo), inicio por volta de 05h50
Janela aplicada: 72h (escalonada a partir de 36h; ver AUDITORIA)
Buscas WebSearch executadas: 23
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 76
Candidatos apos filtro deterministico: 70
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 2 / (d) 0
Origem das fontes: midia tradicional 33% (g1) / Substack-RSS 67% (Artificial Authority, Substack de Damien Charlotin; blog E-Discovery LLC como sinalizador da decisao judicial) / social 0%


1. Gillespie v. Superior Court (People), D088222 (Court of Appeal of California, Fourth Appellate District, Division One), Opinion, not to be published in the Official Reports

Fonte: Court of Appeal of California, 4th District, Div. One (relator Justice Do; acompanharam McConnell, P. J., e Rubin, J.) | URL primaria: https://www.courts.ca.gov/opinions/nonpub/D088222.PDF

Fonte de sinalizacao (blog, nao social): Michael D. Berman, E-Discovery LLC, "Even With an Error, Expert's 'Troubling' Use of AI as a 'Thought Partner' Did Not Undermine Expert Opinion": https://www.ediscoveryllc.com/even-with-an-error-experts-troubling-use-of-ai-as-a-thought-partner-did-not-undermine-expert-opinion/

Data de publicacao: 2026-11-04 (decisao); 2026-11-11 (primeira analise localizada)

Categoria: (b) erro ou fracasso documentado

Sintese: Em processo por grand theft (Super. Ct. No. SCD307508, San Diego), a re pediu pretrial mental health diversion (Penal Code, secao 1001.36). Para afastar o nexo causal, a acusacao usou laudo da psicologa forense Nicole Friedman, que declarou no proprio laudo: "AI was used to help organize timeline and symptoms and/or behaviors to demonstrate the nexus". Em audiencia, Friedman disse usar ChatGPT sob business associate agreement, como "thought partner", inclusive para questoes juridicas do Penal Code, e admitiu ter perguntado ao modelo "What would be, maybe, considered nexus or causal effect"; nao apresentou os prompts porque apaga "everything" apos o uso. O laudo continha erro factual (afirmava "[n]o documentation" de internacao psiquiatrica previa), que ela atribuiu a omissao nas notas fornecidas ao ChatGPT. Perito da defesa rodou detector de IA e afirmou que a secao de nexo era "98 percent AI". A defesa sustentou que o uso de IA configurava novel scientific technique sujeita ao teste Kelly/Frye. A Corte de Apelacao afirmou, em tese, que o uso de IA por psicologo forense para gerar a opiniao pericial "at present, would constitute a novel scientific technique" e exigiria fundamento de confiabilidade, qualificou a prova de dependencia como "troubling", mas deferiu a avaliacao de credibilidade do juizo de origem (uso apenas organizacional) e negou o writ of mandate.

Por que entrou: Caso concreto, com decisao de tribunal, de laudo pericial redigido com assistencia de LLM, erro factual identificado em cross-examination e ausencia de trilha de prompts. Fixa em tese o enquadramento Kelly/Frye para opiniao pericial gerada por IA e mostra que, sem log, a controversia se resolve por credibilidade do perito, o que e diretamente relevante para cadeia de custodia e auditabilidade de prova tecnica assistida por IA.


2. Juiz do CNJ alerta para risco de agentes de IA serem manipulados para vazar dados da Justica

Fonte: g1 (Camila da Silva) | URL primaria: https://g1.globo.com/politica/noticia/2026/11/14/cnj-ia-risco-vazamento-dados.ghtml

Data de publicacao: 2026-11-14

Categoria: (c) risco novo importante

Sintese: O juiz federal George Marmelstein, integrante do Comite Nacional de Inteligencia Artificial do Judiciario (CNJ) e secretario-geral da Enfam, descreve a passagem do prompt injection documental para agentes com permissao de execucao: um agente encarregado de organizar pecas pode encontrar instrucao oculta (texto branco, fonte minima, codigo embutido) e, por exemplo, remeter lista de processos sob segredo de justica a endereco externo ou executar codigo que capture credenciais, sem aprovacao humana por etapa. Segundo ele, "o CNJ esta percebendo algum tipo de vulnerabilidade dos sistemas da Justica por conta dos agentes de IA", mas nao conhece casos comprovados desse ataque na Justica brasileira. A materia retoma os 83 episodios de comandos ocultos levantados pelo Fantastico (01/11), com multas de R$ 5 mil, R$ 20 mil e 10% do valor da causa no STF e no STJ, e cita balanco do ministro Luis Felipe Salomao (evento de 11/11): quase 6 milhoes de pecas varridas pelo STJ, 116 casos suspeitos, 40 confirmados apos revisao humana, cerca de 1 a cada 150.000 pecas. Registra ainda o PROSEG-IA, aprovado em maio pelo Comite, e dados de pesquisa CNJ de 2024 (178 projetos de IA; 45,8% dos orgaos usando IA generativa; 83% dos servidores nao informam o uso).

Por que entrou: Primeira manifestacao localizada de membro do comite de IA do CNJ tratando explicitamente o vetor agentico (injecao indireta com acao, nao apenas com texto) como risco de exfiltracao de dados sigilosos, acompanhada de taxa empirica de deteccao de comandos ocultos no STJ (40 confirmados em cerca de 6 milhoes de pecas). Relevante para quem desenha pipelines de ingestao de pecas com ferramentas e permissoes.


3. Writing for AI: The struggle to become an authority

Fonte: Artificial Authority (Substack de Damien Charlotin, autor do AI Hallucination Cases Database) | URL primaria: https://artificialauthority.ai/p/writing-for-ai

Data de publicacao: 2026-11-13

Categoria: (c) risco novo importante

Sintese: Charlotin argumenta que, com LLMs virando a interface principal de acesso a informacao (inclusive pesquisa juridica), autores, advogados, arbitros e juizes passarao a escrever para serem recuperados e absorvidos por modelos, e que Generative Engine Optimisation (GEO) se confunde com escrita adversarial contra IA, tema de seu texto anterior "Beware Adversarial Inputs". Ampara-se em: estudo do Reuters Institute (Digital News Report 2026) segundo o qual 10% das pessoas usam chatbots para noticias semanalmente; estudo Pew sobre menor clique em links quando ha resumo de IA no Google; arXiv 2604.25707 (Zhang et al., distincao entre selecao e absorcao de citacoes em plataformas de busca com IA, com paginas mais longas, estruturadas e ricas em definicoes e numeros tendo maior influencia); e arXiv 2506.11097 (C-SEO Bench, ganhos de SEO conversacional limitados e de soma zero). Anuncia que testa empiricamente se a amplitude de citacoes em pecas e decisoes diminuiu, hipotese ligada a tendencia de LLMs citarem as mesmas fontes e esticarem precedentes.

Por que entrou: Identifica vetor de risco ainda pouco tratado em RAG juridico: manipulacao da camada de recuperacao por conteudo otimizado para absorcao, com efeito de concentracao de autoridade (Matthew effect) na jurisprudencia e doutrina recuperadas. Complementa o item 2 pelo lado da fonte: o mesmo problema de distinguir conteudo de instrucao aparece aqui como distinguir relevancia de otimizacao.


REVISAO ADVERSARIAL

Item 1 (Gillespie). Fonte primaria: sim, PDF oficial da decisao (26 paginas, cabecalho "Filed 11/4/26 Gillespie v. Superior Court CA4/1"), obtido via curl em www.courts.ca.gov (redirecionado para www4.courts.ca.gov, HTTP 200, application/pdf, sha256 a84e7c3b783a5e42279e2bbb9b600390ec3df2764c8b38d5eabd0ee737cadd1e), lido via pdftotext. Localizado tambem na listagem oficial de opinioes nao publicadas (pagina 4, D088222, "filed 11/4/26"). Dominio oficial do Judiciario da California, nao typosquat. Autores identificados (relator e turma). Trechos citados na sintese conferidos no texto da decisao ("thought partner", "98 percent AI", Kelly/Frye, "troubling", "The petition for writ of mandate is denied"). Limitacao: decisao nao publicada, sem forca de precedente (California Rules of Court, rule 8.1115(a)). Nao verificado em segunda fonte: a confiabilidade do detector de IA usado pelo perito da defesa (ferramenta nao identificada no trecho lido) [nao verificado]; o resultado "98 percent AI" e alegacao da parte, nao achado do tribunal. A citacao Westlaw "2026 WL 3333170" aparece apenas no blog [nao verificado]. Linguagem promocional: nenhuma. Categoria: resiste como (b), por haver erro factual documentado em laudo produzido com assistencia de LLM e examinado em decisao; o componente (c) (enquadramento Kelly/Frye) e secundario.

Item 2 (g1/CNJ). Fonte: midia tradicional, materia assinada (Camila da Silva), datePublished 2026-11-14T00:00-03:00, HTTP 200 via curl. Dominio oficial g1.globo.com. Replicada por SpaceMoney e Sem Pauta, que citam o g1, portanto nao sao segunda fonte independente. Segunda fonte para o PROSEG-IA: nota oficial do CNJ de 28/05/2026 (www.cnj.jus.br, HTTP 200), que confirma a aprovacao do programa e da Manifestacao Tecnica CNIAJ 1/2026 em 27/05. Nao verificados em segunda fonte: os numeros de Salomao (quase 6 milhoes de pecas, 116 suspeitos, 40 confirmados) [nao verificado]; os 83 episodios do Fantastico e os valores das multas, nesta execucao [nao verificado]; os percentuais da pesquisa CNJ 2024 (incluindo o dado de uso de ChatGPT por 96% dos magistrados, cuja base amostral nao e explicitada na materia) [nao verificado]. A frase sobre vulnerabilidade percebida e declaracao, nao incidente documentado; o proprio entrevistado diz nao conhecer caso comprovado. Linguagem promocional: nenhuma. Categoria (c) resiste.

Item 3 (Charlotin). Fonte: Substack com autor identificado e historico publico (pesquisador, mantenedor da base de casos de alucinacao), datePublished 2026-11-13, HTTP 200 via curl. Formato ensaio: e o item mais fraco do dia, com tese majoritariamente argumentativa. Referencias conferidas: arXiv 2604.25707 e 2506.11097 resolvem pela API do arXiv com titulos e autores compativeis com o descrito. Nao verificados em segunda fonte: o percentual de 10% do Reuters Institute e o achado Pew (links presentes, paginas nao abertas nesta execucao) [nao verificado]; o estudo sobre estreitamento de citacoes esta em andamento e sem dados publicados [nao verificado]. Linguagem promocional residual: autopromocao leve (convite para estar "in the weights"), sem impacto factual. Categoria (c) resiste com ressalva: e risco emergente com base empirica indireta, nao incidente.

Descartes e substituicoes no adversarial: nenhum item descartado nesta etapa. Considerado como substituto do item 3 e rejeitado: California SB 574 via PYMNTS (12/11), lei assinada em 30/09 e ja rejeitada em 2026-11-02 por falta de fato novo; a materia de 12/11 nao traz fato novo.


AUDITORIA

Nivel de janela: em 36h (corte 12/11 por volta de 17h50 local) qualificaram apenas o item 2 (g1, 14/11) e o item 3 (Charlotin, 13/11). Escalonado para 72h (corte 11/11 por volta de 05h50 local), entrou o item 1. Criterio de janela aplicado ao item 1: a decisao e de 04/11, mas a primeira cobertura publica localizada e o post de Michael Berman de 11/11 09h53 UTC (dentro do corte de 72h por cerca de uma hora), seguido de republicacao no EDRM; diferente de Withers v. City of Aberdeen (descartado em 06/11, 07/11, 08/11 e 10/11), que teve cobertura original em junho. Registro para eventual revisao do criterio pelo destinatario.

Feeds que falharam: Stanford CodeX, HTTP 404; Migalhas, HTTP 404; Above the Law tag IA, HTTP 200 com 0 entradas parseadas. ConJur respondeu HTTP 200 com 10 entradas (sem desafio Cloudflare nesta execucao); ainda assim foi feita busca site:conjur.com.br, sem resultado na janela. LawSites devolveu o mesmo conteudo do LawNext. Tentativas complementares: RSS do CNJ (HTTP 200, 0 entradas), TST (HTTP 202, 0 entradas), Migalhas quentes/ultimas (HTTP 404); feed do STF com 10 entradas, nenhuma sobre IA na janela.

Camada C: base de Damien Charlotin com "Last updated: 12 November 2026", 2.292 decisoes; caso mais recente datado de 08/11/2026 (Adia Doiakh v. Metkanei Psagotim, Tribunal Regional do Trabalho de Tel Aviv), fora da janela de 72h e sem sancao. Salgado v. Fred Palla Farms (06/11) ja entregue em 2026-11-09. Hacker News: busca sem item na janela. API do arXiv (HTTP 200): nenhum preprint juridico submetido nas ultimas 36h; na janela de 72h apenas 2611.15639 e 2611.15346, ja entregues em 2026-11-13.

Deduplicacao: comparado com curadorias/curadoria-ia-direito_2026-11-13.md (arquivo de ontem) e com 2026-11-11 e 2026-11-12 (dias da janela ampliada), alem de consulta pontual a 2026-11-01 a 2026-11-10. Nenhum dos tres itens coincide por URL ou titulo. O balanco de Salomao foi descartado em 2026-11-13 como discurso sem dado (Correio Braziliense); aqui aparece apenas como dado de contexto dentro do item 2, agora com numeros.

Descartes no filtro deterministico (6): Claren Launches 'Envoys' Inhouse Agents (lancamento de fornecedor sem auditoria); Legora Targets Public Sector With Ex-Minister (contratacao, sem caso de uso); Mercedes Lawyer Joins AI Native Compound Law (contratacao); Keeping Legal AI Connected (conteudo patrocinado); Legal Innovators NY Starts Tuesday e Legal Innovators NY, Ropes & Gray (divulgacao de evento).

Descartes na triagem qualitativa (principais): Withers v. City of Aberdeen via Law Commentary (12/11) e RIO Rundown (13/11), decisao de 08/06/2026 ja descartada em execucoes anteriores; Is Big Law 'AI Gaslighting' Us? (Artificial Lawyer, 12/11), opiniao sem dado, ja descartado em 12/11 e 13/11; Shadow AI e os limites da governanca no trabalho (JOTA, Marcus Brumano, 14/11), texto integral inacessivel (paywall/JS), sem dado verificavel; "CNJ libera uso de IA no Judiciario, mas veda decidir culpa" (TV Sim Brasil e SpaceMoney, 14/11), reapresenta a Resolucao CNJ de 2025 sem fato novo; "Will Courts Enforce Protective Order Restrictions on AI Use?" (E-Discovery LLC, 12/11), comentario de post de 29/09 sem decisao nova; Proposed Rule 707 (E-Discovery LLC, 11/11), relatorio de maio ja coberto em 2026-10-17; Pikesville Deep Fake Audio, A Postscript (11/11), sentenca por crime sem relacao com o deepfake; Law360 2548668 e 2548487 (10/11), fora da janela e com paywall; lawsuit contra OpenAI, Google e Anthropic (Missouri Lawyers Media, 13/11), HTTP 403 Cloudflare e sem relacao direta com pratica juridica; JOTA "Fachin atende OAB e suspende prazos apos falha da Microsoft" (13/11), falha de infraestrutura sem componente de IA; demais itens de ConJur, JOTA e Volokh na janela sem relacao com IA.

Buscas: 23 buscas WebSearch, acima da faixa de 8 a 10, porque as primeiras retornaram majoritariamente material antigo sem filtro de data; as buscas adicionais foram dirigidas a datas e a fontes primarias (opiniao da Corte de Apelacao da California, materia original do g1, balanco do STJ).

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente. WebFetch recusou URLs sem proveniencia na conversa; a leitura foi feita via curl com extracao de texto local.
