from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float = Field(..., gt=0)
    quantidade: int = Field(..., ge=0)

