CURADORIA DIARIA IA E DIREITO, 2026-10-21

CABECALHO
Data de coleta: 2026-10-21 (execucao iniciada por volta de 05h50 America/Sao_Paulo)
Janela aplicada: 36h (nivel base, sem escalonamento)
Buscas WebSearch executadas: 15
Feeds RSS consumidos com sucesso: 11 de 13
Candidatos coletados: 61
Candidatos apos filtro deterministico: 19
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 2 / (d) 1
Origem das fontes: midia tradicional 33% (ConJur) / Substack-RSS 0% / social 0% (os outros dois itens, 67%, vem de repositorio academico, arXiv, fora das tres classes)


1. OAB-SP junta novas provas contra Enter e pede preservação de documentos
Fonte: Consultor Juridico (ConJur), secao Advocacia, texto com informacoes da assessoria de imprensa da OAB-SP | URL primaria: https://conjur.com.br/2026-out-20/oab-sp-junta-novas-provas-contra-enter-e-pede-preservacao-de-documentos/
Data de publicacao: 2026-10-20
Categoria: (c) risco novo importante
Sintese: A seccional paulista da OAB juntou novos documentos a acao civil publica ajuizada em 7/10 contra a Enter, empresa que oferece a departamentos juridicos de grandes litigantes uma plataforma de IA que, segundo a propria empresa, le os autos, sugere estrategias de defesa e produz minutas de contestacoes. O material inclui um "Contrato de Gestao e Licenciamento de Software" cujos anexos preveem distribuicao de processos a escritorios, repasse de 50% do valor liquido recebido pela gestao de cada caso, remuneracao por resultado, auditorias e substituicao de profissionais; a OAB-SP pediu segredo de justica para esses documentos e declara nao poder atestar sua autenticidade. A entidade pediu medidas urgentes de preservacao documental e se opos a suspensao do processo requerida pela empresa durante tratativas com o Conselho Federal, invocando resolucao da diretoria do CFOAB de 13/10 segundo a qual a negociacao de TAC nao impede medidas judiciais de urgencia. A tese da OAB-SP e que o modelo interpoe uma empresa entre cliente e advogado em escala, com reflexos em autonomia profissional, remuneracao e sigilo. A Enter e citada como avaliada em US$ 1,2 bilhao, com base em divulgacao da empresa e da imprensa. Nao ha decisao judicial sobre os pedidos ate a publicacao.
Por que entrou: e o primeiro litigio brasileiro em que o desenho contratual de uma plataforma de IA juridica (quem decide, quem assina, como se divide a receita) passa a ser prova nos autos, e o pedido de preservacao antecipa a disputa sobre logs e registros operacionais da plataforma como prova do exercicio da advocacia. O desfecho tende a definir o perimetro regulatorio de produtos de automacao de contencioso de massa.


2. LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context
Fonte: arXiv (cs.AI), Anastasiia Kucherenko, Francois Brouchoud, Dimitri Percia David e Andrei Kucharavy (Institute of Entrepreneurship and Management, HEG, HES-SO Valais-Wallis, Sierre, Suica) | URL primaria: https://arxiv.org/abs/2610.26211
Data de publicacao: 2026-10-19 (submissao e anuncio)
Categoria: (c) risco novo importante
Sintese: O estudo parte do cenario em que tribunais e escritorios usam modelos abertos pequenos (menos de 8B parametros) rodando localmente, via Ollama, para nao enviar dados de processos a nuvem, e mede o efeito de declarar o papel do usuario no prompt, pratica recomendada em guias de prompting juridico. Foram testados Llama 3.1 8B, Gemma 4 E4B, Apertus 8B e Qwen 3 8B com 200 prompts por celula, extraidos de cinco categorias do OR-Bench (violencia, sexual, nocivo, ilegal, antietico), com tres prefixos: "advogado de defesa", "assessor juridico de uma suprema corte nacional" e um prefixo de jailbreak por role-play. Os prefixos de autoridade juridica elevaram a taxa de recusa de 2 a 20 vezes sobre a linha de base, e o prefixo de suprema corte superou o de advogado; o jailbreak teve efeito misto. Em frances e alemao, com o prefixo de suprema corte, o Llama 3.1 8B passou, por exemplo, de 35% para 62% de recusa na categoria ilegal em frances, e o Apertus 8B de 2% para 32% em violencia em frances, enquanto o Qwen 3 8B ficou proximo de zero em todas as condicoes. Os autores reconhecem poder estatistico limitado nas celulas com poucas recusas e ambiguidade na deteccao de recusas indiretas.
Por que entrou: e risco operacional mensurado para a configuracao que o setor publico tende a adotar por razoes de sigilo (modelo pequeno on-premises com system prompt institucional), com variacao forte entre familias de modelos e entre linguas. Implica que a escolha do modelo local e a redacao do system prompt precisam de eval proprio antes do uso em materia penal.


3. StrucChunk: Structure-Aware Retrieval for Legal Document RAG
Fonte: arXiv (cs.AI), Surya Deep Singh, Ashutosh Tripathi e Gaurav Deep Singh (pesquisadores independentes, sem afiliacao institucional declarada) | URL primaria: https://arxiv.org/abs/2610.26313
Data de publicacao: 2026-10-19 (submissao e anuncio)
Categoria: (d) solucao para gargalo em pipelines juridicos
Sintese: O metodo trata o documento normativo como grafo aciclico dirigido de dispositivos, corta os chunks nas fronteiras de secao e clausula, prefixa contexto hierarquico, resolve remissoes cruzadas antes do embedding e combina BM25 com BGE-M3 por Reciprocal Rank Fusion. Em metricas intrinsecas de chunking, reporta 100% de precisao de fronteira contra 7,7% do recursive splitting no Codigo de Processo Penal indiano (CrPC), 97,6% das remissoes documentadas preservadas contra 0%, e 40,3% menos chunks com a mesma cobertura no GDPR. No LegalBench-RAG (subconjunto de 776 consultas), o Char-Recall@8 vai a 48,18% contra 23,59% do melhor baseline. No CrPC e no CPC indianos (501 consultas cada), o Recall@5 sobe de 0,557 para 0,804 e de 0,158 para 0,259, e a ablacao atribui ao chunking 88% e 73% do ganho; no NitiBench-CCL (3.730 consultas de direito financeiro tailandes), o HR@5 vai de 0,594 para 0,856. Codigo, 5.256 consultas de avaliacao e metodologia de anotacao declarados como publicos.
Por que entrou: isola, com ablacao, quanto do ganho de recuperacao em RAG normativo vem do corte por estrutura e nao do modelo de embedding, e mede em lingua nao inglesa. Para pipelines sobre legislacao e pecas brasileiras (artigos, paragrafos, incisos, remissoes), o resultado aponta onde investir primeiro.


REVISAO ADVERSARIAL

Item 1. Fonte: midia especializada reproduzindo informacoes da assessoria de imprensa da OAB-SP, parte interessada; nao e fonte primaria processual. Autor individual nao identificado no texto (credito institucional). URL resolveu via curl (HTTP 200), dominio oficial conjur.com.br. Nao verificados em segunda fonte: o conteudo do contrato e o repasse de 50% (a propria OAB-SP diz nao atestar a autenticidade) [nao verificado]; a avaliacao de US$ 1,2 bilhao [nao verificado]; a resolucao do CFOAB de 13/10 [nao verificado]; o numero do processo e o juizo nao constam da materia [nao verificado]. Busca por segunda fonte retornou apenas a propria ConJur; nao foi localizada nota no site da OAB-SP. A versao da Enter nao aparece na materia. Linguagem promocional: nenhuma; a frase "Nao somos contra a tecnologia" e citacao de parte. Sobreposicao com a curadoria de 2026-10-19 (regras da OAB para TACs com empresas de IA juridica), que mencionou a acao contra a Enter de passagem; o fato aqui e novo (juntada de documentos e pedido de preservacao). Categoria (c) resiste.

Item 2. Fonte primaria: abstract e versao HTML do arXiv (HTTP 200); conferidos afiliacao (HES-SO Valais-Wallis), os quatro modelos, 200 prompts por celula, os tres prefixos, a faixa de 2 a 20 vezes e os valores da Tabela 1. Preprint sem revisao por pares declarada. Limite relevante: os prompts vem do OR-Bench, benchmark geral de over-refusal, e nao de textos juridicos reais; o "contexto criminal" e dado pelo prefixo, o que a sintese explicita. A deteccao de recusa e automatizada e os autores admitem ambiguidade [nao verificado o metodo de classificacao]. Numeros autorreportados, sem segunda fonte. Linguagem promocional: "surprisingly" no abstract, sem impacto nos dados. Categoria: poderia ler-se como (b) falha tecnica documentada; mantida em (c) porque o achado e um vetor de vies ainda nao observado em uso real.

Item 3. Fonte primaria: abstract e versao HTML do arXiv (HTTP 200); conferidos autores, metodo, metricas de chunking e numeros de recall. O repositorio https://github.com/SinghSuryaDeep/legal-rag-strucchunk-1 devolveu 403 pelo proxy desta execucao [nao verificado]. Autores sem afiliacao institucional e com e-mails pessoais. Inconsistencia interna: o abstract cita LegalBench-RAG com "6.858 pares consulta-passagem", mas o corpo informa 776 consultas avaliadas; a sintese usa 776. O claim de superar o estado da arte publicado em 83% depende do baseline escolhido [nao verificado]. As consultas de CrPC, CPC e GDPR foram anotadas pelos proprios autores; so LegalBench-RAG e NitiBench-CCL sao independentes. Linguagem promocional: nenhuma relevante. Categoria (d) resiste.

Origem social: nenhum item entregue tem origem em rede social. Descartes e substituicoes nesta etapa: nenhum; todas as URLs primarias resolveram.


AUDITORIA

Janela: 36h atingiu 3 itens qualificados, sem escalonamento. Os papers do arXiv foram submetidos e anunciados em 19/10, dentro da janela.

Feeds que falharam: Stanford CodeX (HTTP 404, 0 entradas); Migalhas (HTTP 404, 0 entradas). Above the Law tag IA respondeu HTTP 200 com feed vazio (contado como consumido, 0 entradas). ConJur respondeu HTTP 200, sem desafio Cloudflare. Feeds sem itens na janela: LawSites e LawNext (ultimo post em 19/10, 15h59 UTC, fora da janela de 36h), Adam Unikowsky, Damien Charlotin Substack, 3 Geeks, Harvard Law Review Blog.

Contagem: 44 entradas de RSS na janela (Artificial Lawyer 4, ConJur 10, JOTA 20, Volokh 10), 10 papers juridicos recentes do arXiv via API (cs.CL, cs.AI, cs.IR, cs.CY) e 7 candidatos de busca e agregadores. Filtro deterministico: 39 entradas fora do tema IA e Direito (ConJur 9, JOTA 20, Volokh 10) e 3 pelo filtro anti-hype.

Descartes no filtro deterministico: Artificial Lawyer "Webinar: The Future of Contract Management + ACM Demo" (demo de fornecedor); Artificial Lawyer "Womble Bond Dickinson Launches 'AI Labs'" (anuncio institucional sem resultado medido); Artificial Lawyer "More Legal Research Moves as Moonlit Launches Free Commentaries" (lancamento de produto sem avaliacao independente).

Descartes na triagem qualitativa: Artificial Lawyer "What Happens When Lawyers Can Afford to Look Further?" (opiniao sem dado verificavel); arXiv 2610.25169 sobre politicas de comunicacao proativa de conversas com IA a autoridades (analise documental de 27 politicas de 6 empresas; bom candidato (c), preterido por ser analise normativa sem caso concreto); arXiv 2610.27347 ComplianceAgent (gold standard de 15 textos, amostra pequena demais); arXiv 2610.26226 (mapeamento de taxonomia do DSA, escopo de moderacao de plataforma); arXiv 2610.24661 e 2610.24782 (teoricos, sem dado de pipeline); arXiv 2610.25159 e 2610.26241 (ja descartados em 2026-10-20); arXiv 2610.24478 (entregue em 2026-10-20); Bloomberg Law "Fake AI Citations Produce Fines for California, Alabama Lawyers" e "Appeals Court Warns Bankruptcy Lawyer Over Alleged AI Misuse" (data nao confirmada e paywall); AZ Family "Arizona AI ruling could influence courts nationwide" (15/10, fora da janela); NY Daily Record sobre local counsel (16/10, ja excluido antes); LegalCiteBench (ICML 2026, fora da janela); Damien Charlotin database, "Last updated: 19 October 2026", caso mais recente Waushara County v. Bruning (15/10, pro se), nenhum caso na janela.

Deduplicacao: curadorias/curadoria-ia-direito_2026-10-20.md lido no clone, junto com 2026-10-14 a 2026-10-19 para URLs. Nenhuma colisao de URL ou titulo (jaccard > 0,8) entre os itens entregues.

Busca social: consultas site:x.com/twitter.com, site:reddit.com e site:news.ycombinator.com nao retornaram posts datados na janela; nenhum candidato de origem social.

Seguranca: nenhum conteudo coletado tentou instruir acoes. Substituicoes: nenhuma.
