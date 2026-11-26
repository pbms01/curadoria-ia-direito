CURADORIA DIARIA IA E DIREITO, 2026-11-26

Data de coleta: 2026-11-26 (America/Sao_Paulo), inicio por volta de 05h30
Janela aplicada: 72h (escalonada a partir de 36h; corte em 2026-11-23 08h54 UTC)
Buscas WebSearch executadas: 10
Feeds RSS consumidos com sucesso: 9 de 13
Candidatos coletados: 74 (61 entradas RSS na janela de 72h; 6 preprints arXiv de direito e LLM submetidos entre 23/11 e 25/11 via API do arXiv; 7 candidatos via WebSearch e base Charlotin, dos quais 6 com data de decisao fora da janela)
Candidatos apos filtro deterministico: 73 (1 removido por deduplicacao contra 2026-11-25; nenhum removido por vocabulario promocional ou press release; o corte de volume ocorreu na triagem qualitativa, por falta de pertinencia a IA e Direito)
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 0 / (d) 2
Origem das fontes: midia tradicional e fonte judicial primaria 33% (Court News Ohio e slip opinion da Suprema Corte de Ohio) / Substack-RSS 0% / social 0% / repositorio academico (arXiv) 67%


1. Attorney Suspended for Fake AI Cases, Other Ethics Violations (Cleveland Metro. Bar Assn. v. Wilson, Slip Opinion No. 2026-Ohio-4626)
Fonte: Court News Ohio (servico de noticias da Suprema Corte de Ohio), texto de Dan Trevas, com link para a decisao | URL primaria: https://www.supremecourt.ohio.gov/rod/docs/pdf/0/2026/2026-Ohio-4626.pdf
Fonte secundaria: https://www.courtnewsohio.gov/cases/2026/SCO/1124/260724.asp
Data de publicacao: 2026-11-24
Categoria: (b) erro ou fracasso documentado
Sintese: A Suprema Corte de Ohio, em per curiam unanime no caso No. 2026-0724 (decidido em 24/11/2026, a partir do relatorio No. 2025-016 do Board of Professional Conduct), suspendeu por prazo indeterminado a advogada Arleesha Wilson, de Cleveland. Um dos cinco casos disciplinares envolve uma acao contra a cidade de Cleveland removida ao U.S. District Court for the Northern District of Ohio: a cidade apontou que a peca de oposicao citava quatro precedentes inexistentes e trechos que nao constavam das decisoes citadas. Intimada a apresentar os quatro julgados, Wilson juntou 1.395 paginas de jurisprudencia sem eles e, na audiencia de contempt, ofereceu tres outros casos com nomes, anos e tribunais diferentes, antes de admitir, sob pergunta do juiz, ter usado IA na redacao. O juizo federal reconheceu conduta frivola, deturpacao do alcance de outros sete precedentes e aplicou multa de US$ 7.500 em outubro de 2025, que nao foi paga ate a audiencia disciplinar de marco de 2026. O total de condenacoes pendentes contra ela supera US$ 647.000, incluindo indenizacao de US$ 625.000 por malpractice em outro caso.
Por que entrou: Caso concreto em que a alucinacao de citacoes deixa de ser tratada como sancao processual isolada e passa a compor fundamento de suspensao profissional por instancia disciplinar de cupula estadual. O agravante decisivo foi a falta de franqueza sobre o uso de IA, nao o erro em si, o que interessa diretamente a desenho de politicas de declaracao de uso.


2. Automated Call for Action: RAG-Based Environmental Law Enforcement Screening System
Fonte: arXiv (cs), preprint de Matas Jurkevicius e Yen-Chia Hsu (University of Amsterdam) | URL primaria: https://arxiv.org/abs/2611.30423
Data de publicacao: 2026-11-23
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O trabalho testa um pipeline de triagem para fiscalizacao ambiental no caso das coquerias KGF1 e KGF2 da Tata Steel em IJmuiden, supervisionadas pelo servico ambiental regional neerlandes OD NZKG. Um modelo de trajetoria de pluma alinha medicoes de qualidade do ar, dados meteorologicos e reclamacoes de moradores a cada evento de emissao; um pipeline RAG recupera as condicoes de licenca especificas da instalacao e gera relatorios por evento e um relatorio de periodo com recomendacao de investigacao. Em 74 eventos de marco de 2025, a busca hibrida produziu 58,1% de relatorios citando condicoes da outra planta; um re-ranking com rotulos de planta baseados em regra levou esse indice a 0%, mantendo metricas RAGAS e de LLM-judge altas. GPT-5-mini teve desempenho comparavel ao GPT-5.1, e GPT-5-nano pontuou abaixo em legal grounding e legal faithfulness. Na ablacao de evidencias, remover dados de qualidade do ar foi o que mais alterou notas e recomendacoes; remover detalhes das reclamacoes nao teve efeito mensuravel.
Por que entrou: Mede um modo de falha tipico de RAG juridico sobre corpus normativo quase identico (licencas de duas plantas do mesmo operador), com quantificacao do erro de atribuicao de fonte e da correcao por metadado deterministico. O achado de que reclamacoes nao pesam na saida tem implicacao direta para a admissibilidade de prova cidada em fluxos automatizados.


3. From Data Room to Report: End-to-End AI Support for M&A Legal Due Diligence
Fonte: arXiv (cs.CL), preprint de Johannes R. Huebers e coautores (Fraunhofer IAIS, Lamarr Institute, Universidade de Bonn e escritorio GOERG Partnerschaft von Rechtsanwaelten) | URL primaria: https://arxiv.org/abs/2611.34120
Data de publicacao: 2026-11-25
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O artigo descreve o LEXI (Legal Extraction and Intelligence), sistema em desenvolvimento que cobre a due diligence de M&A desde a ingestao do virtual data room ate a preparacao do relatorio. O sistema classifica documentos numa taxonomia configuravel, atribui entidades-alvo, extrai campos predefinidos com trecho de suporte e proveniencia por pagina e passa os resultados entre etapas por saidas estruturadas, com revisao e correcao pelo advogado. A classificacao foi avaliada em dois data rooms de transacoes alemas reais (76 e 73 documentos, 72 tipos documentais) com Hit@k e MRR, comparando GPT-5.4, GPT-5.4 mini e GPT-5.4 nano com e sem thinking; ativar thinking elevou o Hit@1 do rotulo primario nas seis comparacoes modelo e data room. A extracao foi conferida por um especialista em 41 predicoes em alemao, todas coincidentes com a anotacao de referencia, sem conferir os trechos de suporte. A etapa de relatorio ainda nao foi avaliada formalmente, e os autores declaram a amostra insuficiente para estimativa robusta de acuracia.
Por que entrou: Arquitetura com proveniencia por pagina e handoff estruturado entre etapas, validada com dados de transacao real e coautoria de escritorio de advocacia, com limites declarados pelos proprios autores. A escolha de metricas de ranking em vez de macro-F1 por causa do suporte reduzido por classe e uma decisao de avaliacao reaproveitavel em taxonomias juridicas longas.


REVISAO ADVERSARIAL

Item 1 (Wilson, Ohio): fonte primaria (slip opinion 2026-Ohio-4626) baixada via curl do dominio oficial supremecourt.ohio.gov, HTTP 200, PDF de 338 KB; o texto confirma o caso No. 2026-0724, decisao em 24/11/2026, suspensao indeterminada, multa federal de US$ 7.500 e a admissao do uso de IA na audiencia. A materia do Court News Ohio (courtnewsohio.gov, servico oficial do tribunal, autor identificado) resolveu com HTTP 200. Numeros conferidos apenas na materia e na decisao, que tem a mesma origem institucional: US$ 647.000, US$ 625.000, 1.395 paginas e sete precedentes deturpados [nao verificados em fonte independente]. A designacao "per curiam unanime" vem da materia [nao conferida no rodape de votos da decisao]. Linguagem promocional ausente. Categoria (b) resiste: sancao disciplinar documentada com decisao citada. Publicacao em 24/11 sem horario confirmado; pode estar dentro da janela de 36h, mas foi tratada como item de 72h.

Item 2 (RAG ambiental): preprint sem revisao por pares; arxiv.org/abs/2611.30423 resolve via curl (HTTP 200), dominio oficial. Autores identificados com e-mail institucional da UvA. A pagina traz cabecalho de template da ACM FAccT 2027 [aceitacao nao verificada]. Os valores 58,1%, 0% e 74 eventos foram conferidos no resumo e no HTML do artigo, sem segunda fonte independente [nao verificado]. Os nomes de modelos (GPT-5-mini, GPT-5.1, GPT-5-nano) sao os relatados pelos autores. Linguagem promocional ausente. Categoria (d) resiste: o achado central e um mecanismo de retrieval com erro medido. O caso e de fiscalizacao ambiental administrativa, nao de processo judicial, o que limita a transposicao direta.

Item 3 (LEXI): preprint autodeclarado work in progress; arxiv.org/abs/2611.34120 resolve (HTTP 200). Autores e afiliacoes identificados no HTML, incluindo advogados do escritorio GOERG, o que configura possivel interesse em apresentar o sistema [registrado, sem indicio de linguagem de fornecedor]. Os valores 76, 73, 72 tipos e 41 predicoes foram conferidos no HTML; os valores de Hit@1 e MRR da Tabela 2 nao foram transcritos por nao terem sido extraidos com seguranca do HTML. Nenhum numero tem segunda fonte [nao verificado]. A amostra de extracao (41) e pequena, como os proprios autores reconhecem. Categoria (d) resiste, sem migrar para (a): nao ha resultado mensuravel de producao.

Descartes nesta etapa: GlobalHRBench (arxiv.org/abs/2611.29852) e o trabalho de confianca por campo em extracao com VLM (arxiv.org/abs/2611.30119), ambos pertinentes, foram descartados por terem sido submetidos em 23/11 antes do corte de 72h (00h19 e 06h21 UTC). Nenhuma substituicao foi necessaria. Nenhum item tem origem social.


AUDITORIA

Janela: 36h aplicada inicialmente (corte em 2026-11-24 20h54 UTC). Nessa janela, o unico candidato qualificado com seguranca foi o LEXI; os 45 itens RSS eram majoritariamente fora do tema (ConJur, JOTA e Volokh sobre trabalhista, eleitoral, Segunda Emenda etc.), e a decisao de Ohio nao tinha horario de publicacao confirmado. Escalonado para 72h, nivel em que se atingiram 3 itens; nao foi necessario ir a 7 dias.

Deduplicacao: feita contra curadorias/curadoria-ia-direito_2026-11-25.md e, pelo escalonamento, contra 2026-11-23 e 2026-11-24. Removido: arxiv.org/abs/2611.31679 ("Rethinking Document Indexing for LLM-based Analysis"), ja entregue em 2026-11-25. Os casos Lingle v. Subaru e Kavanagh v Atlassian, da base Charlotin, ja entregues em 2026-11-24, nao foram reconsiderados.

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Artificial Lawyer (HTTP 200, mas pagina HTML de desafio com reload em JavaScript, 0 entradas); Above the Law tag IA (HTTP 200, mas HTML do site em vez de feed, 0 entradas). O ConJur respondeu normalmente nesta execucao (HTTP 200, 10 entradas), e a busca site:conjur.com.br foi feita mesmo assim. Feeds validos sem entradas na janela: Adam Unikowsky (ultima em 23/10), Damien Charlotin Substack (ultima em 20/11), 3 Geeks (16/11), Harvard Law Review Blog (10/11); LawSites e LawNext tiveram 1 entrada cada na janela de 72h, sem tema de IA aplicavel.

Base Charlotin: "Last updated: 25 November 2026". O unico documento com data de 25/11 no nome do arquivo e Messinger v. Samsung Electronics America Inc. (S.D. Florida), mas a decisao e de 10/11/2026 e consiste em advertencia a litigante pro se; descartado por data fora da janela. Garner v. Mendelsohn (20/11), Rodriguez v. Rodriguez (19/11) e People v. Perrot (19/11), todos pro se, descartados por data de decisao fora da janela de 72h.

Hacker News: a busca por data via API Algolia nao trouxe item de IA e Direito na janela (o post mais proximo, "Ask HN: Did Aaron Swartz make modern AI possible?", e opinativo e sem dado). A primeira tentativa com filtro numerico retornou HTTP 400; a segunda, sem filtro, funcionou.

Descartes da triagem qualitativa (amostra relevante):
Delaware Chancery Court Sanctions Attorney for AI Hallucinations (news.bgov.com): publicado em 13/11, fora da janela.
STF, ARE 1608713, comandos ocultos detectados pela Maria Shield (noticias.stf.jus.br): noticia de 25/09/2026, fora da janela e tema ja coberto em curadorias anteriores; a variante ?p=166664 respondeu HTTP 403.
Nota tecnica do CNJ sobre manipulacao de sistemas de IA (portal.trf6.jus.br/?p=137119): URL nao resolveu (HTTP 000, timeout), sem data verificavel.
ConJur, "Condenacao nao encerra prova digital: como pedir acervo bruto na fase recursal" (25/11): tema de prova digital, sem componente de IA; fora do escopo da curadoria.
ConJur, "Do autoritarismo ao totalitarismo digital" (25/11): artigo opinativo sem dado verificavel.
JOTA, "Inteligencia Artificial na Medicina e a Resolucao CFM 2.454/2026" (25/11): regulacao medica, sem eixo juridico-processual; opinativo.
arXiv 2611.34094 (diretrizes de IA generativa em universidades canadenses), 2611.32355 (infraestrutura de neuroimagem) e 2611.31442 (retrieval sensivel a inversao semantica, sem corpus juridico identificado no resumo): fora do tema ou sem dado juridico.
Resultados de busca sobre adocao de IA por escritorios (Bloomberg Law, bestlawfirms.com): pesquisas de percepcao e materias reproduzidas em dezenas de URLs, sem resultado mensuravel de implantacao.
Buscas X/Twitter e Reddit: nenhum post com fonte primaria localizavel na janela; retornaram newsletters e materiais de 2024 e 2025.

Seguranca: nenhum conteudo coletado continha instrucoes direcionadas ao agente.
