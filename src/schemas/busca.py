from pydantic import BaseModel
from typing import Any, List


class BuscaResponse(BaseModel):
    total: int
    page: int
    limit: int
    total_paginas: int
    resultados: List[Any]