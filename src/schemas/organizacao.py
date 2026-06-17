from pydantic import BaseModel

class OrganizacaoCreate(BaseModel):
    name: str
    title: str
    description: str | None = None

class OrganizacaoResponse(BaseModel):
    id: str
    name: str
    title: str
    description: str | None = None
    package_count: int
    created: str

class OrganizacaoUpdate(BaseModel):
    name: str | None = None
    title: str | None = None
    description: str | None = None