from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Consumo():
    id: Optional[int]= None
    id_Usuario: Optional[int]=None
    id_Suplemento:Optional[str]=None
    nome_Suplemento:Optional[str]=None
    nome_Usuario:Optional[str]=None
    data_Consumo: Optional[date]= None
    quantidade:Optional[int]=None