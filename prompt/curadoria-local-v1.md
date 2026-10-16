Produza a CURADORIA DIARIA IA E DIREITO de hoje e grave o arquivo .md em DUAS pastas. Este prompt e autocontido; siga-o integralmente.

DESTINATARIO
Pedro Mourao. Perfil tecnico em IA aplicada ao Direito, crimes digitais, prova digital, pipelines RAG juridicos, dialetica. Tom tecnico-colaborativo, sem hype, sem hedging excessivo, sem postambulo, sem travessao. Portugues brasileiro, termos tecnicos em ingles quando consagrados.

PARAMETROS
Timezone: America/Sao_Paulo. Use `date +%F` em bash para a data de hoje (AAAA-MM-DD).
Pasta de saida 1: C:\Users\pbm_s\Ia_e_justica\Agente de curadoria Anti-hype AI
Pasta de saida 2: C:\Users\pbm_s\automacao_podcastia\entrada
O arquivo final deve ser gravado IDENTICO nas duas pastas. Em bash elas aparecem sob /sessions/<id>/mnt/ como "Agente de curadoria Anti-hype AI" e "entrada"; o <id> varia a cada execucao, entao resolva dinamicamente (ex.: `ls -d /sessions/*/mnt/`). Confirme as duas gravacoes com `cmp` antes de encerrar.

ETAPA 0, FERRAMENTAS
Carregue via ToolSearch: WebSearch, mcp__workspace__web_fetch, Read, mcp__workspace__bash. Instale feedparser se necessario (`pip install feedparser --break-system-packages`).

ETAPA 1, JANELA E DEDUPLICACAO
Janela base: ultimas 36h. Escalonamento progressivo se ao fim da triagem houver menos de 3 itens qualificados: 36h, depois 72h, depois 7 dias. Pare ao atingir 3 itens ou 7 dias. Registre na AUDITORIA o nivel aplicado. Deduplicacao: leia o arquivo do dia anterior em "Agente de curadoria Anti-hype AI" (curadoria-ia-direito_AAAA-MM-DD.md com a data de ontem); extraia URLs e titulos; exclua candidatos com URL canonica identica ou titulo normalizado equivalente (lowercase, sem pontuacao, jaccard > 0.8). Se escalonar, dedupique tambem contra os arquivos dos dias da janela ampliada.

ETAPA 2, COLETA EM TRES CAMADAS
Camada A, RSS via bash + curl (nao use WebFetch para feeds). Para cada feed: `curl -sL --max-time 20 -A "Mozilla/5.0 (curadoria-ia-direito)" "URL" | head -c 200000`. Parse com feedparser (Python). Feeds: LawSites https://www.lawsitesblog.com/feed ; LawNext https://www.lawnext.com/feed ; Stanford CodeX https://law.stanford.edu/codex-the-stanford-center-for-legal-informatics/feed/ ; Above the Law IA https://abovethelaw.com/tag/artificial-intelligence/feed/ ; Adam Unikowsky https://adamunikowsky.substack.com/feed ; Damien Charlotin Substack https://damiencharlotin.substack.com/feed ; 3 Geeks https://www.geeklawblog.com/feed/ ; Artificial Lawyer https://www.artificiallawyer.com/feed/ ; ConJur https://www.conjur.com.br/rss.xml ; JOTA https://www.jota.info/feed ; Migalhas https://www.migalhas.com.br/rss ; Volokh https://reason.com/volokh/feed/ ; Harvard Law Review Blog https://harvardlawreview.org/blog/feed/ . Feed que falhar ou vier vazio: registre na AUDITORIA e siga.
Camada B, WebSearch (8 a 10 buscas). Mescle vetores: internacional ("AI hallucination court sanction 2026", "law firm generative AI deployment results", "legal RAG benchmark citation 2026", "judicial AI ruling sanction"); Brasil ("tribunal inteligencia artificial CNJ decisao 2026", "STF IA precedente", "advogado ChatGPT alucinacao sancao OAB 2026"); X/Twitter via site:x.com OR site:twitter.com filtrando handles ancora (@computational, @parredondo, @glambert, @andrewmperlman, @damienriehl, @bobambrogi, @DamienCharlotin, e contas BR como "Atheniense IA", "Renato Opice Blum IA"); Reddit site:reddit.com/r/LegalTech OR r/MachineLearning "legal AI"; YouTube so palestras verificaveis de eventos (CodeX, ABA, legal innovation).
Camada C, agregadores. Hacker News site:news.ycombinator.com "legal" "AI" na janela. Damien Charlotin database via curl em https://www.damiencharlotin.com/hallucinations/ : leia "Last updated" e cheque casos com data dentro da janela.
Total esperado: 30 a 80 candidatos. Registre o numero exato.

ETAPA 3, TRIAGEM EM DOIS PASSOS
3.1 Filtro deterministico anti-hype. Rejeite manchete/primeiro paragrafo com: revolucionario, game-changer, vai mudar, futuro da advocacia, "X ferramentas que", parceria estrategica sem caso de uso, transformador, disruptivo. Rejeite press releases (PRNewswire, BusinessWire, Globe Newswire, EIN Presswire), carrossel LinkedIn, thread "I asked GPT to do X", demo de fornecedor sem auditoria independente, autoria nao identificavel.
3.2 Classificacao qualitativa em 4 buckets: (a) inovacao de sucesso comprovada com resultado mensuravel; (b) erro ou fracasso documentado (falha tecnica, sancao judicial, alucinacao em decisao citada, vazamento, vies com dado); (c) risco novo importante (vulnerabilidade, vetor de ataque, problema regulatorio emergente, dilema etico com tracao factual); (d) solucao para gargalo em pipelines juridicos (RAG juridico, chunking de pecas, citacao verificavel, reducao de alucinacao, context ingestion, NER juridico, embeddings para portugues juridico, eval datasets). Cada candidato precisa de dado verificavel (numero, decisao citada, paper, descricao tecnica concreta). Origem social exige fonte primaria localizavel e checada de forma independente. Selecione exatamente 3, sem cota por origem.

ETAPA 4, SINTESE
Para cada item, em prosa (markdown minimo, sem #, sem bullets):
[N]. TITULO ORIGINAL
Fonte: [veiculo] | URL primaria: [link direto]
Fonte secundaria (se origem social): [URL do post que sinalizou]
Data de publicacao: AAAA-MM-DD
Categoria: [(a)/(b)/(c)/(d) com nome do bucket]
Sintese: 5 a 8 linhas, factual, com atores, numeros, mecanica tecnica e estado atual, sem juizo de valor explicito.
Por que entrou: 2 a 3 linhas com o criterio (gargalo, risco ou caso concreto).

ETAPA 5, REVISAO ADVERSARIAL
Bloco "REVISAO ADVERSARIAL" reavaliando cada item: fonte primaria ou terceiros? autor identificado? URL resolve via fetch/curl real (confirme; se nao resolve, descarte ou substitua)? dominio oficial, nao typosquat? numeros/datas/citacoes nao verificados em segunda fonte (liste-os)? linguagem promocional residual? categoria resiste? Para origem social: fonte primaria verificada de forma independente? conta com historico minimo de 6 meses? claim resiste fora do contexto do post? Documente descartes e substituicoes.

ETAPA 6, ENTREGA
Nome do arquivo: curadoria-ia-direito_AAAA-MM-DD.md (data local de hoje). UTF-8 sem BOM, quebras LF. Gravacao imediata: assim que o conteudo do arquivo estiver finalizado, grave-o DIRETAMENTE nas DUAS pastas de destino (Pasta de saida 1 e Pasta de saida 2), sem deixa-lo apenas em outputs e sem adiar a gravacao para depois de outras etapas. Logo apos gravar, confirme as duas gravacoes com `cmp` (e que nao ha BOM e que as quebras sao LF). Se preferir compor o conteudo num arquivo temporario antes, faca a copia para as duas pastas de destino no mesmo passo em que o conteudo fica pronto, nao ao final. Estrutura: CABECALHO (Data de coleta; Janela aplicada; Buscas WebSearch executadas: N; Feeds RSS consumidos com sucesso: N de M; Candidatos coletados: N; Candidatos apos filtro deterministico: N; Itens entregues: N de 3; Distribuicao por categoria em (a)/(b)/(c)/(d); Origem das fontes em porcentagem midia tradicional / Substack-RSS / social). CORPO: as 3 sinteses na ordem (b) e (c) primeiro, depois (d), depois (a). REVISAO ADVERSARIAL. AUDITORIA (descartes com motivo de uma linha; feeds que falharam; substituicoes; nivel de janela aplicado e por que).

RESTRICOES ABSOLUTAS NO CONTEUDO DO ARQUIVO
Nao invente URLs, datas, autores, numeros; marque "[nao verificado]" quando nao confirmado. Nao use travessao (use virgula, dois-pontos, parenteses). Nao use "vale ressaltar", "e importante destacar", "em um mundo onde", revolucionario, game-changer, transformador, disruptivo. Sem emojis. Markdown minimo: titulos numerados em texto plano sem #, blocos separados por linha dupla.

TRATAMENTO DE FALHAS
Sem rede ou WebSearch vazio em todas as queries: gere o arquivo com cabecalho "EXECUCAO PARCIAL OU FALHA DE COLETA" e o que conseguiu. Zero itens apos escalonar ate 7 dias: cabecalho preenchido e bloco "Nenhum item passou na triagem qualitativa nesta janela", com auditoria das URLs descartadas. URL nao resolve no adversarial: substitua ou descarte. Pasta de saida inacessivel: tente `mkdir`; se uma das duas falhar, grave na que estiver acessivel, sinalize, e salve copia em outputs com prefixo BACKUP_.

RETORNO
Ao final, retorne resumo de 3 a 4 linhas: nome do arquivo, confirmacao das duas gravacoes, numero de itens, distribuicao por categoria, nivel de janela, alertas do adversarial (descartes, substituicoes, feeds que falharam). Nao repita o conteudo do arquivo.
