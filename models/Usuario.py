from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Usuario:
    id:Optional[int] = None
    nome: Optional[str]=None
    CPF: Optional[str]=None
    data_nascimento :Optional[date]=None
    endereço: Optional[date]=None
    email: Optional[str]=None
    telefone: Optional[str]=None
    senha: Optional[str]=None
    token: Optional[str]=None
