from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Consumo():
    id: Optional[int]= None
    id_usuario: Optional[int]=None
    data_consumo: Optional[date]= None
    quantidade:Optional[int]=None
    tipo:Optional[str]=None