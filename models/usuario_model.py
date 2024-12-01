from dataclasses import dataclass
from typing import Optional

@dataclass
class UsuarioModel:
    id: Optional[int] = None
    matricula: Optional[str]= None
    senha: Optional[str] = None
    perfil: Optional[int] = None