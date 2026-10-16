# Recuperação da curadoria diária IA e Direito

Este repositório é a fonte da verdade da curadoria. Nenhum computador guarda estado que não esteja aqui. Se um arquivo existir só numa máquina, ele ainda não está protegido.

## O que vive onde

| Peça | Onde vive | Cópia versionada |
|---|---|---|
| Definição das tarefas (prompt, agenda, modelo, conectores) | Conta claude.ai, em claude.ai/code/routines | `prompt/` e `tarefa.json` |
| Execução | Tarefa em nuvem `Curadoria ia direito nuvem`, sem dependência de computador | não se aplica |
| Acervo diário | `curadorias/` neste repositório | o próprio git |
| Consumidor (podcast) | `automacao_podcastia` no computador local, lendo de `entrada\` | fora deste repositório, plano próprio |

## Estado em 2026-10-16

A tarefa em nuvem foi criada e roda às 05h51 (São Paulo). A tarefa local (`desktop-3l0sta1`, 06h00) continua ativa em paralelo e ainda é quem alimenta `automacao_podcastia\entrada`. O corte (pausar a local e alimentar `entrada\` a partir deste repositório) ainda não foi feito.

## Cenário 1: perda do computador

A curadoria em nuvem não para. O que se perde é o consumidor local e, antes do corte, a cópia em `entrada\`.

Em máquina nova (Windows):

1. Instalar Git for Windows e o app Claude desktop, e entrar na mesma conta.
2. Clonar: `git clone https://github.com/pbms01/curadoria-ia-direito "$env:USERPROFILE\curadoria-ia-direito"`
3. Conferir as quebras de linha: o `.gitattributes` força LF no checkout, mas confira com `git ls-files --eol curadorias` (a coluna `w/` deve mostrar `lf`).
4. Restaurar `automacao_podcastia` pelo plano próprio dele e apontar a entrada para `curadorias\` deste clone, com `git pull` agendado no Agendador de Tarefas do Windows antes do horário em que o pipeline lê.
5. Se a tarefa local ainda existir, ela ficou presa ao computador perdido: pausar em claude.ai/code/routines.

## Cenário 2: tarefa em nuvem apagada, corrompida ou com prompt quebrado

Prompt quebrado: recuperar a versão anterior com `git log -- prompt/curadoria-nuvem.md` e `git show <hash>:prompt/curadoria-nuvem.md`, e colar no campo de instruções da tarefa.

Tarefa apagada: em claude.ai/code/routines, New routine, Cloud. Instruções: conteúdo literal de `prompt/curadoria-nuvem.md`. Repositório: `pbms01/curadoria-ia-direito`. Agenda e modelo: conforme `tarefa.json`. Conectores: remover todos os incluídos por padrão. Atualizar o `id` em `tarefa.json` no mesmo commit.

## Cenário 3: GitHub desconectado da conta Claude

A tarefa pula execuções por até 72 horas e, depois disso, é desligada. Reconectar o GitHub na conta e, se já tiver passado das 72 horas, religar a tarefa em claude.ai/code/routines.

## Cenário 4: contingência em modo local

Se a execução em nuvem ficar indisponível, `prompt/curadoria-local-v1.md` é o prompt original que grava em pastas locais. Criar uma tarefa local num computador com as duas pastas e ajustar os caminhos em PARAMETROS se o usuário do Windows for outro. Depois, copiar os arquivos produzidos para `curadorias/` e commitar, para o acervo não divergir.

## Migração do acervo local (uma vez, com o computador atual funcionando)

As curadorias de 24/09 em diante existem só em `C:\Users\pbm_s\Ia_e_justica\Agente de curadoria Anti-hype AI`. No PowerShell:

```powershell
cd $env:USERPROFILE
git clone https://github.com/pbms01/curadoria-ia-direito
# /XC /XN /XO: copia só arquivos que ainda não existem no destino,
# para não sobrescrever as curadorias que a tarefa em nuvem já gravou
robocopy "$env:USERPROFILE\Ia_e_justica\Agente de curadoria Anti-hype AI" "$env:USERPROFILE\curadoria-ia-direito\curadorias" "curadoria-ia-direito_*.md" /XC /XN /XO
cd curadoria-ia-direito
git add curadorias
git commit -m "migracao do acervo local (desktop-3l0sta1)"
git push
```

O robocopy devolve código 1 quando copiou arquivos; isso é sucesso, não erro.

## Verificação de saúde

O status verde da tarefa indica só que a sessão começou e terminou sem erro de infraestrutura, não que o arquivo foi gravado. A prova de execução é o commit do dia em `curadorias/`. Pendente: verificador independente (GitHub Action às 08h que abre issue se o arquivo do dia não existir).
