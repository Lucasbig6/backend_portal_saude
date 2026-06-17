from pydantic import BaseModel

class GrupoCreate(BaseModel):
    name: str
    title: str
    description: str | None = None