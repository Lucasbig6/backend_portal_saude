from fastapi import FastAPI

from src.routes.organizacoes import router as org_router
from src.routes.conjuntos_dados import router as cd_router
from src.routes.resources import router as resources_router
from src.routes.grupos import router as grupos_router
from src.routes.tags import router as tags_router
from src.routes.busca import router as busca_router
from src.routes.upload import router as upload_router
from src.routes.estatisticas import router as estatisticas_router

app = FastAPI(
    title="Portal de Dados da Saúde API",
    description="Camada de conexão entre o CKAN e frontend.",
    version="1.0.0"
)

app.include_router(
    org_router,
    prefix="/api/v1/organizacoes",
    tags=["Organizações"]
)

app.include_router(
    cd_router,
    prefix="/api/v1/conjuntos-dados",
    tags=["Conjuntos de dados"]
)

app.include_router(
    resources_router,
    prefix="/api/v1/recursos",
    tags=["Recursos / Arquivos"]
)

app.include_router(
    grupos_router,
    prefix="/api/v1/grupos",
    tags=["Grupos"]
)

app.include_router(
    tags_router,
    prefix="/api/v1/tags",
    tags=["Tags"]
)

app.include_router(
    busca_router,
    prefix="/api/v1/busca",
    tags=["Bucar Dados"]
)

app.include_router(
    upload_router,
    prefix="/api/v1/upload",
    tags=["Upload de arquivos"]
)

app.include_router(
    estatisticas_router,
    prefix="/api/v1/estatisticas",
    tags=["Estatísticas"]
)