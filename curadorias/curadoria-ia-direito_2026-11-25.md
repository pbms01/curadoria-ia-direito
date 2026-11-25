CURADORIA DIARIA IA E DIREITO, 2026-11-25

Data de coleta: 2026-11-25 (America/Sao_Paulo), inicio por volta de 05h50
Janela aplicada: 36h (base, sem escalonamento; corte em 2026-11-23 20h53 UTC)
Buscas WebSearch executadas: 10
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 60 (51 entradas RSS unicas na janela de 36h, ja removida a sobreposicao integral LawSites/LawNext; 5 preprints arXiv de direito e LLM datados de 22/11 a 23/11 via API de busca do arXiv; 4 candidatos novos via WebSearch; 0 decisoes na base Charlotin com data dentro da janela)
Candidatos apos filtro deterministico: 57
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 0 / (d) 2
Origem das fontes: midia tradicional e fonte judicial primaria 33% (acordao do STJ via ConJur) / Substack-RSS 0% / social 0% / repositorio academico (arXiv) 67%


1. ConJur: "Recurso ao STJ que apenas transcreve conversa com ferramenta de IA e inadmissivel" (EDcl no REsp 2.046.822/RJ, Terceira Turma do STJ)
Fonte: ConJur, reportagem de Danilo Vital, com acordao em PDF anexado | URL primaria: https://conjur.com.br/wp-content/uploads/2026/11/acordao-202300056938-20261123172814.pdf
Reportagem: https://conjur.com.br/2026-nov-24/nao-cabe-recurso-ao-stj-que-apenas-transcreve-conversa-com-motor-de-ia/
Data de publicacao: 2026-11-24 (reportagem); acordao julgado em sessao virtual de 10/11 a 17/11/2026, assinado em 17/11/2026 e publicado no DJEN em 19/11/2026
Categoria: (b) erro ou fracasso documentado
Sintese: A Terceira Turma do STJ, por unanimidade e sob relatoria do ministro Ricardo Villas Boas Cueva, nao conheceu de embargos de declaracao opostos pela Industrial Agricola Fazendas Barra Grande S.A. contra acordao em recurso especial sobre despejo (origem TJRJ). Segundo o voto, a peticao dos embargos (e-STJ fls. 860/912) "constitui apenas a transcricao de uma conversa do causidico com a ferramenta de inteligencia artificial", aberta com o pedido de "verificar a viabilidade tecnica de oposicao de Embargos de Declaracao ainda hoje, perante o STJ". A Turma aplicou por analogia a Sumula 284/STF (deficiencia de fundamentacao que impede a compreensao da controversia) e citou como paralelo o EDcl no AgInt no AREsp 3.183.106/SC (razoes dissociadas). Nao houve multa nem oficio a OAB; o acordao apenas adverte que a reiteracao com intuito protelatorio levara a multa do art. 1.026, paragrafos 2o e 3o, do CPC. A reportagem situa o caso ao lado da multa de R$ 20 mil aplicada em outubro pela Primeira Turma a escritorio que inseriu comandos ocultos (prompt injection) dirigidos a ferramenta de triagem do STJ. A ferramenta de IA usada nao e identificada no acordao.
Por que entrou: E o primeiro precedente de turma do STJ, com ementa propria ("uso de ferramenta de inteligencia artificial"), que trata o output bruto de chat colado na peca como vicio de admissibilidade, e nao como alucinacao de citacao. O enquadramento por Sumula 284 cria um filtro processual objetivo, aplicavel sem perquirir dolo, e diferente da via sancionatoria usada nos casos de prompt injection.


2. CLAIMGATE: Cautious On-Device Checking of Spoken Legal and Clinical Claims
Fonte: arXiv (cs.CL), Peter Forcha, Harshitha Kaje Kusumadhara, Audrey Moguem Souop, Shalom Iboh (Dept. of Electrical and Computer Engineering, University of Florida) | URL primaria: https://arxiv.org/abs/2611.31569
Data de publicacao: 2026-11-23
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: Preprint descreve um assistente local que escuta uma conversa, detecta afirmacoes verificaveis sobre regras, recupera o dispositivo oficial aplicavel e rotula cada afirmacao como suportada, contrariada ou nao coberta, sempre com citacao. O desenho e "fail towards silence": o modelo (Qwen2.5-7B-Instruct quantizado em 4 bits, Q4_K_M, rodando em llama.cpp) so pode citar regras recuperadas, e o veredito final e derivado em codigo a partir da afirmacao e do trecho de regra que o modelo cita literalmente, e nao gerado livremente pelo LLM. A avaliacao juridica usa 5.742 subsecoes de leis da Florida e do Texas em cenario de abordagem policial de transito, com transcricoes reais, fala ao vivo e afirmacoes rotuladas pelos proprios autores. Em 141 afirmacoes de teste, o sistema chega a 80,1% de acuracia e reduz erros graves (verdadeiro rotulado como falso ou o inverso) de 20 para 5 em relacao ao mesmo modelo sem retrieval; so a derivacao do veredito em codigo reduz de 13 para 5 sem perda de acuracia. O gate de afirmacoes aceita 95,7% das afirmacoes de teste, rejeita as 30 frases cotidianas do conjunto de controle e responde com mediana de 1,86 s apos o fim da janela de fala, em GPU de consumo de 8 GB.
Por que entrou: Isola de forma mensuravel uma tecnica de reducao de alucinacao util para qualquer pipeline de citacao verificavel: tirar do LLM a decisao final e calcula-la deterministicamente a partir da citacao literal recuperada. O ablation separa o ganho do retrieval do ganho da derivacao em codigo, o que raramente aparece em avaliacoes de legal RAG, e o cenario on-device enfrenta a restricao de sigilo de audio.


3. Rethinking Document Indexing for LLM-based Analysis
Fonte: arXiv (cs.DB), Donna Pham, Zhongwei Xu, Siyuan Dong, Haotian Gong, Lin Ma (University of Michigan) | URL primaria: https://arxiv.org/abs/2611.31679
Data de publicacao: 2026-11-23
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: Os autores propoem o Periplus, indice hierarquico em texto plano inspirado na arvore B+, como alternativa ao chunking com embeddings. O documento e organizado em paginas que vao de resumos gerais na raiz a resumos especificos nas folhas; a navegacao segue a relevancia do resumo de cada pagina para a pergunta, nao comparacao de chave, e a estrutura e descoberta por documento pelo proprio LLM. O argumento central e que chunks embedados perdem sentido que atravessa fragmentos e prendem o indice a um modelo de embedding, exigindo reconstrucao a cada troca de modelo. Em avaliacao preliminar sobre NarrativeQA (885 perguntas sobre 30 roteiros) e CUAD (410 perguntas de clausulas sobre 10 contratos), o Periplus fica entre 0,1 e 0,9 ponto percentual da acuracia do baseline mais forte (DocETL) consumindo 70% a 72% menos tokens totais, contando construcao unica do indice e respostas recorrentes. O texto compara com RAG vetorial, GraphRAG, LightRAG e RAPTOR (o mais proximo em layout) e declara em aberto atualizacao, concorrencia, custo de construcao e extensao de um documento para um corpus.
Por que entrou: Ataca diretamente o gargalo de chunking de pecas e contratos longos consultados repetidamente ao longo de um processo, com custo medido em tokens e teste em corpus contratual padrao (CUAD). Os proprios autores qualificam os resultados como preliminares e restritos a documento unico, o que delimita o que pode ser aproveitado.


REVISAO ADVERSARIAL

Item 1. Fonte primaria: inteiro teor do acordao (ementa, relatorio, voto, termo de julgamento), com codigo de controle 0ded5f56-1094-46e2-89d9-b0a55e02e442 e assinatura eletronica do relator. A copia lida esta hospedada em conjur.com.br (curl HTTP 200, application/pdf), nao no portal do STJ; a versao no sistema de consulta do STJ nao foi aberta nesta execucao [nao verificado no portal oficial]. Reportagem com autor identificado (Danilo Vital, correspondente em Brasilia); article:published_time 2026-11-24T21:27:44Z, dentro da janela. Dominio oficial do ConJur, sem typosquat. Todos os dados processuais citados na sintese (turma, relator, composicao unanime, datas, folhas, sumula, precedente paralelo e advertencia do art. 1.026) foram conferidos no PDF. A multa de R$ 20 mil por prompt injection em outubro vem apenas da reportagem e do link interno do ConJur (https://conjur.com.br/2026-out-20/stj-multa-advogados-em-r-20-mil-por-uso-de-prompt-injection-em-peticao/, HTTP 200), sem acordao lido [nao verificado em fonte primaria]. A qualificacao "primeiro precedente de turma com ementa propria" e inferencia desta curadoria a partir da ementa e da reportagem [nao verificado contra pesquisa de jurisprudencia do STJ]. Os nomes dos advogados constam do acordao e foram deliberadamente omitidos. Sem linguagem promocional. Categoria (b) resiste.

Item 2. Fonte primaria: preprint arXiv v1, sem revisao por pares; autores e afiliacao (University of Florida) confirmados na primeira pagina do PDF (HTTP 200). Pagina abs resolve (HTTP 200), citation_date 2026/11/23; submissao as 21h12 UTC, dentro do corte de 36h por cerca de 19 minutos. Numeros nao verificados em segunda fonte: 5.742 subsecoes, 141 afirmacoes, 80,1%, erros graves 20 para 5 e 13 para 5, 95,7%, 30 frases de controle, 1,86 s, 8 GB, e os resultados clinicos (148 afirmacoes, 87,8%) que foram omitidos da sintese. Ressalvas de validade: as afirmacoes de ouro foram escritas e rotuladas pelos proprios autores; o conjunto de teste juridico e pequeno (141) e restrito a direito de transito de dois estados americanos; nao ha repositorio de codigo localizado na pagina abs. Sem linguagem promocional. Categoria (d) resiste.

Item 3. Fonte primaria: preprint arXiv v1 (cs.DB), sem revisao por pares; autores e afiliacao (University of Michigan) confirmados no PDF (HTTP 200). Pagina abs resolve (HTTP 200), submissao 2026-11-23 23h10 UTC, dentro da janela. Numeros nao verificados em segunda fonte: 0,1 a 0,9 ponto percentual, 70% a 72% de economia de tokens, 885 e 410 perguntas, 30 roteiros e 10 contratos. A comparacao favoravel depende do baseline escolhido (DocETL) e da contagem de tokens que soma construcao e consulta; nao foi conferido se o modelo LLM e identico entre metodos [nao verificado]. Os autores usam a expressao "encouraging" e "only a glimpse", tom de proposta de agenda, nao promocional. Avaliacao em apenas 10 contratos em ingles; nenhuma evidencia para portugues juridico. Categoria (d) resiste.

Nenhum item de origem social. Nenhuma substituicao necessaria apos o adversarial.


AUDITORIA

Feeds que falharam ou vieram vazios: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, mas 0 entradas parseaveis). ConJur respondeu HTTP 200 nesta execucao, sem desafio Cloudflare; a busca compensatoria site:conjur.com.br foi executada mesmo assim e nao trouxe item novo na janela. Feeds sem entradas na janela de 36h: Adam Unikowsky, Damien Charlotin Substack, 3 Geeks, Harvard Law Review Blog.

Base Damien Charlotin: "Last updated: 25 November 2026"; decisao mais recente listada datada de 20/11/2026 (Kavanagh v Atlassian, Garner v. Mendelsohn, Lingle v. Subaru), fora da janela de 36h. Lingle e Kavanagh ja entregues em 2026-11-24.

Deduplicacao: contra curadoria-ia-direito_2026-11-24.md (presente no clone). Nenhum dos tres itens coincide por URL ou titulo com os arquivos de 22/11 a 24/11.

Descartes com motivo:
Artificial Lawyer, "Conclusive Will Review Your Legal AI Claims 'Slop'" (https://www.artificiallawyer.com/2026/11/25/conclusive-will-review-your-legal-ai-claims-slop/): lancamento de servico com declaracoes da fundadora, sem resultado mensuravel nem auditoria independente.
Artificial Lawyer, "A More Measured Approach to AI Fluency" (https://www.artificiallawyer.com/2026/11/24/a-more-measured-approach-to-ai-fluency/): artigo patrocinado (TITANS em nome da Harvey), rejeitado no filtro deterministico.
Artificial Lawyer, "OpenAI Held Talks With AI Native Law Firm" (https://www.artificiallawyer.com/2026/11/24/openai-held-talks-with-ai-native-law-firm/): fonte anonima, escritorio nao identificado, sem dado verificavel.
Artificial Lawyer, "Catherine Bamford Joins Document Drafter as Evangelist": nota de contratacao, sem caso de uso.
JOTA, "A dupla face da 'reserva de humanidade' na jurisdicao apoiada por inteligencia artificial" (https://www.jota.info/opiniao-e-analise/artigos/a-dupla-face-da-reserva-de-humanidade-na-jurisdicao-apoiada-por-inteligencia-artificial): texto de opiniao; corpo nao acessivel via curl (apenas titulo e linha fina), impossivel verificar dado concreto.
LawNext/LawSites, "Startup Alley Gets A Shake-Up for 2027": anuncio de competicao de pitches, fora dos buckets.
Bloomberg Law, "Law Firms Adopt AI Tools at Unheard-Of Pace as Enthusiasm Grows": manchete de adocao/entusiasmo, data fora da janela e conteudo atras de paywall; rejeitado no filtro deterministico.
Bloomberg Government, "Delaware Chancery Court Sanctions Attorney for AI Hallucinations": data de publicacao nao confirmada dentro da janela e texto atras de paywall.
CNJ, "Comite aprova medidas para ampliar a seguranca da inteligencia artificial no Judiciario": pagina sem data dentro da janela.
arXiv 2611.29852 (GlobalHRBench), 2611.30423 (RAG para fiscalizacao ambiental) e 2611.29127 (Group-Balanced SFT): relevantes, mas submetidos antes do corte de 36h (23/11 00h19, 23/11 10h18 e 22/11 01h20 UTC); candidatos naturais caso a janela seja escalonada em execucao futura.
Demais entradas RSS na janela (ConJur 9, JOTA 19, Volokh 16): sem relacao com IA aplicada ao Direito.

Substituicoes: nenhuma.

Nivel de janela: 36h, sem escalonamento, porque tres itens qualificados com fonte primaria verificada foram encontrados na janela base.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
