from pydantic import BaseModel
from typing import Optional

class ResourceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    url: str

class ResourceResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    url: str
    package_id: str