from pydantic import BaseModel
from typing import List


class PokemonResponse(BaseModel):
    name: str
    id: int
    types: List[str]
