from typing import List, Optional
from models.livro_model import Livro
from sql.livro_sql import SQL_CRIAR_TABELA_LIVRO, SQL_INSERIR_LIVRO, SQL_OBTER_TODOS_LIVRO
from util import obter_conexao


def criar_tabela_livro():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA_LIVRO)

def inserir_livro(livro: Livro) -> Optional[Livro]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_INSERIR_LIVRO, 
            (livro.titulo,
            livro.autor,
            livro.ano,
            livro.paginas,
            livro.edicao,
            livro.idioma,
            livro.editora,
            livro.isbn,
            livro.genero1,
            livro.genero2,
            livro.sinopse,))
        if db.rowcount > 0:
            livro.id = db.lastrowid
            return livro
        else:
            return None

def obter_todos_livro() -> List[Livro]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        tuplas = db.execute(SQL_OBTER_TODOS_LIVRO).fetchall()
        livros = [Livro(*t) for t in tuplas]
        return livros