from fastapi import APIRouter
from src.services.ckan_service import CKANService

router = APIRouter()

service = CKANService()

@router.get("/")
def listar_tags():
    return service.listar_tags()


@router.get("/{tag}")
def obter_tag(tag: str):
    return service.obter_tag(tag)


@router.get("/{tag}/datasets")
def datasets_por_tag(tag: str):
    return service.buscar_datasets_por_tag(tag)