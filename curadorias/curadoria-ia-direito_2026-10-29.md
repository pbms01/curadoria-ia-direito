CURADORIA DIARIA IA E DIREITO, 2026-10-29

CABECALHO
Data de coleta: 2026-10-29 (execucao iniciada por volta de 06h00 America/Sao_Paulo, 09h00 UTC)
Janela aplicada: 7 dias (escalonamento de nivel 2; em 36h nenhum item qualificado, em 72h apenas 2)
Buscas WebSearch executadas: 19
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 84 (57 entradas RSS unicas na janela de 72h; 3 entradas RSS com tema IA entre 72h e 7 dias; 9 artigos da API do arXiv com tema juridico submetidos desde 2026-10-22; 8 decisoes no AI Hallucination Cases Database datadas de 2026-10-22 em diante; 7 materias ou decisoes examinadas a partir do WebSearch)
Candidatos apos filtro deterministico: 14
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 2 / (d) 0
Origem das fontes: midia tradicional 33% (NY Daily Record) / Substack-RSS 0% / social 0% (os outros dois itens, 67%, vem de decisao judicial obtida via base de dados academica e de repositorio academico, arXiv, fora das tres classes)


1. South African Post Office SOC Ltd (In Business Rescue) and Others v Commissioner Menzi Fakude N.O. and Others, Labour Court of South Africa, Johannesburg, Case No. 2026-249228
Fonte: AI Hallucination Cases Database (Damien Charlotin), que hospeda a integra da decisao | URL primaria: https://www.damiencharlotin.com/documents/3361/SA_Post_Office_v._Fakuade_South_Africa_23-10-2026.pdf
Data de publicacao: 2026-10-23
Categoria: (b) erro ou fracasso documentado
Sintese: Pedido urgente dos Correios sul-africanos (SAPO), em business rescue desde 2023, e de dois business rescue practitioners para suspender arbitragem de dispensa injusta na CCMA. O arbitro (Commissioner Fakude) decidiu prosseguir com base em "South African Post Office SOC Ltd v Communication Workers Union [2023] ZACC 40", que teria afirmado que o business rescue nao suspende a legislacao trabalhista. O juiz interino S. Snyman pesquisou o SAFLII e as bases usuais e nao encontrou o julgado; a referencia 2023 ZACC 40 corresponde a Rayment v Minister of Home Affairs, sobre vistos de conjuge. A decisao (paras. 49 e 55) infere uso de IA sem verificacao, qualifica a conduta como misconduct e irregularidade material, afirma que o arbitro deve verificar se o julgado existe e le-lo, e propoe "zero-tolerance". Resultado: arbitragem suspensa e interditada ate o julgamento da revisao, sem condenacao em custas; o merito tambem se apoiou na moratoria do s 133(1) do Companies Act e na falta de citacao dos practitioners. A decisao cita precedente anterior (FJL v TGO) envolvendo juiz interino.
Por que entrou: e o julgador, e nao a parte, quem decide com base em precedente inexistente, e o tribunal revisor trata isso como vicio que justifica intervencao imediata. O teste aplicado (existencia do julgado e leitura do holding) e o mesmo controle minimo que um pipeline de citacao verificavel precisa automatizar.


2. Penny for Your Prompts: A Measurement Study of Contextual Leakage in AI Chat Platforms
Fonte: arXiv (2610.37467), Paschalis Bekos, Billy Tsouvalas, Nick Nikiforakis e Michalis Polychronakis, Stony Brook University | URL primaria: https://arxiv.org/abs/2610.37467
Data de publicacao: 2026-10-27
Categoria: (c) risco novo importante
Sintese: Auditoria das interfaces web de 42 chatbots (25 de uso geral e 17 de dominio especifico: educacao, saude e juridico; no juridico, LawConnect, NyayGuru, AI Lawyer e TheLawGPT), com instrumentacao do navegador no nivel do motor JavaScript (Puppeteer e VisibleV8) para atribuir cada fluxo de dados a acao do usuario que o disparou. Resultado: 21 plataformas enviam o titulo da conversa a trackers de terceiros e 9 enviam o prompt literal. Nas plataformas juridicas, cerca de 317 requisicoes a trackers por plataforma, 9% delas com conteudo do usuario; 2 das 4 juridicas analisadas vazam contexto. O prompt de teste juridico incluia pergunta sobre situacao migratoria. O AI Lawyer envia titulo da conversa e e-mail do usuario na mesma requisicao a Meta e ByteDance. Conteudo trafega em texto claro; e-mail, nas juridicas, em geral como hash SHA-256. ChatGPT e Grok tinham trackers coletando contexto durante o estudo e os removeram; o TheLawGPT corrigiu apos notificacao.
Por que entrou: o vetor nao e o modelo, e o script de analytics e session replay da pagina, que captura o DOM antes mesmo da resposta. Para quem usa ou recomenda assistentes juridicos web, isso e quebra de sigilo verificavel em trafego de rede, e o metodo de atribuicao serve como roteiro de auditoria tecnica e de prova digital.


3. The Risks of Using Artificial Intelligence in Preparing Court Papers: What Every Attorney Should Know (New York State Unified Court System), noticiada como "NY court officials release AI guide for lawyers"
Fonte: NY Daily Record, reportagem de Bennett Loudon | URL primaria: https://nydailyrecord.com/2026/10/27/ny-court-officials-ai-guide-for-lawyers-responsible-use/
Fonte secundaria: amNY, reportagem de Isabella Gallo, https://www.amny.com/law/nys-court-system-ai-attorney-guide/ ; documento oficial em https://webfiles.nycourts.gov/public/2026-10/guidance-document-for-attorneys.pdf [nao verificado: HTTP 403 a partir deste ambiente]
Data de publicacao: 2026-10-27
Categoria: (c) risco novo importante (problema regulatorio emergente)
Sintese: O Advisory Committee on Artificial Intelligence and the Courts, nomeado pelo Chief Administrative Judge Joseph A. Zayas, publicou guia de sete paginas para advogados. Pontos relatados pelas duas reportagens: uso de IA generativa em pecas permitido sem dever de divulgacao ao juiz nem certificacao propria, alem da certificacao implicita da assinatura; dever de conferir citacoes e transcricoes em ferramentas de pesquisa autoritativas, ler cada julgado e documentar os passos de verificacao; manutencao integral das obrigacoes das Rules of Professional Conduct e de 22 NYCRR Part 130 (sancoes por conduta frivola); ordens permanentes de cada juiz prevalecem sobre o guia. Heidi Brown (New York Law School), ouvida pelo amNY, criticou a ausencia de divulgacao e apontou o problema dos "misgroundings" (julgado real com holding distorcido). Data exata de liberacao: amNY indica segunda-feira 26/10, NY Daily Record indica 27/10 [nao verificado].
Por que entrou: um dos maiores sistemas judiciais dos EUA escolhe nao exigir disclosure e concentrar o controle na verificacao documentada pelo advogado. Isso desloca o risco para o fluxo interno de revisao e torna a trilha de verificacao (o que foi checado, onde, quando) o elemento probatorio relevante em eventual sancao.


REVISAO ADVERSARIAL

Item 1. Fonte primaria: sim, integra da decisao (PDF de 47 paginas, "Reportable: Yes"), baixada via curl (HTTP 200, application/pdf) e lida: numero do processo, juiz (S Snyman, AJ), paras. 46 a 49 (julgado inexistente e Rayment) e 54 a 56 (misconduct, zero-tolerance) conferidos no texto. Dominio damiencharlotin.com e o da base mantida por Damien Charlotin (HEC Paris), mesma origem usada em curadorias anteriores; nao e o site oficial do tribunal. Nao verificado em segunda fonte: publicacao no SAFLII ou em site oficial do Labour Court; o uso de IA e inferencia do tribunal ("must have relied on AI"), nao fato admitido pelo arbitro. A grafia "Fakuade" no nome do arquivo diverge de "Fakude" na decisao; adotada a da decisao. Sem linguagem promocional. Categoria (b) resiste.

Item 2. Fonte primaria: sim, preprint no arXiv; PDF baixado via curl (HTTP 200) e lido nos trechos de metodologia (secao 3.1), resultados juridicos (secoes 4.2 e 4.3, Tabela 2, Figura 10) e divulgacao responsavel. Autores identificados com afiliacao institucional. Sem revisao por pares confirmada: o PDF traz nota de copyright IEEE 2027, mas o veiculo de aceitacao nao foi verificado [nao verificado]. Amostra juridica pequena (4 plataformas, todas de nicho, nenhuma das grandes ferramentas juridicas corporativas); os numeros de 317 requisicoes e 9% sao medias da categoria e o proprio artigo diz que o vazamento juridico se concentra quase todo no AI Lawyer. Nao replicado por terceiros. Categoria (c) resiste.

Item 3. Fonte primaria oficial (PDF do nycourts.gov) nao resolvida neste ambiente (HTTP 403 via curl; WebFetch sem autorizacao); tentativa adicional com outro user-agent foi bloqueada pela politica do ambiente e nao foi repetida. Substituida como URL primaria pela reportagem do NY Daily Record (HTTP 200, autor identificado, datePublished 2026-10-27T15:57Z), com confirmacao independente pelo amNY (HTTP 200, autora identificada, 2026-10-27T17:00 -04:00). Titulo do guia, sete paginas, comite, Part 130 e ausencia de disclosure aparecem de forma convergente nas duas reportagens; citacoes literais do guia nao foram conferidas no documento original. Data exata de liberacao divergente entre as fontes. Categoria (c) e discutivel (orientacao, nao norma vinculante; o guia diz que ordens de juizes prevalecem); mantida como problema regulatorio emergente por falta de candidato mais forte na janela.


AUDITORIA

Nivel de janela: 36h sem item qualificado (entradas recentes eram politica, tributario ou noticias de fornecedor); 72h com 2 itens (itens 2 e 3); escalonado para 7 dias, onde entrou o item 1 (2026-10-23). Deduplicacao feita contra curadorias de 2026-10-22 a 2026-10-28 por URL e titulo.

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, mas devolveu pagina HTML, 0 entradas); Harvard Law Review Blog (HTTP 200, 8 entradas, nenhuma na janela, contado como consumido). ConJur respondeu HTTP 200 com 10 entradas, nenhuma sobre IA; busca site:conjur.com.br complementar nao trouxe resultado do dominio.

Descartes:
"Lexis Protege Is Labeling Your Downloads AI-Generated" (3 Geeks, 2026-10-27): ja entregue em 2026-10-28.
"Anthropic Increases Legal Vertical Push With Artifacts" (Artificial Lawyer, 2026-10-28): noticia de fornecedor sem resultado mensuravel.
"AI Governance Must Keep Pace with Legal Practice" (Artificial Lawyer, 2026-10-29): opiniao generica, sem dado verificavel.
"ClioCon 2026: A Quick Wrap-Up" (LawNext, 2026-10-26) e "LexisNexis Protege Is Now Live In EvenUp" (2026-10-22): anuncios de fornecedor sem auditoria independente.
"Not Anymore, Part Two" (Adam Unikowsky, 2026-10-23): ficcao especulativa, ja descartada em dias anteriores.
"AI & Law Stuff" (Artificial Authority, 2026-10-23): ja coberto em 2026-10-25.
Moore v. Jackson Walker LLP (S.D. Tex., 2026-10-21, US$ 7.500, parte sem advogado): caso rotineiro de citacao inexistente, menos informativo que o item 1.
Paananen v. Peckham, Boyd v. Beachwood, Lewis v. Cameron-Nichols, American Leadership Academy v. Sherburne (2026-10-23): partes sem advogado, advertencias ou custas simbolicas, sem detalhe tecnico.
U.S. HHS and NTEU, 74 FLRA No. 87, e Chilingarian v. Blanche: ja entregues em dias anteriores.
PatentAgentBench, "Officially corrected errors persist in AI training data", UAE GovTrust e "Commit or Abstain?": ja entregues em dias anteriores.
Juiz ve uso indevido de IA em contestacao e condena Crea/RS (Migalhas): publicado em julho de 2026, fora da janela.
Turma Recursal do TJDFT anula sentenca redigida por IA (Bocater): acordao de outubro de 2025, fora da janela.
Atty With False AI Citation Filings Ordered To Pay $39K (Law360, 2026-10-09): fora da janela e numero do processo atras de paywall.
STJ multa tentativa de manipular IA com texto oculto (2026-10-22): ja coberto em curadorias anteriores.
California Supreme Court e brief de promotoria com alucinacoes (Daily Journal): sem fato novo datado na janela.
"Free Speech Unmuted: Flock Cameras and the Fourth Amendment" (Volokh, 2026-10-27): podcast, sem dado verificavel extraivel.
Busca X/Twitter e Reddit: nenhum post dos handles ancora com fonte primaria nova na janela.

Substituicoes: item 3 teve a URL primaria oficial (nycourts.gov, 403) substituida pela reportagem do NY Daily Record, mantida a URL oficial como referencia nao verificada.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
