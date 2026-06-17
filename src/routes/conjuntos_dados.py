from fastapi import APIRouter, HTTPException

from src.services.ckan_service import CKANService
from src.schemas.conjunto_dados import (
    ConjuntoDadosCreate,
    ConjuntoDadosUpdate
)

router = APIRouter()

@router.get("/")
def listar_conjunto_de_dados():
    return CKANService().listar_datasets()

@router.get("/{dataset_id}")
def obter_conjunto_dados(dataset_id: str):
    return CKANService().obter_dataset(dataset_id)

@router.post("/")
def criar_conjunto_dados(dataset: ConjuntoDadosCreate):
    try:
        return CKANService().criar_dataset(
            **dataset.model_dump()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{dataset_id}")
def atualizar_conjunto_dados(dataset_id: str, dataset: ConjuntoDadosUpdate):
    try:
        dados = dataset.model_dump(exclude_unset=True)
        dados["id"] = dataset_id

        return CKANService().atualizar_dataset(
            **dados
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{dataset_id}")
def excluir_conjunto_dados(dataset_id: str):
    try:
        return CKANService().excluir_dataset(
            dataset_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))