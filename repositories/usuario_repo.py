import sqlite3
from typing import List, Optional
from models.usuario_model import UsuarioModel
from sql.usuario_sql import *
from utils.db import obter_conexao


class UsuarioRepo:
    @staticmethod
    def criar_tabela_usuario():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA_USUARIO)

    @staticmethod
    def inserir_usuario(usuario: UsuarioModel) -> Optional[UsuarioModel]:
        with obter_conexao() as conexao:
            db = conexao.cursor()
            db.execute(SQL_INSERIR_USUARIO, 
            (usuario.matricula, 
            usuario.senha,))
        if db.rowcount == 0:
                return None
        usuario.id = db.lastrowid
        return usuario

    @staticmethod
    def obter_senha_por_matricula(matricula: str) -> Optional[str]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_SENHA_POR_MATRICULA, (matricula,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return dados["senha"]

    @staticmethod
    def obter_dados_por_matricula(matricula: str) -> Optional[UsuarioModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_DADOS_POR_MATRICULA, (matricula,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return UsuarioModel(
                id=dados["id"],  
                matricula=dados["matricula"],
                senha=None)
        
    @staticmethod
    def alterar_usuario(usuario: UsuarioModel) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ALTERAR_USUARIO, (
                usuario.matricula,
                usuario.senha,
                usuario.id,))
            if cursor.rowcount == 0:
                return False
            return True
            
    @staticmethod
    def excluir_usuario(id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR_USUARIO, (id,))
            return cursor.rowcount > 0
            
    @staticmethod
    def obter_usuario_por_id(id: int) -> Optional[UsuarioModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_USUARIO_POR_ID, (id,))
            linha = cursor.fetchone()
            if linha:
                return UsuarioModel(
                    id=linha["id"],
                    matricula=linha["matricula"],
                    senha=linha["senha"])
            else:
                return None
            
    @staticmethod
    def obter_todos_usuario() -> List[UsuarioModel]:
        with obter_conexao() as conexao:
            db = conexao.cursor()
            tuplas = db.execute(SQL_OBTER_TODOS_USUARIO).fetchall()
            livros = [UsuarioModel(*t) for t in tuplas]
            return livros