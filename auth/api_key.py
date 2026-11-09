from fastapi import Header, HTTPException

API_KEY = "123456"  # desenvolver o .env (x-api-key: 123456)


def verify_api_key(x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida ou não fornecida.")
