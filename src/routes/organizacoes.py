from fastapi import APIRouter
from src.services.ckan_service import CKANService
from src.schemas.organizacao import (
    OrganizacaoCreate,
    OrganizacaoResponse,
    OrganizacaoUpdate
)

router = APIRouter()

# ====================
# Organizações
# ====================

# Lista Organizações
@router.get("/", response_model=list[OrganizacaoResponse])
def listar_organizacoes():
    return CKANService().listar_organizacoes()

# Cria Organização
@router.post("/", response_model=OrganizacaoResponse)
def criar_organizacao(org: OrganizacaoCreate):
    return CKANService().criar_organizacao(
        **org.model_dump()
    )

# Buscar Organização
@router.get("/{org_id}")
def obter_organizacao(org_id: str):
    return CKANService().obter_organizacao(org_id)

# Atualizar Organização
@router.put("/{org_id}")
def atualizar_organizacao(
    org_id: str,
    org: OrganizacaoUpdate
):
    dados = org.model_dump()
    dados["id"] = org_id

    return CKANService().atualizar_organizacao(
        **dados
    )

# Deletar Organização
@router.delete("/{org_id}")
def excluir_organizacao(org_id: str):
    return CKANService().excluir_organizacao(
        org_id
)
