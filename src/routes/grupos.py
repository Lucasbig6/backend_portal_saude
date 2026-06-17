from fastapi import APIRouter, HTTPException

from src.schemas.grupo import GrupoCreate
from src.services.ckan_service import CKANService

router = APIRouter()
service = CKANService()


@router.get("/")
def listar_grupos():
    try:
        return service.listar_grupos()

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/")
def criar_grupo(grupo: GrupoCreate):
    try:
        return service.criar_grupo(
            **grupo.model_dump()
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/{grupo_id}")
def obter_grupo(grupo_id: str):
    try:
        return service.obter_grupo(
            grupo_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put("/{grupo_id}")
def atualizar_grupo(
    grupo_id: str,
    grupo: GrupoCreate
):
    try:
        dados = grupo.model_dump()
        dados["id"] = grupo_id

        return service.atualizar_grupo(
            **dados
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{grupo_id}")
def excluir_grupo(grupo_id: str):
    try:
        return service.excluir_grupo(
            grupo_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )