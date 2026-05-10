````md
# API de Consulta de Pokémon

API REST desenvolvida com FastAPI para consulta de dados de Pokémon através da PokéAPI. O projeto implementa cache com Redis, autenticação via API Key, rate limiting por IP, validação de respostas com Pydantic e tratamento robusto de erros HTTP.

---

## Tecnologias utilizadas

- Python
- FastAPI
- Redis
- Requests
- Uvicorn
- Pydantic
- Python-dotenv

---

## Funcionalidades

- Consulta de dados de Pokémon via PokéAPI
- Cache com Redis para otimização de performance
- Controle de acesso via API Key
- Rate limiting por IP para limitar requisições
- Tratamento de erros com códigos HTTP adequados
- Transformação e validação dos dados retornados pela API externa
- Timeout para requisições externas
- Health Check endpoint para monitoramento da aplicação

---

## Estrutura do projeto

```text
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
├── schemas/
│   └── pokemon_schema.py
└── .env
````

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/davicode20/pokemon-api-fastapi.git
cd pokemon-api-fastapi
```

---

### 2. Criar e ativar ambiente virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install fastapi uvicorn redis requests python-dotenv pydantic
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
API_KEY=123456
```

---

### 5. Iniciar o Redis

No WSL ou ambiente Linux:

```bash
redis-server
```

Ou em segundo plano:

```bash
redis-server --daemonize yes
```

---

### 6. Executar a aplicação

```bash
py -m uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

---

## Endpoints

### Buscar Pokémon

```http
GET /pokemon/{nome}
```

#### Exemplo

```text
http://127.0.0.1:8000/pokemon/pikachu
```

#### Header obrigatório

```text
x-api-key: 123456
```

---

### Health Check

```http
GET /health
```

#### Resposta

```json
{
  "status": "ok",
  "api": "pokemon-api",
  "version": "1.0.0"
}
```

---

## Comportamento da aplicação

* Primeira requisição: consulta a PokéAPI e armazena em cache
* Requisições subsequentes: retorno direto do Redis
* Limite de requisições: retorna HTTP 429
* API Key inválida: retorna HTTP 401
* Pokémon não encontrado: retorna HTTP 404
* Timeout da API externa: retorna HTTP 504

---

## Exemplos de resposta

### Sucesso (200)

```json
{
  "name": "pikachu",
  "id": 25,
  "types": ["electric"]
}
```

---

### Não encontrado (404)

```json
{
  "detail": "Pokémon não encontrado"
}
```

---

### Não autorizado (401)

```json
{
  "detail": "API Key inválida ou não fornecida."
}
```

---

### Rate limit (429)

```json
{
  "detail": "Muitas requisições. Tente novamente mais tarde."
}
```

---

### Timeout da API externa (504)

```json
{
  "detail": "A PokéAPI demorou para responder."
}
```

---

## Conceitos aplicados

* Arquitetura em camadas (routes, services, middleware, cache)
* Integração com API externa
* Cache com Redis
* Rate limiting por IP
* Autenticação via API Key
* Schemas e validação com Pydantic
* Boas práticas com códigos de status HTTP
* Variáveis de ambiente com `.env`
* Tratamento de timeout em serviços externos

---

## Autor

Davi
GitHub: [https://github.com/davicode20](https://github.com/davicode20)

```
```


