CURADORIA DIARIA IA E DIREITO, 2026-11-11

CABECALHO
Data de coleta: 2026-11-11 (America/Sao_Paulo), execucao entre 08:51 e 09:40 UTC
Janela aplicada: 36h (nivel base, sem escalonamento)
Buscas WebSearch executadas: 15
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 66 (59 itens RSS dentro da janela, deduplicados entre LawSites e LawNext; 3 arXiv via RSS cs.CL/cs.CY/cs.AI; 4 resultados WebSearch datados dentro da janela; 0 casos novos na base Charlotin dentro da janela)
Candidatos apos filtro deterministico: 59
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 2 / (d) 1
Origem das fontes: midia tradicional/especializada 33% / Substack-RSS e blogs/preprints via RSS 67% / social 0%


1. Doe v. Regents of the University of Michigan, No. 26-10451 (E.D. Mich.), Opinion and Order Granting in Part and Denying in Part Defendants' Motion to Dismiss

Fonte: United States District Court, Eastern District of Michigan (Judge Laurie J. Michelson), via CourtListener/RECAP; sinalizado por The Volokh Conspiracy (Eugene Volokh) | URL primaria: https://storage.courtlistener.com/recap/gov.uscourts.mied.391922/gov.uscourts.mied.391922.43.0.pdf
Fonte secundaria: https://reason.com/volokh/2026/11/10/disability-discrimination-and-allegations-of-ai-use-in-students-university-of-michigan-course-papers/
Data de publicacao: 2026-11-09 (decisao, ECF No. 43); 2026-11-10 (post Volokh)
Categoria: (c) risco novo importante

Sintese: Estudante de graduacao com transtorno de ansiedade generalizada e TOC foi sancionada pela Universidade de Michigan (probation disciplinar anotada no historico, reescrita de trabalhos e ensaio reflexivo) em tres acusacoes de uso de IA em trabalhos do curso Great Books 191. Segundo a peticao, o instrutor usou software de deteccao de IA e anexou "AI-generated comparison outputs" obtidos ao promptar um modelo com o outline da propria aluna e o feedback do professor; a aluna sustenta que tom, estrutura meticulosa e consistencia estilistica decorrem das suas condicoes clinicas e apresentou laudos. A decisao de 28 paginas extingue o pedido de devido processo (imunidade qualificada dos individuos, porque nao ha precedente que torne "clear to a reasonable" instrutor que usar deteccao de IA para fundamentar acusacao viole o devido processo), extingue os pedidos de falta de acomodacao e retaliacao, mas mantem as pretensoes de discriminacao por deficiencia sob ADA e Rehabilitation Act contra a universidade, por ser plausivel a alegacao de que os laudos foram desconsiderados ao concluir pelo uso de IA. O caso segue para instrucao; nenhuma conclusao sobre a confiabilidade do detector foi emitida.

Por que entrou: E um caso concreto, com decisao primaria, em que saida de detector de IA e comparacao gerada por LLM funcionaram como prova de autoria em procedimento sancionador. Para prova digital, expoe o problema de falso positivo estilistico e o vies contra perfis de escrita atipicos, e indica que a via de contestacao viavel, nesta fase, foi antidiscriminatoria e nao processual.


2. Crosby Insures Paralegal Agents: Interview

Fonte: Artificial Lawyer (entrevista com Ryan Daniels, CEO da Crosby; autoria editorial "artificiallawyer") | URL primaria: https://www.artificiallawyer.com/2026/11/10/crosby-insures-paralegal-agents-interview/
Data de publicacao: 2026-11-10
Categoria: (c) risco novo importante (alocacao de responsabilidade por agentes juridicos autonomos)

Sintese: A Crosby, escritorio de advocacia estruturado em torno de agentes de IA, declara ter contratado apolice de responsabilidade de US$ 5 milhoes cobrindo o output de seus "paralegal agents", emitida pela Testudo (coverholder do Lloyd's de Londres que subscreve seguro autonomo de responsabilidade por IA) e em vigor desde o inicio de novembro de 2026. Segundo a empresa, a apolice cobre tanto agentes em tarefas sob supervisao de advogado quanto agentes executando trabalho paralegal sozinhos; a Testudo teria analisado arquitetura, modelos, controles de governanca e logs de revisao humana antes da subscricao. Os agentes funcionam como porta de entrada de toda mensagem do cliente, em sandbox com isolamento de dados por cliente, e escalam para advogados o que esta fora do conjunto de capacidades. Metricas declaradas pela propria Crosby: 94% de acuracia na decisao de executar ou escalar antes do lancamento; revisao humana zerada para 20% das tarefas preexistentes; economia de cerca de 36 das ~180 horas diarias de revisao. A Bloomberg Law havia noticiado em 2026-08-03 a intencao de contratar o seguro.

Por que entrou: E o primeiro caso documentado, com seguradora e cobertura identificadas, de transferencia contratual do risco de erro de agente juridico autonomo, incluindo atuacao sem supervisao de advogado. Coloca em pauta factual questoes de supervisao (ABA Model Rule 5.3), exercicio irregular da advocacia e o que uma subscricao exige como evidencia de controle (logs, isolamento, avaliacao por trajetoria).


3. An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework

Fonte: arXiv (cs.CL), Serhii Zabolotnii e Alina Tarasova | URL primaria: https://arxiv.org/abs/2611.14244
Data de publicacao: 2026-11-10
Categoria: (d) solucao para gargalo em pipelines juridicos

Sintese: Os autores descrevem um pipeline para triagem de projetos de lei quanto a riscos de corrupcao, que localiza o dispositivo que um perito criticaria e nomeia o defeito regulatorio. A arquitetura separa nucleo deterministico de parsing, qualificacao por modelo dispositivo a dispositivo, atribuicao de fatores por regras e supervisao humana externa. Construiram benchmark aberto a partir de pareceres publicados da agencia anticorrupcao ucraniana (NAZK): 132 projetos e 474 achados extraidos por modelo. Em 100 projetos, o sistema casa 0,28 dos achados nos dez primeiros flags com Gemma 4 31B local, 0,30 com Sonnet 5.5 e 0,43 a 0,46 considerando todos os flags (nao cego), contra baseline cego congelado de 0,21 (IC 95% 0,16 a 0,26). A maioria dos erros ocorre em dispositivos corretamente localizados mas qualificados com risco diferente, e nenhum dos 32 achados de colisao normativa foi recuperado. Em 21 atos fora do tuning, o pipeline supera um prompt monolitico com toda a metodologia na metrica estrita, mas nao na leniente, e Opus 5.5 nao acrescenta nada sobre Sonnet. Os autores registram que os escores medem concordancia com achados extraidos por modelo e julgados por LLM, sem validacao por perito humano.

Por que entrou: Ataca o gargalo de ancoragem dispositivo a dispositivo (qual artigo, qual defeito) com arquitetura hibrida deterministica mais LLM e eval publico derivado de pareceres oficiais. O relato de limitacoes e util como padrao: falha total em colisao normativa (raciocinio intertextual), ganho marginal de modelo maior e circularidade de rotulos gerados e julgados por LLM.


REVISAO ADVERSARIAL

Item 1 (Doe v. Regents). Fonte primaria: decisao judicial, PDF de 28 paginas no RECAP (CourtListener), resolve via curl (HTTP 200, application/pdf, 244 KB); cabecalho "Case 2:26-cv-10451-LJM-DRG ECF No. 43 Filed 11/09/26", assinatura "Dated: November 9, 2026, s/Laurie J. Michelson". Dominio storage.courtlistener.com e o bucket oficial do Free Law Project, sem typosquat. Conferidos no PDF: diagnosticos alegados, curso, nomes dos instrutores, sancoes, trecho sobre "AI-detection software", dispositivo final (extintos devido processo, acomodacao e retaliacao; mantidas ADA/RA por discriminacao contra a universidade em capacidade oficial e o pedido declaratorio). Nao verificado: qual detector de IA foi usado (a decisao nao nomeia ferramenta) [nao verificado]. Os fatos sao alegacoes aceitas como verdadeiras na fase de motion to dismiss, nao fatos provados. Autor do post (Eugene Volokh) identificado, blog com historico longo. Linguagem promocional: nenhuma. Categoria (c) resiste; nao e (b) porque nao ha falha tecnica comprovada, apenas risco de falso positivo alegado.

Item 2 (Crosby). Fonte: entrevista em veiculo especializado, com as respostas escritas pela propria empresa; a apolice nao foi publicada. URL resolve (HTTP 200). Verificado de forma independente: a Testudo existe e se apresenta em seu site oficial (testudo.co) como coverholder do Lloyd's que subscreve seguro autonomo de responsabilidade por IA generativa; a Bloomberg Law (2026-08-03) noticiou a intencao da Crosby de contratar seguro para outputs de IA. Nao verificados em segunda fonte: valor de US$ 5 milhoes, data de vigencia, escopo da cobertura (incluindo agentes sem supervisao), 94% de acuracia de escalonamento, 20% de tarefas sem revisao, 36 de ~180 horas diarias [nao verificado]. Linguagem promocional residual: o comentario editorial final do Artificial Lawyer ("groundbreaking", aposta de que sera mainstream em 2030) e o anuncio de evento foram excluidos da sintese. Categoria: o item foi rejeitado como (a) porque as metricas sao autodeclaradas e sem auditoria independente; mantido como (c) porque o fato relevante (existencia de cobertura securitaria para agentes) e um evento verificavel parcialmente e gera questao regulatoria concreta. Titulo original contem travessao curto entre "Agents" e "Interview", substituido por dois-pontos por restricao de formatacao.

Item 3 (TRACE). Fonte primaria: preprint arXiv, autores identificados (afiliacao nao confirmada na pagina de abstract [nao verificado]); URL resolve (HTTP 200); metadados citation_date 2026/11/10. Preprint sem revisao por pares. Numeros (132 projetos, 474 achados, 0,28/0,30/0,43 a 0,46, baseline 0,21 com IC 0,16 a 0,26, 32 achados de colisao, 21 atos held-out, 73 de 74 rotulos concordantes) conferidos apenas no abstract, nao em segunda fonte nem no corpo do PDF [nao verificado em segunda fonte]. Disponibilidade publica do benchmark declarada pelos autores, link nao checado [nao verificado]. Linguagem promocional: nenhuma; o abstract relata limitacoes explicitamente. Categoria (d) resiste.

Nenhum item de origem social. Nenhuma substituicao foi necessaria por URL quebrada.


AUDITORIA

Janela: 36h aplicada; 3 itens qualificados atingidos sem escalonamento.

Deduplicacao: comparado com curadorias/curadoria-ia-direito_2026-11-10.md (FraudBench, ConJur/TJ-RO "porta fechada", Vietnamese Legal Ontology); nenhuma colisao de URL ou titulo. Conferido tambem que Crosby e Doe v. Regents nao aparecem em curadorias de 2026-11-06 a 2026-11-10.

Feeds que falharam: Stanford CodeX (HTTP 404); Migalhas (HTTP 404); Above the Law tag IA (HTTP 200, feed com 0 entradas). Demais 10 feeds HTTP 200. ConJur respondeu 200 nesta execucao (sem desafio Cloudflare); mesmo assim foi feita busca site:conjur.com.br, sem resultado novo na janela. Unikowsky, Charlotin Substack e 3 Geeks sem itens na janela.

Camada C: base de Damien Charlotin com "Last updated: 10 November 2026", caso mais recente datado de 6 November 2026 (Salgado v. Fred Palla Farms, ja entregue em 2026-11-09); nenhum caso novo dentro da janela. arXiv via API retornou HTTP 429; substituido pelos RSS diarios cs.CL, cs.CY e cs.AI (HTTP 200). Hacker News: busca sem resultado datado na janela.

Descartes com motivo:
Law360, "2 Attys Fined For AI Citation Errors But Local Counsel Spared" (2026-11-10, magistrada federal de Delaware, US$ 3.000): paywall, decisao primaria nao localizada (CourtListener API exige autenticacao, HTTP 401); sem fonte primaria verificavel.
Law360, "Atty Can't Duck Sanctions Over Alleged AI Fake Citations" (2026-11-10, D. Mass.): mesmo motivo.
NC/VA Lawyers Weekly, "It's no hallucination: AI-generated errors persist in court filings" (2026-11-09): HTTP 403 e materia de panorama sem caso novo.
Bradford & Barthel, "Legislative Roundup: AI Citations..." (2026-11-09): boletim de escritorio, sem dado novo verificavel.
Blue J, captacao de US$ 176M (LawNext e Artificial Lawyer, 2026-11-10): rodada de investimento sem resultado mensuravel.
Artificial Lawyer, "Claude on Anthropic IPO": texto gerado perguntando a um LLM, padrao "I asked GPT".
Artificial Lawyer, "Copilot for Legal Won't Cannibalize Us, Litera" e "In Conversation With Axiom": discurso de fornecedor sem dado auditavel.
Artificial Lawyer, "Mercedes Lawyer Joins AI Native Compound Law" e keynote White & Case no Legal Innovators NY: movimentacao de pessoal e divulgacao de evento.
Ken Crutchfield, "Is BigLaw Too Big To Fail?" (LawNext): sem componente de IA verificavel.
JOTA, "Envelhecimento, clima e IA ampliarao desafios do Estado": projecao generica, IA periferica.
arXiv ScrapeBench (2611.11306) e "Time as Structure" (2608.15270): versoes revisadas (replace) de submissoes anteriores a janela.
STF, "STF identifica uso de comandos ocultos para influenciar IA" (2026-09-25), CNJ, comite de seguranca da IA (2026-05-28), Migalhas, TJ-MG multa por IA (2026-08-21), Mondaq/Jones Walker sobre prompt injection (2026-08-25): fora da janela.
Demais itens de ConJur (cobertura do Anuario da Justica SP), JOTA (tributario, eleitoral, STF), Volokh (constitucional) e HLR (comentarios de casos da Suprema Corte): sem relacao com IA e Direito.

Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.

Substituicoes: nenhuma.
