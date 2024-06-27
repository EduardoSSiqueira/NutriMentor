from dataclasses import dataclass
from typing import Optional


@dataclass
class Suplemento():
    id: Optional[int]= None
    nome: Optional[str]= None
    marca:Optional[str]=None
    tipo:Optional[str]=None