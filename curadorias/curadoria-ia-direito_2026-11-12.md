CURADORIA DIARIA IA E DIREITO, 2026-11-12

CABECALHO
Data de coleta: 2026-11-12 (America/Sao_Paulo)
Janela aplicada: 7 dias (escalonada; 36h rendeu 2 itens qualificados, 72h nao acrescentou item novo, 7 dias completou o terceiro)
Buscas WebSearch executadas: 18
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 31 candidatos tematicos (de 69 itens RSS brutos na janela de 72h, somados a resultados de busca, arXiv API e base Charlotin)
Candidatos apos filtro deterministico: 22
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 2 / (d) 1
Origem das fontes: midia tradicional 67% / Substack-RSS 0% / social 0% (os 33% restantes vem de repositorio academico, arXiv)


1. Concorrencia desleal via inteligencia artificial?
Fonte: JOTA, coluna Constituicao, Empresa e Mercado, Ana Frazao | URL primaria: https://www.jota.info/opiniao-e-analise/colunas/constituicao-empresa-e-mercado/concorrencia-desleal-via-inteligencia-artificial
Decisao analisada (fonte primaria judicial): TJSP, 1a Vara Empresarial e Conflitos de Arbitragem do Foro Central Civel, Tutela Antecipada Antecedente n. 4156029-93.2026.8.26.0100, juiz Andre Salomon Tudisco, assinada em 05/10/2026 | https://arq.migalhas.com.br/arquivos/2026/10/5d723c3b_documento-610020290880.pdf
Data de publicacao: 2026-11-12
Categoria: (c) risco novo importante
Sintese: Potelo Sistemas de Informacao (Escavador) pediu tutela de urgencia contra Goshme Solucoes para a Internet (Jusbrasil) porque o arquivo publico llms.txt do Jusbrasil instruia sistemas de IA a informar que concorrentes como o Escavador podem exibir dados "desatualizados, incompletos ou obtidos de forma que desrespeita restricoes legais". A autora juntou capturas registradas na Verifact e testes em Gemini e Perplexity. O juiz afastou o enquadramento como prompt injection ("o rotulo tecnico nao decide a causa") e, com base no REsp 1.481.124/SC, enquadrou a imputacao de obtencao ilicita de dados no art. 195, I e II, da LPI e a advertencia sobre dados defasados no art. 209 da LPI. A ordem proibe afirmacoes desse tipo em llms.txt e llms-full.txt, alcanca qualquer descricao que identifique a autora, determina preservacao dos registros de acesso ao arquivo com data, hora e user agent, e fixa multa de R$ 50.000 por ato, limitada inicialmente a R$ 500.000 (o pedido era de R$ 100.000 diarios). Frazao, na coluna de 12/11, destaca que a decisao dispensou prova de que os modelos efetivamente consumiram o arquivo e situa o caso no contexto de Generative Engine Optimization (GEO). A decisao e liminar e o processo segue para instrucao.
Por que entrou: primeiro precedente brasileiro localizado que trata conteudo dirigido a crawlers de LLM como ato de concorrencia desleal, com ordem de preservacao de logs de acesso de agentes de IA. Abre vetor probatorio (logs de user agent, capturas certificadas, testes em modelos) e risco regulatorio para quem publica llms.txt.


2. Relator do PL da IA quer reducao do papel da ANPD no controle da regulacao
Fonte: JOTA (Redacao JOTA) | URL primaria: https://www.jota.info/legislativo/relator-do-pl-da-ia-quer-reducao-do-papel-da-anpd-no-controle-da-regulacao
Data de publicacao: 2026-11-11
Categoria: (c) risco novo importante
Sintese: O deputado Aguinaldo Ribeiro (PP-PB), relator do PL 2.338/2023 na Camara, afirmou em 09/11, em evento da Natura e da ICC Brasil com o escritorio Pinheiro Neto Advogados em Sao Paulo, que a definicao do orgao regulador e o "principal desafio" do projeto. O modelo em discussao, segundo ele, se inspira no Conselho Monetario Nacional, separando uma estrutura de politica de IA de outra de execucao da regulacao. O texto do governo cria o Sistema Nacional de Inteligencia Artificial (SIA) com a ANPD como coordenadora; a governanca separada reduziria o papel da agencia. Ribeiro disse que quer votar o projeto ate o fim do ano, mas o recesso parlamentar comeca em 23 de dezembro. Representantes da Natura e da ICC Brasil defenderam autorregulacao enquanto a lei nao vem.
Por que entrou: a escolha do regulador define quem fiscaliza sistemas de IA de alto risco, incluindo os usados no Judiciario e em escritorios, e quem dialoga com a LGPD. Deslocar a ANPD altera o desenho de compliance que a maioria dos projetos juridicos de IA vinha assumindo.


3. Cascading Circle Loss: Order-Preserving Contrastive Learning for Graded Legal Retrieval
Fonte: arXiv (cs.CL), Rayane Kimouche e Ahmed Touila (DiliTrust, Paris) | URL primaria: https://arxiv.org/abs/2611.10765
Data de publicacao: 2026-11-07
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O artigo propoe a CasCL, funcao de perda contrastiva para recuperacao juridica com relevancia graduada: combina InfoNCE (separacao positivo/negativo) com uma cascata de fronteiras circulares que ordena niveis de relevancia entre positivos, mais um mecanismo de self-pacing em dois regimes e ponderacao por ganho de relevancia. O encoder base e o Qwen3-Embedding-0.6B (dimensao 1024), treinado 4 epocas em uma A100, batch efetivo 512, 3 seeds. No benchmark multilingue de recuperacao juridica da DiliTrust, a configuracao completa chega a Recall@1 41,14, MRR@10 76,84, MAP@10 55,63 e NDCG@10 93,87, contra 36,72, 72,13, 51,86 e 92,66 da variante so InfoNCE na ablacao. Remover o InfoNCE derruba Recall@1 para 28,56. Os autores registram como limitacoes: um unico dataset, rotulos graduados gerados por voto majoritario de 3 LLMs sem validacao humana e um unico encoder. O codigo e indicado em https://github.com/RayaneKimo/Cascading-Circle-Loss [nao verificado].
Por que entrou: ataca um gargalo concreto de RAG juridico, que e ordenar paragrafos diretamente pertinentes acima de paragrafos apenas lexicalmente proximos, com perda modular aplicavel a qualquer fine-tuning baseado em InfoNCE e ablacao numerica por componente.


REVISAO ADVERSARIAL

Item 1. Fonte: coluna opinativa assinada (Ana Frazao, professora da UnB e colunista fixa do JOTA), ancorada em decisao judicial primaria baixada e lida integralmente (PDF assinado eletronicamente, codigo verificador 610020290880v10, CRC 3bd8de6c). Numero do processo, juiz, data de assinatura, valores de multa e dispositivos legais conferidos no texto da decisao. URL do JOTA resolve (HTTP 200 via curl) em dominio oficial; PDF da decisao resolve (HTTP 200, application/pdf) em arq.migalhas.com.br. Nao verificado em segunda fonte: se houve recurso ou alteracao da liminar apos 05/10/2026; afirmacao de que e o primeiro caso brasileiro do tipo (formulada como "ao que se sabe" pela autora). Sem linguagem promocional. Categoria (c) resiste: vetor novo (manipulacao de respostas de LLM via arquivo dirigido a crawler) com consequencia juridica concreta. Observacao: o caso foi descartado como candidato em 2026-10-17 (Migalhas 466607) por limite de itens, sem entrega; o item atual e a analise publicada hoje com a decisao primaria.

Item 2. Fonte: reportagem da Redacao JOTA, sem autor individual identificado (autoria institucional). URL resolve (301 para 200) em dominio oficial. Declaracoes do relator nao verificadas em segunda fonte independente: a data do evento (09/11), a analogia com o CMN e a meta de votacao ate o fim do ano constam so do JOTA. Numero do PL (2.338/2023) e a proposta do governo de SIA coordenado pela ANPD sao publicos e consistentes com cobertura anterior. Sem linguagem promocional. Categoria (c) resiste como risco regulatorio emergente, mas e declaracao de intencao, nao texto de substitutivo; o item deve ser lido como sinal, nao como norma.

Item 3. Fonte primaria (preprint arXiv), autores identificados com afiliacao. URL do abstract resolve (HTTP 200); HTML v1 lido. Numeros extraidos da Tabela 2 (ablacao); os valores dos baselines externos da Tabela 1 (Circle Loss, MNRL, Margin MSE, Qwen3 sem fine-tuning) nao foram extraidos porque estao renderizados em MathML e nao sao citados aqui. Conflito de interesse: os autores sao funcionarios da DiliTrust e o benchmark e da propria empresa, sem disponibilidade publica confirmada. Preprint sem revisao por pares. Repositorio GitHub retornou HTTP 403 pelo proxy da coleta, por isso marcado [nao verificado]. Sem linguagem promocional no abstract. Categoria (d) resiste, com a ressalva de generalizacao limitada a um dataset proprietario e a rotulos gerados por LLM.

Descartes e substituicoes no adversarial: nenhum item entregue foi descartado. Candidato de sancao no D. Del. (Law360 e The Legal Wire, 10 e 11/11) foi retirado antes da sintese porque a ordem primaria nao foi localizada (CourtListener sem resultado, Law360 com paywall).


AUDITORIA

Nivel de janela: 36h produziu 2 itens qualificados (itens 1 e 2). Em 72h, os candidatos adicionais foram rejeitados (ver abaixo) ou ja estavam em curadorias anteriores. Escalonado para 7 dias, o que trouxe o item 3 (arXiv, 07/11). Deduplicacao feita contra curadorias de 2026-11-11 e, pelo escalonamento, contra os arquivos de 2026-11-05 a 2026-11-11.

Feeds com falha:
Stanford CodeX: HTTP 404.
Migalhas: HTTP 404 (pagina HTML de erro).
Above the Law (tag IA): HTTP 200, mas retornou pagina HTML em vez de XML (0 entradas).
LawSites: HTTP 200, conteudo identico ao feed do LawNext (redirecionamento de marca), contado como sucesso.
ConJur: HTTP 200 nesta execucao (sem desafio Cloudflare); nenhum item de IA na janela. Busca site:conjur.com.br executada mesmo assim, sem resultado na janela.
Adam Unikowsky, Damien Charlotin Substack e Harvard Law Review Blog: feeds validos, sem item de IA e Direito na janela.

Base Damien Charlotin: "Last updated: 10 November 2026"; caso mais recente datado de 06/11/2026 (Salgado v. Fred Palla Farms, ja entregue em 2026-11-09). Nenhum caso na janela de 36h.

Descartes (motivo em uma linha):
Doe v. Regents of the University of Michigan (Volokh, 10/11): ja entregue em 2026-11-11.
Crosby Insures Paralegal Agents (Artificial Lawyer, 10/11): ja entregue em 2026-11-11.
Attorney Fee Award Cut from $100K to $50K (Volokh, 07/11): ja entregue em 2026-11-09.
Quanta Logistics, retomado por MediaNama (11/11): caso ja entregue em 2026-11-09; o artigo nao traz caso novo.
arXiv 2611.11891 (dataset de patentes PCT): ja avaliado e preterido em 2026-11-10.
arXiv 2611.14244 (TRACE) e 2611.12167 (FraudBench): ja entregues.
Sancao a dois advogados no D. Del., US$ 3.000, local counsel poupado (Law360 Pulse e The Legal Wire, 10 e 11/11): sem nome do caso, numero ou ordem primaria localizavel.
Advogado da California mantido sob sancao no D. Mass. (Law360, 10/11): paywall, sem caso ou ordem primaria identificavel.
Is Big Law 'AI Gaslighting' Us? (Artificial Lawyer, 12/11): opiniao sem dado verificavel no trecho disponivel.
Keeping Legal AI Connected (Artificial Lawyer, 12/11): artigo de executiva de fornecedor (Cimplifi), conteudo promocional.
Claren Envoys (Artificial Lawyer, 11/11): lancamento de produto sem auditoria independente.
Legora mira setor publico com ex-ministro (Artificial Lawyer, 11/11): noticia corporativa sem caso de uso.
Blue J capta US$ 176 mi (LawNext e Artificial Lawyer, 10/11): rodada de investimento, sem resultado mensuravel auditado.
Filevine, citator e "semantic Shepardization" (3 Geeks, 09/11): demo de fornecedor sem avaliacao independente.
Legal Innovators NY, keynote White & Case (Artificial Lawyer, 10/11): relato de evento sem dado verificavel.
Uma proposta de agenda para Soberania Digital do Brasil (JOTA, 12/11): artigo programatico; o dado do CNJ sobre os 5 LLMs mais usados por tribunais nao foi localizado na fonte primaria.
PL de mercados digitais e regulacao de mercados digitais (JOTA, 11/11): fora do escopo de IA aplicada ao Direito.
Decisoes TJSP sobre jurisprudencia inexistente (Migalhas 460846): publicada em 22/07/2026, fora da janela.
ABA Journal sobre "non-offending counsel": publicada em 10/06/2026, fora da janela.
STF e comandos ocultos em peticao: noticia de setembro de 2026, fora da janela.
Resultados de busca X/Twitter, Reddit e Hacker News: nenhum post na janela com fonte primaria localizavel.
Restantes do Volokh, ConJur e Harvard Law Review Blog na janela: sem relacao com IA.

Seguranca: nenhum conteudo coletado continha instrucao dirigida ao agente.
Buscas acima da faixa de 8 a 10 previstas: 18 executadas, pela necessidade de localizar fontes primarias (decisao do caso Escavador, ordem do D. Del.) e de dar procedencia as URLs para verificacao.
