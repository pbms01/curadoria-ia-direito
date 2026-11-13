CURADORIA DIARIA IA E DIREITO, 2026-11-13

CABECALHO
Data de coleta: 2026-11-13 (America/Sao_Paulo), inicio por volta de 05h40
Janela aplicada: 72h (escalonada a partir de 36h; ver AUDITORIA)
Buscas WebSearch executadas: 15
Feeds RSS consumidos com sucesso: 10 de 13
Candidatos coletados: 34
Candidatos apos filtro deterministico: 21
Itens entregues: 3 de 3
Distribuicao por categoria: (a) 0 / (b) 0 / (c) 1 / (d) 2
Origem das fontes: midia tradicional 33% (MediaNama, com copia da decisao judicial) / Substack-RSS 67% (arXiv, via API Atom) / social 0%


1. Ramasubbu v. K. Gopal, IAS, and another, Cont. P(MD) No. 3763 of 2026 (High Court of Madras, Madurai Bench), Order dated 10.11.2026

Fonte: High Court of Madras, Bancada de Madurai (Justice G.R. Swaminathan e Justice M.D. Sumathi), copia integral da ordem hospedada por MediaNama; reportagem de Prabhanu Kumar Das (MediaNama) | URL primaria: https://www.medianama.com/wp-content/uploads/2026/11/Library_contempt_order.pdf

Fonte secundaria: https://www.medianama.com/2026/11/223-madras-high-court-ai-generated-books-fir/

Data de publicacao: 2026-11-10 (ordem); 2026-11-11 (reportagem)

Categoria: (c) risco novo importante

Sintese: Em incidente de desacato (contempt) por descumprimento de ordem de 19.06.2024 sobre compras de livros para bibliotecas publicas de Tamil Nadu, a bancada de dois juizes registra que o Estado adquiriu, com recursos publicos ("crores of rupees"), obras falsamente atribuidas a autores reais, incluindo um livro atribuido ao economista Jean Dreze, que o denunciou como falso, e textos atribuidos ao poeta Bharathiyar. A ordem interpreta a Regra 18(4) das Tamil Nadu Public Libraries Rules, 1950, e estende o criterio "doubtful taste" a nao ficcao, afirmando expressamente que obras geradas por IA e plagiadas se enquadram nessa vedacao. O tribunal vincula o fato ao direito de receber informacao acurada (art. 19(1)(a) da Constituicao indiana), determina o registro imediato de FIR pela Directorate of Vigilance and Anti-Corruption, o congelamento das contas da editora Agal Vilakku e de seu proprietario, a retirada dos livros suspeitos do acesso publico e a apresentacao, por affidavit, dos valores gastos e dos servidores envolvidos. O caso foi pautado para 11.11.2026. A propria ordem nao quantifica quantos titulos seriam gerados por IA.

Por que entrou: Primeiro precedente localizado nesta curadoria em que um tribunal qualifica conteudo gerado por IA como criterio juridico de inidoneidade em compra publica de acervo informacional, com consequencia penal (FIR) e patrimonial (bloqueio de contas). O vetor (livros sinteticos com autoria falsa entrando em acervo publico) tem paralelo direto com contaminacao de bases documentais usadas em RAG.


2. Towards Better Legal Reasoning LLMs: Signal Balancing and Reward Scheduling

Fonte: arXiv (cs.CL), Yinghao Hu, Qian Xiao, Yuting Huang, Kaisong Song, Yiquan Wu, Ang Li, Junjie Cao, Jun Lin, Kun Kuang e Fei Wu (Zhejiang University, Northeastern University, Alibaba Group, University of Macau) | URL primaria: https://arxiv.org/abs/2611.15346

Data de publicacao: 2026-11-11

Categoria: (d) solucao para gargalo em pipelines juridicos

Sintese: O trabalho propoe treinamento em dois estagios para LLMs juridicos que geram cadeia de raciocinio explicita. No Estagio I (JurisCoT-SFT), um objetivo dual normalizado por comprimento evita que o sinal de aprendizado da resposta final seja diluido por traces longos. No Estagio II (LABPO, Lifecycle-Aware Backtrackable Policy Optimization), sinais de recompensa auxiliares sao avaliados periodicamente, reponderados ou aposentados conforme impacto na metrica final, com rollback de checkpoint para mitigar reward hacking. Entre os sinais auxiliares ha uma verificacao de autenticidade de dispositivos legais: cada artigo citado no raciocinio e extraido (nome, numero, conteudo), embeddado com SimBERT e confrontado com uma base de referencia de textos normativos reais. O corpus de treino tem 2,73 milhoes de triplas (consulta, raciocinio, resposta) para direito legislado e 35.965 para case law, com traces gerados por DeepSeek-R1 e filtrados por rejection sampling. Sobre Qwen3-8B, o score agregado no ChJGBench sobe de 0,6406 para 0,7786; sobre Llama-3.1-8B, de 0,3374 para 0,6452; no LegalBench (Sara-N, erro, menor e melhor) o Qwen3-8B cai de 8,093 para 1,753.

Por que entrou: Oferece mecanica concreta e replicavel para um gargalo recorrente em pipelines juridicos: citacao normativa inexistente dentro do raciocinio, tratada como sinal de recompensa verificavel contra base de referencia, e nao apenas como checagem pos-geracao.


3. ChJGBench: A Comprehensive Benchmark for Chinese Legal Judgment Generation with Diagnostic Evaluation

Fonte: arXiv (cs.CL), Yinghao Hu, Linggang Kong, Qian Xiao, Yuting Huang, Yunlong Zhang, Yujie Zhang, Yiquan Wu, Fei Duan, Kaisong Song, Jun Lin, Kun Kuang e Fei Wu | URL primaria: https://arxiv.org/abs/2611.15639

Data de publicacao: 2026-11-11

Categoria: (d) solucao para gargalo em pipelines juridicos

Sintese: Benchmark para geracao das secoes de fundamentacao e dispositivo de sentencas chinesas, construido a partir de 3.462 decisoes reais da China Judgments Online (2019 a 2024), em casos civeis, criminais e administrativos. A amostragem e estratificada por tipo de caso e ano, com transformacao de temperatura sobre a distribuicao de categorias para cobrir a cauda longa. A avaliacao e diagnostica e sensivel ao tipo de caso, com 13 tipos de metrica: tres dimensoes compartilhadas (aplicacao de dispositivo legal, identificacao de questoes controvertidas, fundamentacao) e dimensoes especificas como tipificacao, multa, reincidencia, atenuantes e pena (criminal), acolhimento do pedido e obrigacao de pagar (civel e administrativo). Qwen3-Plus atua como extrator e avaliador semantico, com acuracia de extracao media de 99,41% e kappa de Cohen de 0,70 (JUS), 0,82 (ISS) e 0,89 (DIS) contra anotacao humana. Foram testados dois modelos juridicos (WisdomInterrogatory, LegalOne 8B) e sete gerais (Claude Sonnet 4.5, DeepSeek-R1, Gemini 3 Pro Preview, GPT-5.4, Grok-4, LLaMA 3.1 405B, Qwen3-Max): Gemini 3 Pro Preview tem a maior media, o modelo juridico de 8B so compete em criminal, e civel e administrativo seguem como os casos mais dificeis.

Por que entrou: Desenho de avaliacao por dimensao juridica (e nao por similaridade textual global) e reaproveitavel como molde para eval datasets de minutas de decisao em portugues, incluindo a validacao explicita do LLM avaliador contra anotacao humana.


REVISAO ADVERSARIAL

Item 1 (Madras HC). Fonte primaria: sim, texto integral da ordem (17 paginas, rodape "https://www.mhc.tn.gov.in/judis, Uploaded on: 10/11/2026 06:31:45 pm"), obtido via curl em copia hospedada pela MediaNama (HTTP 200, application/pdf, sha256 11b6d3064bdcf53330472138eaebf587760a883a00f87c9d4b21faefae6addab). O portal oficial mhc.tn.gov.in/judis nao respondeu do ambiente de nuvem (sem codigo HTTP), entao a copia nao foi confrontada com o repositorio oficial. Autores identificados: juizes nominados na ordem; reportagem assinada. Dominio: medianama.com, veiculo indiano estabelecido, nao typosquat. Nao verificado em segunda fonte: a afirmacao, presente no titulo da reportagem, de que os livros adquiridos sao gerados por IA; a ordem trata "AI-generated and plagiarised works" como hipotese normativa e descreve concretamente obras plagiadas e de autoria falsa, sem atribuir geracao por IA a titulos especificos [nao verificado]. Tambem nao verificados: o valor total gasto (a ordem diz apenas "crores of rupees") e o desfecho da audiencia de 11.11.2026. Linguagem promocional: nenhuma. Categoria: resiste como (c); o enquadramento como (b) foi descartado porque nao ha falha tecnica de sistema de IA documentada, e sim risco regulatorio de conteudo sintetico em compra publica.

Item 2 (JurisCoT/LABPO). Fonte primaria: preprint arXiv, abstract e versao HTML resolvidos via curl (HTTP 200). Autores e afiliacoes identificados. Sem revisao por pares. Nao verificados em segunda fonte: todos os numeros (0,6406 para 0,7786; 0,3374 para 0,6452; 1,753 no Sara-N; 2,73 milhoes de instancias), extraidos apenas das tabelas do proprio paper; codigo ou pesos publicos nao localizados [nao verificado]. Ponto de atencao: o principal benchmark de avaliacao (ChJGBench) e do mesmo grupo de autores, o que reduz a independencia da comparacao. Linguagem promocional residual: "methodological innovations" na secao de limitacoes, sem impacto factual. Categoria (d) resiste.

Item 3 (ChJGBench). Fonte primaria: preprint arXiv, abstract e HTML resolvidos via curl (HTTP 200). Autores identificados. Nao verificados em segunda fonte: 3.462 decisoes, 13 tipos de metrica, 99,41% de acuracia de extracao e valores de kappa. Disponibilidade publica do dataset nao confirmada: o paper menciona revisao de privacidade "prior to any public release", e o paper irmao cita deposito no Zenodo sem link verificado [nao verificado]. Viés de avaliacao: o juiz automatico (Qwen3-Plus) e da mesma familia de um dos modelos avaliados (Qwen3-Max). Sobreposicao: itens 2 e 3 sao do mesmo grupo e do mesmo dia; mantidos como itens distintos porque um entrega metodo de treino e o outro protocolo de avaliacao, e nao houve terceiro candidato qualificado de outra origem na janela de 72h. Categoria (d) resiste.

Origem social: nenhum item entregue tem origem social. Descartes e substituicoes na revisao: nenhum item descartado nesta etapa.


AUDITORIA

Janela: a base de 36h (desde 2026-11-11 17h52 BRT) produziu 1 item qualificado (ChJGBench, anunciado no arXiv apos 20h52 UTC de 11-11; submetido as 15h52 UTC). Escalonado para 72h (desde 2026-11-10 05h52 BRT), que atingiu 3 itens; escalonamento interrompido nesse nivel.

Deduplicacao: comparado contra curadorias de 2026-11-10, 2026-11-11 e 2026-11-12 (dias da janela ampliada) e conferido contra 2026-11-06 a 2026-11-09. Excluidos por duplicidade: Doe v. Regents of the University of Michigan (Volokh, 11-10; ja em 2026-11-11); An AI Assistant for Automating Anti-Corruption Expertise (arXiv 2611.14244; ja em 2026-11-11); Quanta Logistics v. Commissioner of Customs, via MediaNama "Another customs order falls over fake judgments" (ja em 2026-11-09); Attorney Fee Award Cut from $100K to $50K (Volokh, 11-07; ja em 2026-11-08); Salgado v. Fred Palla Farms (Charlotin DB; ja em 2026-11-09).

Feeds que falharam: Stanford CodeX, HTTP 404 (pagina "Page not found"); Migalhas, HTTP 404; Above the Law IA, HTTP 200 mas corpo HTML sem itens parseaveis (provavel pagina de tema ou desafio, nao RSS). ConJur respondeu HTTP 200 com itens validos nesta execucao (sem desafio Cloudflare). Adam Unikowsky e Damien Charlotin Substack: HTTP 200, sem itens na janela. JOTA: 25 itens, nenhum sobre IA aplicada ao Direito.

Camada C: Damien Charlotin AI Hallucination Cases Database, "Last updated: 12 November 2026", 2.292 casos; CSV baixado via curl; nenhuma decisao datada dentro de 72h (mais recente: Tel Aviv Regional Labor Court, 2026-11-08, fora da janela). Hacker News: busca sem resultado na janela.

Descartes por filtro deterministico (13): Claren Launches 'Envoys' Inhouse Agents (lancamento de fornecedor sem auditoria); Legora Targets Public Sector With Ex-Minister (contratacao, sem caso de uso); Blue J $176m raise (Artificial Lawyer e LawNext, rodada de investimento); Mercedes Lawyer Joins AI Native Compound Law (movimentacao de pessoal); Legal Innovators NY, Darby Green, Ropes & Gray (entrevista promocional de evento com link de inscricao); Legal Innovators NY, Roberto Alarcon, White & Case (idem, sem dado); Keeping Legal AI Connected (conteudo patrocinado de fornecedor); Copilot for Legal Won't Cannibalize Us, Litera (declaracao de fornecedor); Claude on Anthropic IPO (especulacao sem dado); Jusbrasil lanca ferramenta gratuita (ConJur, lancamento de produto sem auditoria independente); Especialistas discutem impactos e desafios do uso da IA (ConJur, secao "Estudio ConJur", conteudo de evento patrocinado); Back to Brains, Filevine (3 Geeks, entrevista com executivo de fornecedor, fora de 72h).

Descartes na triagem qualitativa: Is Big Law 'AI Gaslighting' Us? (Artificial Lawyer, opiniao sem dado verificavel); Salomao aponta transparencia e responsabilidade (Correio Braziliense, 11-11, discurso sem decisao ou dado); Uso da IA pelo Judiciario expoe falta de transparencia (PAIPEE, 11-12, agregador sem autoria individual identificada, republica opiniao sem fonte primaria); Mensagens ocultas chegam ao STF (DCM, 11-02, fora da janela; tema ja coberto em 2026-11-07); Atty Can't Duck Sanctions Over Alleged AI Fake Citations (Law360, paywall, data e decisao nao verificaveis); It's no hallucination (Virginia Lawyers Weekly, 11-09, fora de 72h); ScrapeBench (arXiv 2611.11306, 11-08, fora de 72h); patent drafting dataset PCT (arXiv 2611.11891, 11-09, fora de 72h e sem foco em pipeline juridico de litigio); demais resultados de busca com datas anteriores a 2026-11 (listas agregadas, guias de fornecedores e trackers sem data de atualizacao).

Substituicoes: nenhuma. Seguranca: nenhum conteudo coletado continha instrucoes dirigidas ao agente.
