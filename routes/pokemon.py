from fastapi import APIRouter, Request
from services.pokeapi import get_pokemon_data
from middleware.rate_limit import rate_limit
from auth.api_key import verify_api_key

router = APIRouter()

@router.get("/{pokemon}")
async def get_pokemon(pokemon: str, request: Request):
    verify_api_key(request.headers.get("x-api-key"))  #  autenticacao
    await rate_limit(request)                         #  rate limit
    return get_pokemon_data(pokemon)