# Backend - Portal de Dados SESAPI

## Visão Geral

O backend do Portal de Dados da SESAPI foi desenvolvido utilizando FastAPI e atua como uma camada intermediária entre o frontend da aplicação e a plataforma CKAN.

Essa abordagem desacopla o frontend da estrutura nativa do CKAN, permitindo a implementação de regras de negócio, controle de acesso, validações e padronização das respostas da API.

## Arquitetura

```text
Frontend
    ↓
FastAPI (Backend)
    ↓
CKAN API
    ↓
PostgreSQL / Solr / File Storage
```

O backend é responsável por:

* Gerenciar a comunicação com a API Action do CKAN.
* Centralizar regras de negócio.
* Validar dados recebidos do frontend.
* Padronizar respostas da aplicação.
* Controlar autenticação e autorização.
* Facilitar futuras integrações com outros sistemas da SESAPI.

## Tecnologias Utilizadas

* Python 3.x
* FastAPI
* Pydantic
* CKAN API (ckanapi)
* Uvicorn
* Requests

## Instalação e Configuração

1. Clone o repositório.
2. Crie um ambiente virtual e instale as dependências.
3. Configure as variáveis de ambiente:

```bash
cp .env.example .env
```
Edite o arquivo `.env` com as credenciais da sua instância CKAN.

## Estrutura do Projeto

```text
src/
├── core/
│   └── config.py
├── schemas/
│   ├── organizacao.py
│   ├── grupo.py
│   ├── conjunto_dados.py
│   └── resource.py
├── routes/
│   ├── organizacoes.py
│   ├── grupos.py
│   ├── conjuntos_dados.py
│   └── resources.py
├── services/
│   └── ckan_service.py
└── main.py
```

## Funcionalidades Implementadas

### Organizações (Setores)

Representam os setores responsáveis pela publicação dos dados.

Funcionalidades:

* Listar organizações
* Consultar organização
* Criar organização
* Atualizar organização
* Excluir organização

### Grupos (Temas)

Representam os temas utilizados para classificação dos conjuntos de dados.

Funcionalidades:

* Listar grupos
* Consultar grupo
* Criar grupo
* Atualizar grupo
* Excluir grupo

### Conjuntos de Dados

Representam os conjuntos de dados publicados pelos setores.

Funcionalidades:

* Listar conjuntos de dados
* Consultar conjunto de dados
* Criar conjunto de dados
* Atualizar conjunto de dados
* Excluir conjunto de dados

### Recursos (Arquivos)

Representam arquivos ou links associados aos conjuntos de dados.

Funcionalidades:

* Listar recursos de um conjunto de dados
* Consultar recurso
* Criar recurso
* Atualizar recurso
* Excluir recurso

## Mapeamento Conceitual

O Portal de Dados utiliza uma nomenclatura adaptada para o contexto institucional da SESAPI:

| CKAN         | Portal SESAPI     |
| ------------ | ----------------- |
| Organization | Setor             |
| Group        | Tema              |
| Dataset      | Conjunto de Dados |
| Resource     | Arquivo / Recurso |

## Integração com CKAN

A comunicação com o CKAN é realizada através da biblioteca `ckanapi`, utilizando autenticação por API Token.

A camada de serviços encapsula todas as chamadas para a API do CKAN, permitindo que o frontend consuma apenas os endpoints disponibilizados pelo backend.

## Próximas Implementações

* Upload de arquivos para recursos
* Busca avançada de conjuntos de dados
* Paginação de resultados
* Controle de autenticação via JWT
* Gestão de usuários
* Logs e auditoria
* Integração com indicadores e painéis da SESAPI

## Objetivo

Fornecer uma API robusta, escalável e desacoplada do CKAN, permitindo a construção de um Portal de Dados moderno para publicação, catalogação e disseminação de informações da Secretaria de Estado da Saúde do Piauí (SESAPI).
