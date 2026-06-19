from pydantic import BaseModel
from typing import Optional, List


class Tag(BaseModel):
    name: str


class ConjuntoDadosCreate(BaseModel):
    name: str
    title: str
    notes: Optional[str] = None
    owner_org: str

    tags: List[Tag] = []

    version: Optional[str] = None
    license_id: Optional[str] = None

    author: Optional[str] = None
    author_email: Optional[str] = None

    maintainer: Optional[str] = None
    maintainer_email: Optional[str] = None


class ConjuntoDadosUpdate(BaseModel):
    title: Optional[str] = None
    notes: Optional[str] = None
    tags: Optional[List[Tag]] = None


class ConjuntoDadosResponse(BaseModel):
    id: str
    name: str
    title: str
    notes: Optional[str] = None
    owner_org: str
    state: str
    tags: List[Tag] = []

    