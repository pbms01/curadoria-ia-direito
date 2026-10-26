CURADORIA DIARIA IA E DIREITO, 2026-10-26

CABECALHO
Data de coleta: 2026-10-26 (execucao iniciada por volta de 05h55 America/Sao_Paulo, 08h55 UTC)
Janela aplicada: 72h (escalonamento de nivel 1; em 36h so 1 item qualificado)
Buscas WebSearch executadas: 11
Feeds RSS consumidos com sucesso: 9 de 13
Candidatos coletados: 39 (30 entradas RSS na janela de 72h, 5 preprints no arXiv via API e 4 decisoes datadas na janela no AI Hallucination Cases Database); os links das 11 buscas WebSearch vieram fora da janela ou sem data verificavel e nao foram contados
Candidatos apos filtro deterministico: 10 (dos 39: 26 fora do escopo IA e Direito, 1 ficcao, 2 duplicatas de dias anteriores)
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 1 / (d) 1
Origem das fontes: midia tradicional 0% / Substack-RSS 67% (Volokh Conspiracy via RSS apontando para a base primaria de Damien Charlotin; Artificial Authority, Substack de Charlotin) / social 0% (o terceiro item, 33%, vem de repositorio academico, arXiv, fora das tres classes)


1. AI Hallucination Cases Database, queda trimestral, comentada em "AI & Law Stuff" (secao "All quiet on the hallucination front")
Fonte: Artificial Authority (Substack), Damien Charlotin; base de dados primaria do mesmo autor | URL primaria: https://www.damiencharlotin.com/hallucinations/ ; post: https://artificialauthority.ai/p/ai-and-law-stuff-273
Data de publicacao: 2026-10-23 (post); base com "Last updated: 25 October 2026"
Categoria: (b) erro ou fracasso documentado
Sintese: Charlotin afirma que, pelo segundo trimestre seguido, caiu o numero de decisoes com alucinacao de IA registradas na base (2.218 linhas no CSV baixado nesta execucao, licenca CC BY 4.0). Contagem propria por data da decisao no CSV: 2025Q3 270, 2025Q4 410, 2026Q1 455, 2026Q2 423, 2026Q3 359. Por parte: advogados 177, 164 e 145 de 2026Q1 a 2026Q3; litigantes pro se 269, 247 e 204. Causas apontadas pelo autor, sem medicao propria: modelos novos alucinam menos (cita um experimento com geracao de pecas juridicas, link para arXiv 2606.21155), investimento de fornecedores em verificacao, standing orders e efeito comportamental; ele registra tambem decisoes nos EUA que desentranham pecas so por falta da declaracao obrigatoria de uso de IA. Ressalvas do proprio autor: possivel subcoleta em algumas jurisdicoes e "hallucination fatigue" (menos casos notados ou reportados). O jornal coreano 법률신문 (Law Times) noticiou a queda do 2o trimestre em 2026-10-21.
Por que entrou: e o primeiro sinal quantitativo de inflexao na serie de sancoes por citacao inventada, com dado aberto que permite recontagem. A tese de deslocamento de erros legiveis (precedente inexistente) para ilegiveis (sicofantia, inputs adversariais) muda o alvo de verificacao em pipelines juridicos: checar existencia da citacao deixa de bastar.


2. AI Deepfakes in Court (base de dados), noticiada como "AI Deepfakes in Court"
Fonte: Damien Charlotin (base); The Volokh Conspiracy, Eugene Volokh (post) | URL primaria: https://www.damiencharlotin.com/deepfakes/ ; post: https://reason.com/volokh/2026/10/25/ai-deepfakes-in-court/
Data de publicacao: 2026-10-25 (post); data de lancamento da base [nao verificado]
Categoria: (c) risco novo importante
Sintese: Nova base, CC BY 4.0 com CSV, de decisoes em que se alegou ou se reconheceu deepfake submetido como prova (inclusive documentos, formularios e correspondencia), separada da base de alucinacoes e da base AI Evidence. Registra 26 casos de 2023-05-08 a 2026-10-09: EUA 12 (mais 1 marcado Pennsylvania), Canada 8, Hong Kong 3, Franca 1, Italia 1. Status da alegacao: 14 rejeitadas, 11 alegadas sem resolucao, 1 estabelecida (Mendones v. Cushman and Wakefield, Superior Court da California, Alameda, 2025-09-09: videos e capturas de mensagens reconhecidos como gerados ou alterados por IA, acao extinta com prejuizo como sancao com base no Cal. Civ. Proc. Code 128.7). Modalidade predominante: video (17 registros com video). Metodos de autenticacao codificados: testemunho (17), inspecao judicial (13), arquivo ou dispositivo original (12), sinal de proveniencia como C2PA ou marca d'agua (7), metadados (6), pericia (6). Caso mais recente: State v. Amyda, Suprema Corte de Iowa, 2026-10-09, que tratou a alegacao de deepfake do reu como "unsupported conjecture" e manteve condenacao com base em autenticacao por testemunho. A base codifica separadamente falha de autenticacao e achado de geracao por IA.
Por que entrou: e o primeiro conjunto estruturado e reaproveitavel sobre deepfake como prova em juizo, e os dados mostram que o risco dominante hoje e a alegacao defensiva de deepfake (25 de 26 sem achado positivo), resolvida majoritariamente por testemunho e inspecao, nao por forense tecnica. Relevante para cadeia de custodia e onus de autenticacao em prova digital.


3. UAE GovTrust Scope Filtering Gains and Routing Failures in Bilingual Public Service Retrieval
Fonte: arXiv, Aleksandar Mihajlovic | URL primaria: https://arxiv.org/abs/2610.32608
Data de publicacao: 2026-10-23
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: Diagnostico controlado de recuperacao ingles-arabe com 22 resumos de servicos publicos, 50 cenarios e 110 variantes de consulta, em que a consulta cita varias localidades mas so uma define a competencia do servico. Doze metodos comparados (lexical, denso, reciprocal rank fusion, filtro de escopo, cross-encoder multilingue, lookup direto). Em 72 consultas respondiveis com evidencia bilingue, RRF com filtro por papel do local acerta o primeiro resultado em 69 (95,8%), contra 47 (65,3%) sem filtro; denso filtrado e lookup direto chegam a 68 (94,4%). So com evidencia em ingles, excluir candidatos lexicais com score zero eleva a fusao filtrada de 52 para 64 acertos. Porem o roteador que infere escopo e acao acerta apenas 2 de 168 perturbacoes (parafrase, fato irrelevante, negacao, correcao). O autor declara que as perturbacoes sao diagnosticas, nao avaliacao held-out, que nao avalia respostas geradas nem correcao juridica, e que todas as 1.320 ordenacoes foram reproduzidas em ambiente limpo.
Por que entrou: isola um gargalo comum ao RAG juridico, filtrar por competencia ou jurisdicao quando a consulta menciona varios foros: metadado de escopo correto melhora muito o ranking, mas inferencia fragil de escopo elimina a evidencia antes da geracao. O desenho (filtro vs. roteador, com perturbacoes adversariais) e transponivel para recorte por tribunal, comarca ou ramo.


REVISAO ADVERSARIAL

Item 1. Fonte: primaria (base de dados do proprio autor) mais comentario do mesmo autor; autor identificado. URLs resolvem via curl (HTTP 200 para a base, o post e o artigo do Law Times). Dominios damiencharlotin.com e artificialauthority.ai sao os usados historicamente pela base (o feed damiencharlotin.substack.com redireciona para artificialauthority.ai); nao ha typosquat aparente. Numeros trimestrais: recontados nesta execucao a partir do CSV, nao copiados do post; a afirmacao de queda e confirmada de forma independente pelo Law Times (https://www.lawtimes.co.kr/news/articleView.html?idxno=228006, publicado 2026-10-21), que porem cita a mesma base. Limitacoes: base unica, curada por uma pessoa, com defasagem de coleta, o que pode inflar a queda de 2026Q3; 2026Q4 parcial (42) foi ignorado. Nao verificado: o conteudo do experimento citado (arXiv 2606.21155) e a frequencia de pecas desentranhadas por falta de declaracao de IA. Linguagem promocional: o post menciona o produto PelAIkan do autor na pagina da base; nao afeta os dados. Categoria (b) resiste: trata de erros documentados em decisoes, ainda que como serie agregada.

Item 2. Fonte: primaria (base com CSV e descricao de cada caso) e secundaria (Volokh, autor identificado). URLs resolvem (HTTP 200). Contagens por status e modalidade conferidas no CSV (26 linhas; 14/11/1). Nao verificado em segunda fonte: as decisoes individuais (State v. Amyda, Mendones) nao foram abertas nesta execucao; a data de lancamento da base nao aparece na pagina. Os itens 1 e 2 dependem do mesmo curador, o que reduz independencia entre eles; mantidos por terem objetos distintos (citacao inventada vs. prova fabricada) e numeros recontados do dado bruto. Base e work in progress com 26 casos: nao serve para inferir taxa ou prevalencia. Categoria (c) resiste. Linguagem promocional: nenhuma.

Item 3. Fonte: primaria (preprint), autor unico identificado, sem revisao por pares. URL resolve (HTTP 200). Numeros extraidos do abstract via API do arXiv; tabelas e codigo nao conferidos [nao verificado no corpo do paper]. Fragilidades: corpus minusculo e autoral (22 documentos), dominio de servico publico e nao juridico estrito, perturbacoes escritas pelo proprio autor; o resultado do roteador (2/168) e diagnostico, nao estimativa de desempenho. Categoria (d) resiste com ressalva de transposicao: o paper nao testa textos juridicos. Linguagem promocional: nenhuma.

Origem social: nenhum item depende de post em rede social; a busca site:x.com / reddit nao retornou post datado na janela.


AUDITORIA

Janela: 36h rendeu 1 item qualificado (item 2, Volokh 2026-10-25). Escalonado para 72h, que incluiu o post de Charlotin (2026-10-23 09:00 UTC) e o preprint GovTrust (2026-10-23 13:30 UTC). Parou em 72h com 3 itens.

Deduplicacao: arquivo de 2026-10-25 lido; tambem conferidos 2026-10-23 e 2026-10-24 por causa da janela ampliada. Excluidos como duplicata: "Some Communications by Rabbi Shmuley with AI Platforms May Be Discovered..." (Volokh, 2026-10-24; item 1 de 2026-10-25) e "The District Court, or Perhaps, Being Charitable, Its AI Agent..." (Volokh, 2026-10-23; item 1 de 2026-10-24).

Feeds que falharam ou vieram vazios: Stanford CodeX (HTTP 404, pagina "Page not found"); Above the Law tag IA (HTTP 200, mas sem entradas parseaveis); ConJur (HTTP 403, desafio Cloudflare; compensado com busca site:conjur.com.br, que nao retornou materia da janela, e WebFetch de conjur.com.br/?p=892454 falhou com client_error); Migalhas (HTTP 404, devolve HTML da home). Feeds sem entradas na janela de 72h: LawSites e LawNext (ultima entrada 2026-10-22), 3 Geeks (2026-10-14), Artificial Lawyer (2026-10-23, fora da janela), Harvard Law Review Blog (2026-09-07).

Descartes:
"Not Anymore, Part Two" (Adam Unikowsky, 2026-10-23): ficcao especulativa sobre adulteracao de precedentes por IA, sem dado verificavel.
JOTA, 14 entradas: eleicoes 2026, ESG, feminicidio, precedentes sem IA; fora do escopo.
Volokh, 11 entradas restantes: tarifas, historia da Suprema Corte, open threads, eleicoes; fora do escopo.
4 decisoes de 2026-10-23 no AI Hallucination Cases Database (American Leadership Academy v. Sherburne; Boyd v. Beachwood City School District; Lewis v. Cameron-Nichols; Paananen v. Peckham): pro se, advertencia ou custos, sem elemento novo.
arXiv 2610.32576 (privacy climate e GDPR): pesquisa com desenvolvedores, sem IA aplicada ao Direito.
arXiv 2610.32238 e 2610.32226 (armas ciberneticas autonomas): pesos e limiares declarados ilustrativos, nao ajustados.
arXiv 2610.32245 (agente cientifico e MDL): fora do escopo juridico.
"Lawyers Sanctioned Over AI Use on Both Sides in Federal Case" (Bloomberg Law, Mississippi): de junho de 2026, fora da janela.
Demais resultados WebSearch (ABA, ABA Journal, CNJ, STF, TJPR, TJSC, TSE, materias de previsoes para 2026, LegalCiteBench): sem data na janela ou ja antigos.

Substituicoes: nenhuma; todas as URLs entregues resolveram via curl.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
