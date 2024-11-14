from dataclasses import dataclass
from typing import Optional

@dataclass
class Livro:
    id: Optional[int] = None
    titulo: Optional[str] = None
    autor: Optional[str] = None
    ano: Optional[int] = None
    paginas: Optional[int] = None
    edicao: Optional[str] = None
    idioma: Optional[str] = None
    editora: Optional[str] = None
    isbn: Optional[str] = None
    genero1: Optional[str] = None
    genero2: Optional[str] = None
    sinopse: Optional[str] = None