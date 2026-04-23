 API de Consulta de Pokémon

API REST desenvolvida em **Python com FastAPI**, responsável por consumir dados da PokéAPI, com implementação de cache em Redis, controle de acesso via API Key e rate limiting por usuário.

---

 Tecnologias utilizadas

* Python
* FastAPI
* Redis
* Requests
* Uvicorn

---

 Funcionalidades

* Consulta de dados de Pokémon via PokéAPI
* Cache com Redis para otimização de performance
* Controle de acesso via API Key
* Rate limiting por IP para limitar requisições
* Tratamento de erros com códigos HTTP adequados
* Transformação dos dados retornados pela API externa

---

 Estrutura do projeto

```
ProjetoAPI/
│
├── main.py
├── routes/
│   └── pokemon.py
├── services/
│   └── pokeapi.py
├── cache/
│   └── redis_client.py
├── middleware/
│   └── rate_limit.py
├── auth/
│   └── api_key.py
└── .env
```

---

 Como executar o projeto

 1. Clonar o repositório

```
git clone https://github.com/davicode20/pokemon-api-fastapi.git
cd pokemon-api-fastapi
```

---

 2. Criar e ativar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

---

 3. Instalar dependências

```
pip install fastapi uvicorn redis requests python-dotenv
```

---

 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
API_KEY=123456
```

---

 5. Iniciar o Redis

No WSL ou ambiente Linux:

```
redis-server
```

Ou em segundo plano:

```
redis-server --daemonize yes
```

---

 6. Executar a aplicação

```
py -m uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

 Uso da API

 Endpoint

```
GET /pokemon/{nome}
```

Exemplo:

```
http://127.0.0.1:8000/pokemon/pikachu
```

---

 Header obrigatório

```
x-api-key: 123456
```

---

 Comportamento da aplicação

* Primeira requisição: consulta a PokéAPI e armazena em cache
* Requisições subsequentes: retorno direto do Redis
* Limite de requisições: retorna HTTP 429
* API Key inválida: retorna HTTP 401
* Pokémon não encontrado: retorna HTTP 404

---

 Exemplos de resposta

 Sucesso (200)

```json
{
  "name": "pikachu",
  "id": 25,
  "types": ["electric"]
}
```

---

 Não encontrado (404)

```json
{
  "detail": "Pokémon não encontrado"
}
```

---

 Não autorizado (401)

```json
{
  "detail": "API Key inválida ou não fornecida."
}
```

---

 Rate limit (429)

```json
{
  "detail": "Muitas requisições. Tente novamente mais tarde."
}
```

---

 Conceitos aplicados

* Arquitetura em camadas (routes, services, middleware, cache)
* Integração com API externa
* Cache com Redis
* Rate limiting por IP
* Autenticação via API Key
* Boas práticas com códigos de status HTTP

---

## Autor

Davi
[https://github.com/davicode20](https://github.com/davicode20)

