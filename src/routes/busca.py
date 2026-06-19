from fastapi import APIRouter, Query
from src.services.ckan_service import CKANService
from src.schemas.busca import BuscaResponse

import math

router = APIRouter()

service = CKANService()


@router.get(
    "/",
    response_model=BuscaResponse,
    summary="Buscar conjuntos de dados"
)
def buscar(
    q: str = Query(..., description="Termo de busca"),
    page: int = Query(1, ge=1, description="Página"),
    limit: int = Query(20, ge=1, le=100, description="Quantidade por página")
):

    resultado = service.buscar(
        termo=q,
        page=page,
        limit=limit
    )

    if "error" in resultado:
        return resultado

    total = resultado["count"]

    return BuscaResponse(
        total=total,
        page=page,
        limit=limit,
        total_paginas=math.ceil(total / limit),
        resultados=resultado["results"]
    )