from fastapi import APIRouter, UploadFile, File, Form
from src.services.ckan_service import CKANService

router = APIRouter()

service = CKANService()


@router.post("/")
async def upload_arquivo(
    package_id: str = Form(...),
    arquivo: UploadFile = File(...),
    nome: str | None = Form(None),
    descricao: str | None = Form(None)
):

    resultado = service.upload_resource(
        package_id=package_id,
        file=arquivo.file,
        name=nome or arquivo.filename,
        description=descricao
    )

    return resultado