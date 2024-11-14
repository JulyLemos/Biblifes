from typing import List, Optional
from models.usuario_model import Usuario
from sql.usuario_sql import SQL_CRIAR_TABELA_USUARIO, SQL_INSERIR_USUARIO, SQL_OBTER_TODOS_USUARIO
from util import obter_conexao

def criar_tabela_usuario():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA_USUARIO)

def inserir_usuario(usuario: Usuario) -> Optional[Usuario]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        try:
            db.execute(SQL_INSERIR_USUARIO, (usuario.matricula, usuario.senha))
            if db.rowcount > 0:
                usuario.id = db.lastrowid
                return usuario
            else:
                print("Inserção falhou, nenhum usuário foi inserido.")
                return None
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
            return None

def obter_todos() -> List[Usuario]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        tuplas = db.execute(SQL_OBTER_TODOS_USUARIO).fetchall()
        usuarios = [Usuario(*t) for t in tuplas]
        return usuarios