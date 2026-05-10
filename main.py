from fastapi import FastAPI
from routes.pokemon import router as pokemon_router
from dotenv import load_dotenv

# aqui liga tudo

# aqui carregar variaveis de ambiente
load_dotenv()

app = FastAPI()

app.include_router(pokemon_router, prefix="/pokemon")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "api": "pokemon-api",
        "version": "1.0.0"
    }