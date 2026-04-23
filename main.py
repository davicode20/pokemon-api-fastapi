from fastapi import FastAPI #importo a api
from routes.pokemon import router as pokemon_router

app = FastAPI()

app.include_router(pokemon_router, prefix="/pokemon")

#liga o servidor e conecta os modulos
