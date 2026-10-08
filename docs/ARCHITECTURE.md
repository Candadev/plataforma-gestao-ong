# Arquitetura

## Visão geral

Sistema web de gestão para a AMAD. O backend é uma API em FastAPI que guarda os dados em um banco relacional. As telas ainda serão definidas a partir do levantamento de necessidades com a associação.

## Camadas

| Camada | Pasta | Responsabilidade |
|---|---|---|
| API | `app/main.py` | Rotas e regras de entrada e saída |
| Acesso ao banco | `app/database/` | Conexão, sessão e `Base` do SQLAlchemy |
| Modelos | `app/models/` | Definição das tabelas |
| Migrações | `migrations/` | Histórico versionado do esquema do banco |

## Modelo de dados atual

**users**: `id`, `nome`, `email` (único), `senha_hash`, `perfil`, `ativo`.

Perfis de acesso: `ADMIN`, `AUDITOR`, `PARCEIRO`, `PUBLICO`.

## Módulos planejados

Definidos a partir das dificuldades observadas na AMAD:

1. **Membros**: cadastro com status (ativo/inativo) e contagem.
2. **Atividades**: registro com data, responsável, participantes e anexos, com busca.
3. **Projetos**: objetivo, responsáveis, prazos e tarefas.
4. **Avisos e relatório de impacto**: comunicados e dados consolidados para propostas de financiamento.

A ordem de construção será validada com a associação.

## Decisões técnicas

- **SQLite em desenvolvimento, PostgreSQL em produção.** A URL do banco vem de `DATABASE_URL`, então a troca não exige mudar o código. A migração deve acontecer antes de entrarem dados reais.
- **Alembic para o esquema.** As tabelas não são mais criadas automaticamente ao iniciar a API; o histórico fica em `migrations/versions/`.
- **Senhas.** Apenas o hash é armazenado (`senha_hash`); a biblioteca de hash será definida na etapa de login.
- **Dados pessoais (LGPD).** Coletar o mínimo necessário e restringir a visualização por perfil.

## Metodologia

O desenvolvimento segue a pesquisa-ação: a associação participa do levantamento, da priorização e da validação de cada módulo antes da próxima etapa.

## Pendências em aberto

- Escolha da forma de entregar as telas (páginas servidas pela própria API ou front-end separado).
- Definição de hospedagem, backups e responsável pela manutenção.
- Suporte a múltiplas associações (campo de organização nas tabelas).
