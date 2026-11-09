import requests
from fastapi import HTTPException
import json

from cache.redis_client import redis_client


def get_pokemon_data(pokemon: str):

    print("REDIS PING:", redis_client.ping())

    pokemon = pokemon.lower()
    key = f"pokemon:{pokemon}"

    # pra verificar cache
    cache = redis_client.get(key)

    if cache:
        print("VEIO DO CACHE")
        return json.loads(cache)

    # requisição na api externa
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}", timeout=5)

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")

    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao buscar dados da API externa")

    data = r.json()

    formatted_data = {
        "name": data["name"],
        "id": data["id"],
        "types": [t["type"]["name"] for t in data["types"]],
    }

    print("SALVANDO NO CACHE:", key)

    # salvar no redis
    redis_client.set(key, json.dumps(formatted_data), ex=60)

    return formatted_data
