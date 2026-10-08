# Plataforma de Gestão para Associações (Piloto AMAD)

Sistema web de gestão para associações sem fins lucrativos, desenvolvido como projeto de extensão universitária em parceria com a AMAD. O objetivo é reunir em um só lugar o cadastro de membros, o registro de atividades e a organização de projetos, com acesso por perfil.

> **Status:** em desenvolvimento inicial. Hoje existem a base da API e o modelo de usuários. As funcionalidades abaixo ainda serão construídas a partir do levantamento de necessidades feito com a associação.

## Tecnologias

- Python 3.10 ou superior
- [FastAPI](https://fastapi.tiangolo.com/) (API)
- [SQLAlchemy](https://www.sqlalchemy.org/) 2.x (acesso ao banco)
- [Alembic](https://alembic.sqlalchemy.org/) (migrações do banco)
- SQLite em desenvolvimento e PostgreSQL planejado para produção

## Como rodar

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Criar as tabelas do banco
alembic upgrade head

# 4. Iniciar a API
uvicorn app.main:app --reload
```

Com a API no ar, abra:

- http://127.0.0.1:8000/ : verificação de status
- http://127.0.0.1:8000/docs : documentação interativa (Swagger)

> Se você já tinha um arquivo `amad.db` criado antes das migrações, apague-o (está vazio) e rode `alembic upgrade head` de novo.

## Configuração do banco de dados

Por padrão o projeto usa SQLite (`amad.db`, criado na raiz). Para usar outro banco, defina a variável de ambiente `DATABASE_URL`:

```bash
# Exemplo PostgreSQL (instale também o driver: pip install "psycopg[binary]")
set DATABASE_URL=postgresql://usuario:senha@servidor:5432/amad          # Windows (cmd)
# export DATABASE_URL=postgresql://usuario:senha@servidor:5432/amad     # Linux / macOS
```

Depois rode `alembic upgrade head` para criar as tabelas no novo banco.

## Migrações

Sempre que alterar um modelo em `app/models/`:

```bash
alembic revision --autogenerate -m "descreva a mudança"
alembic upgrade head
```

Revise o arquivo gerado em `migrations/versions/` antes de aplicar.

## Estrutura do projeto

```
app/
  main.py            # aplicação FastAPI
  database/          # conexão e sessão do banco
  models/            # modelos SQLAlchemy (tabelas)
migrations/          # histórico de migrações (Alembic)
docs/                # documentação (arquitetura e decisões)
```

## Plano de desenvolvimento

- [x] Base da API e modelo de usuários com perfis (ADMIN, AUDITOR, PARCEIRO, PUBLICO)
- [ ] Cadastro de usuário e login com senha criptografada
- [ ] Controle de acesso por perfil
- [ ] Cadastro de membros
- [ ] Registro de atividades
- [ ] Projetos e tarefas
- [ ] Painel e relatório de impacto
- [ ] Suporte a várias associações (multi-tenant), se o projeto evoluir além do piloto

## Segurança e privacidade

- Nunca versione arquivos `.db` nem `.env` (já estão no `.gitignore`).
- O sistema deve coletar apenas os dados pessoais estritamente necessários (LGPD).
