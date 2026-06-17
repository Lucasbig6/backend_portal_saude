from fastapi import APIRouter, HTTPException

from src.schemas.resource import ResourceCreate
from src.services.ckan_service import CKANService

router = APIRouter()
service = CKANService()


@router.get("/dataset/{dataset_id}")
def listar_resources_dataset(dataset_id: str):
    try:
        return service.listar_resources_dataset(dataset_id)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/dataset/{dataset_id}")
def criar_resource(
    dataset_id: str,
    resource: ResourceCreate
):
    try:
        dados = resource.model_dump()
        dados["package_id"] = dataset_id

        return service.criar_resource(**dados)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/{resource_id}")
def obter_resource(resource_id: str):
    try:
        return service.obter_resource(resource_id)

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put("/{resource_id}")
def atualizar_resource(
    resource_id: str,
    resource: ResourceCreate
):
    try:
        dados = resource.model_dump()
        dados["id"] = resource_id

        return service.atualizar_resource(**dados)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{resource_id}")
def excluir_resource(resource_id: str):
    try:
        return service.excluir_resource(resource_id)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )