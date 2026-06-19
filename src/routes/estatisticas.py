from fastapi import APIRouter

from src.services.ckan_service import CKANService
from src.schemas.estatisticas import EstatisticasResponse

router = APIRouter()

service = CKANService()


@router.get(
    "/",
    response_model=EstatisticasResponse,
    summary="Dashboard do portal"
)
def obter_estatisticas():
    return service.obter_estatisticas()