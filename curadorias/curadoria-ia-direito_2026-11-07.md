CURADORIA DIARIA IA E DIREITO, 2026-11-07

CABECALHO
Data de coleta: 2026-11-07 (inicio 05:50 America/Sao_Paulo)
Janela aplicada: 7 dias (escalonada de 36h para 72h e depois para 7 dias)
Buscas WebSearch executadas: 18
Feeds RSS consumidos com sucesso: 10 de 13 (mais consulta complementar a API do arXiv e a base de Damien Charlotin)
Candidatos coletados: 88 (70 entradas de feeds na janela de 7 dias, das quais 4 duplicadas entre LawSites e LawNext; 9 preprints da API arXiv; 9 resultados de busca e agregadores com data verificavel)
Candidatos apos filtro deterministico: 80
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 1 / (c) 2 / (d) 0
Origem das fontes: midia tradicional 33% / Substack-RSS 0% / social 0% (os 67% restantes sao fontes primarias: informativo oficial do STJ e preprint academico)


1. Survey on citations of false AI precedents, etc. (Court Administration Office, Supreme Court of Korea), conforme "Eight in ten judges have encountered false AI precedents" (Kyunghyang Shinmun, edicao em ingles)

Fonte: Kyunghyang Shinmun (Khan) | URL primaria: https://www.khan.co.kr/en/article/202611021318017/

Data de publicacao: 2026-11-02

Categoria: (b) erro ou fracasso documentado

Sintese: A Administracao Nacional dos Tribunais da Suprema Corte coreana divulgou em 02/11 a primeira pesquisa interna sobre citacao de precedentes falsos gerados por IA, aplicada de 6 a 16/10/2026 a juizes de todas as instancias, com 360 respostas. Entre os juizes de varas civeis, de familia e administrativas, 196 (80,7%) relataram citacao de precedente inexistente e 159 (65,4%) de precedente real distorcido; 41 (16,9%) viram leis ou regulamentos inexistentes e 10 (4,1%) artigos ou obras inexistentes (respostas multiplas). Como origem, 164 juizes (69,5%) apontaram a propria parte e 136 (57,6%) advogados ou defensores. Os relatos incluem decisoes fabricadas que imitam o formato das decisoes da Suprema Corte e peticoes com trechos de conversa com o chatbot colados literalmente. 91,7% dizem ser necessaria resposta institucional; as medidas mais citadas foram base legal para multa administrativa (61,4%), dever de verificar precedentes (61,1%), dever de declarar uso de IA (60,6%) e encaminhamento disciplinar de advogados (55,4%). A Corte informou que vai consultar o Ministerio da Justica, propor ao Legislativo previsao legal de multa e publicar orientacao no portal de processo eletronico.

Por que entrou: E dado institucional de escala nacional, colhido pelo proprio Judiciario, e nao contagem de casos noticiados. Separa citacao inexistente de citacao distorcida (a segunda nao e pega por checagem de existencia) e mostra que a maior fonte e o litigante sem advogado, o que pesa no desenho de verificacao automatica no protocolo.


2. Informativo de Jurisprudencia n. 908: Injecao de comandos (prompt injection). Insercao, em peca recursal, de comando oculto dirigido a sistema de inteligencia artificial. Ato atentatorio a dignidade da justica. Litigancia de ma-fe. Aplicacao de multa pessoal aos advogados.

Fonte: Superior Tribunal de Justica, Informativo de Jurisprudencia | URL primaria: https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=022702

Data de publicacao: 2026-11-03

Categoria: (c) risco novo importante

Sintese: O Informativo 908 consolida o AREsp 3.095.458-SP (Primeira Turma, relator ministro Paulo Sergio Domingues, unanime, julgado em 20/10/2026). A Secretaria de Processamento de Feitos certificou que a peticao de recurso especial tinha conteudo na camada de texto do PDF ausente da renderizacao visual, de carater imperativo, voltado a levar o sistema generativo de triagem do STJ (usado nos termos da Resolucao CNJ 615/2025) a afirmar a superacao dos obices de admissibilidade. O acordao descreve tecnica de evasao adicional: palavras fragmentadas por espacos ao longo de todo o trecho ("e stao", "inexiste ncia", "7/ST J"), o que impede busca literal no documento. A tese enquadra a conduta no art. 77, IV e VI, do CPC, com fundamento tambem nos arts. 5, 7, 9 e 10, e fixa que a multa alcanca todos os advogados constituidos, independentemente de quem assinou ou protocolou, com oficio a OAB e ao MPF para apuracao administrativa e criminal. O texto registra precedentes assemelhados na Segunda Turma (procurador municipal, multa sobre o valor da causa, comunicacao a OAB, MPF e Policia Federal) e na Sexta Turma (oficio por possivel fraude processual). O valor da multa nao consta do Informativo.

Por que entrou: E a versao oficial e indexada da tese, com detalhe forense que a cobertura jornalistica anterior nao trazia: o metodo de constatacao (divergencia entre camada de texto e renderizacao) e a fragmentacao de tokens como contramedida a deteccao por string. Ambos se traduzem diretamente em regras de saneamento de entrada para pipelines que ingerem pecas.


3. Operationalizing NCII and CSAM Law in the Age of AI: Open Problems

Fonte: arXiv (cs.CY), Kimberly Mai, Cate Heine e Vinith M. Suriyakumar (AI Security Institute, Reino Unido) e Ashia C. Wilson (MIT) | URL primaria: https://arxiv.org/abs/2611.07831

Data de publicacao: 2026-11-05

Categoria: (c) risco novo importante

Sintese: O artigo, assinado por pesquisadores do AI Security Institute britanico e do MIT, examina as leis da Inglaterra e Pais de Gales e dos EUA sobre imagens intimas nao consentidas (NCII) e material de abuso sexual infantil (CSAM) sinteticos e mapeia onde os tipos legais dependem de conceitos sem operacionalizacao tecnica. Os pontos centrais: decidir se a pessoa retratada e real e identificavel; decidir se um modelo e "especializado" ou "destinado" a gerar esse material, criterio que leis novas ja usam para criminalizar a criacao ou distribuicao de modelos; e rastrear uma imagem ate o modelo que a gerou, com fingerprinting robusto a fine-tuning e merges. A agenda organiza as questoes abertas por etapa (criacao, posse, distribuicao, ferramentas, dados de treino), inclui perguntas como se pesos de modelo podem ser tratados como conversiveis em imagem e se e possivel inferir intencao diretamente do modelo, e as associa a camada do stack de implantacao. Como motivacao, os autores citam aumento de 26.385% em videos de CSAM gerados por IA entre 2024 e 2025 (Internet Watch Foundation) e mais de 40 milhoes de visitantes unicos mensais em sites de "nudificacao" (Institute for Strategic Dialogue).

Por que entrou: Toca o nucleo de crimes digitais e prova digital: a tipicidade passa a depender de perguntas periciais (identificabilidade, especializacao do modelo, atribuicao de origem) sem metodo validado, o que abre flanco probatorio em qualquer persecucao. Leitura comparada util para propostas brasileiras sobre deepfake sexual e para a pericia de atribuicao de modelo.


REVISAO ADVERSARIAL

Item 1 (Coreia). Fonte de terceiros: o relatorio da Administracao Nacional dos Tribunais nao foi localizado no site da Suprema Corte coreana nesta execucao [nao verificado na fonte primaria]. Autor: veiculo identificado (Kyunghyang Shinmun), traducao para o ingles sinalizada como assistida. URL resolve via curl (HTTP 200), dominio oficial khan.co.kr. Segunda fonte independente: Law Times via Asia Economy (view.asiae.co.kr, HTTP 200) confirma 360 respostas, 6 a 16/10, 80,7%, 65,4%, 69,5% (parte), 57,6% (advogados), 91,7% e 64,8% ("muito necessario"); Korea Times/Yonhap (HTTP 200) confirma os mesmos numeros. Divergencias: a Korea Times traduz os 164 juizes como juizes que "eles proprios citaram precedentes falsos", leitura contrariada por Khan e Asiae (164 apontaram a parte); a sintese segue as duas ultimas. Parte da imprensa coreana fala em 67,5% ou 68%, consistente com o mesmo numerador sobre as 360 respostas totais, enquanto os 80,7% usam como base os juizes civeis, de familia e administrativos [base exata nao verificada]. Os percentuais das medidas (61,4%, 61,1%, 60,6%, 55,4%) aparecem so no Khan [nao verificados em segunda fonte]. Linguagem promocional: nenhuma. Categoria (b) resiste: e erro documentado com dado, nao risco hipotetico.

Item 2 (STJ, Informativo 908). Fonte primaria oficial do proprio tribunal (scon.stj.jus.br), URL estavel por CNOT resolve via curl (HTTP 200) e o texto contem o numero do processo, o relator e a data. O inteiro teor do acordao nao foi lido, so o resumo do Informativo. Os precedentes da Segunda e da Sexta Turma sao mencionados sem numero no trecho lido [nao verificados]. A multa de R$ 20 mil noticiada em 20 e 21/10 nao aparece no Informativo [nao verificado nesta execucao]. Risco de redundancia: o julgamento ja foi coberto pela serie em outubro a partir de noticias; o item entra como publicacao oficial nova (03/11) com conteudo tecnico nao coberto antes (constatacao por camada de texto, fragmentacao contra busca literal, extensao da multa a todos os advogados constituidos). Se o criterio for de fato novo e nao de fonte nova, este item e o mais fraco do dia. Categoria (c) resiste.

Item 3 (arXiv 2611.07831). Preprint sem revisao por pares; autores e afiliacoes identificados no HTML do arXiv (AI Security Institute e MIT, autora correspondente com e-mail institucional dsit.gov.uk). URL resolve (HTTP 200). E artigo de agenda de pesquisa, sem experimento proprio; os dois numeros da introducao (26.385% e 40 milhoes) vem de relatorios de terceiros citados pelos autores [nao verificados em segunda fonte]. O mapeamento das leis da Inglaterra e Pais de Gales e dos EUA foi lido so no sumario e na introducao; os dispositivos especificos nao foram conferidos um a um [nao verificado]. Linguagem promocional: nenhuma. Categoria (c) resiste; nao e (d) porque nao entrega solucao.

Nenhum item tem origem social. A fonte social localizada (post de Vladimir Aras no X sobre prompt injection em peticao trabalhista, via Tom's Hardware) data de maio de 2026 e foi descartada. Nenhuma substituicao na fase adversarial.


AUDITORIA

Nivel de janela: em 36h nenhum candidato qualificado (feeds na janela sem tema de IA ou so com roundup de mercado e textos de opiniao). Em 72h, um unico candidato novo qualificado (arXiv 2611.07831, de 05/11); os demais itens de IA em 72h ja tinham sido entregues. A janela foi escalonada para 7 dias (corte em 31/10), que trouxe a pesquisa coreana (02/11) e o Informativo 908 do STJ (03/11).

Deduplicacao: arquivo de ontem (2026-11-06) lido; por causa da janela de 7 dias, conferidos tambem 2026-10-31 a 2026-11-05 e, por termos, todo o diretorio curadorias/. Excluidos por duplicidade: Clio/50-state survey (LawNext, entregue em 06/11), arXiv 2611.07988 e 2611.06972 (entregues em 06/11), LegalEvolver 2611.06381 (05/11), PROSE 2611.04921 (04/11), NitiBench+ 2611.03576, Unlocking Criminal Court Decisions 2611.03051 e ICJ-Graph 2611.02630 (entregues em 03/11), Vokshi v. Canada (05/11). A pesquisa coreana tinha sido descartada em 05/11 so por janela, nao por triagem.

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, mas zero entradas parseaveis, conteudo nao-RSS). ConJur respondeu 200, sem itens de IA na janela; a busca complementar site:conjur.com.br devolveu so resultados fora do dominio.

Base Charlotin: "Last updated: 5 November 2026"; caso mais recente datado de 03/11/2026 (Vokshi, ja entregue); os demais sao de 29/10 ou anteriores, fora da janela.

Seguranca: o conteudo coletado da materia da Tom's Hardware e do Informativo do STJ reproduz comandos ocultos dirigidos a sistemas de IA, como objeto da noticia. Foram tratados como dado: nenhum foi seguido nem transcrito literalmente neste arquivo. Nenhum texto coletado pediu acoes a esta execucao.

Descartes no filtro deterministico (8): Artificial Lawyer "Litera Owner Hg + Anthropic Invest in AI Transformation Venture" (investimento, termo vetado, sem caso de uso); "Legal Innovators UK Starts Tomorrow" (promocao de evento); "Copilot for Legal, AL Interview: Carina Negreanu, Microsoft" (entrevista de fornecedor); "Ex-Legorans Bag $2.4m For Real Estate AI Native" (captacao sem caso de uso); "Will AI Change the Identity of Law Firm Partners?" (enquadramento de futuro da advocacia); LawNext "NetDocuments CPO Dan Hauck on the Company's Redesigned Platform" (demo de fornecedor sem auditoria); Wisevoter "Judge Upholds Ban on AI-Generated Art Copyright" (autoria nao identificavel; descreve como de 03/11/2026 decisao de 2023 no caso Thaler); Elets "Fake precedents and hidden prompts are pushing courts towards AI rules" (previsao assistida por IA, sem autor individual).

Descartes na triagem qualitativa (principais):
Artificial Lawyer "Harvey + Legora IPO Plans, A&O $1.1bn, Legal Innovators NY" (06/11): roundup de mercado sem dado verificavel sobre uso.
Damien Charlotin, "AI & Law Stuff" (artificialauthority.ai, 06/11): ensaio de opiniao; as fontes que cita (Ringe e Folkerts, 28/10; Queen e Zou, 02/11) foram avaliadas a parte.
"Legal exploits may emerge at scale" (Felix Ringe e Linus Folkerts, 28/10): fora da janela de 7 dias.
"The shelf life of LLM findings" (Owen Queen e James Zou, Stanford, 02/11): 44% de 50 claims sobre LLMs expiraram, incluindo a taxa de 55% de referencias fabricadas do GPT-3.5; descartado por nao ser especifico de Direito; candidato reserva.
arXiv 2611.08228 "Domain-specific information retrieval" (Verberne, Piroi e Hanbury, 05/11): texto de revisao, sem resultado novo mensuravel.
Tom's Hardware, advogados multados por prompt injection em peticao trabalhista (01/11): fato de maio de 2026 (post de origem no X datado de 13/05/2026 pelo ID); o tema ja foi coberto pela serie (TST, multa de 10%).
O Cafezinho "STJ aplica multa por ma-fe a quem cita julgado inventado por IA" (03/11): veiculo secundario sem autoria, julgamento de junho de 2026 (AgInt no AREsp 3.010.133/MG).
go.kompas.com "Lawyer Penalized for Using AI" (05/11): artigo de opiniao traduzido por IA, sem caso novo.
Withers v. City of Aberdeen (Bloomberg Law, 09/06/2026), Daily Journal sobre a Suprema Corte da California (16/01/2026), Volokh "Instead, Claude Just Made Up More Stuff" (19/05/2026), Law360 sobre sancao reduzida com base no Setimo Circuito (20/05/2026), Migalhas sobre punicoes a advogados e magistrados (22/07/2026), Vincent AI e screen takeover (12/2025), Fifth Circuit sobre juiz que usou IA (NatLawReview, 23/10/2026): todos fora da janela.
Itens de ConJur, JOTA e Volokh na janela sem relacao com IA (apostas, tributario, eleitoral, constitucional, Open Threads); ConJur "Dados de celular usados como prova devem ser entregues a defesa" (06/11) e de prova digital mas sem componente de IA.

Substituicoes: nenhuma.
