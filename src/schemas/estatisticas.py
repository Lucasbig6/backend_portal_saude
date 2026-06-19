from pydantic import BaseModel
from typing import List


class OrganizacaoAtiva(BaseModel):
    nome: str
    datasets: int


class EstatisticasResponse(BaseModel):
    total_datasets: int
    total_organizacoes: int
    total_grupos: int
    total_tags: int

    datasets_recentes: int

    organizacoes_mais_ativas: List[OrganizacaoAtiva]

    tags_populares: List[str]