from pydantic import BaseModel
from typing import Optional

class ConjuntoDadosCreate(BaseModel):
    name: str
    title: str
    notes: Optional[str]
    owner_org: str

class ConjuntoDadosUpdate(BaseModel):
    title: Optional[str] = None
    notes: Optional[str] = None

class ConjuntoDadosResponse(BaseModel):
    id: str
    name: str
    title: str
    notes: Optional[str] = None
    owner_org: str
    state: str