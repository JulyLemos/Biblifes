import sqlite3
from typing import List, Optional
from models.usuario_model import UsuarioModel
from sql.usuario_sql import *
from util import obter_conexao

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
            usuario.senha,
            usuario.perfil,))
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
            print(f"Dados obtidos para a matrícula {matricula}: {dados}")  # Depuração
            if dados is None:
                return None
            return UsuarioModel(
                id=dados["id"],  # Certifique-se de que "id" é o nome correto no banco
                matricula=dados["matricula"],
                senha=None,  # A senha não é retornada aqui
                perfil=dados["perfil"])
        
    @staticmethod
    def alterar_usuario(usuario: UsuarioModel) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ALTERAR_USUARIO, (
                usuario.matricula,
                usuario.senha,
                usuario.perfil,
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
            dados = cursor.fetchone()
            if dados is None:
                return None
            return UsuarioModel(**dados)
            
    @staticmethod
    def obter_todos_usuario() -> List[UsuarioModel]:
        with obter_conexao() as conexao:
            db = conexao.cursor()
            tuplas = db.execute(SQL_OBTER_TODOS_USUARIO).fetchall()
            livros = [UsuarioModel(*t) for t in tuplas]
            return livros
    
    # @staticmethod
    # def inserir_usuarios_iniciais():
    #     with obter_conexao() as db:
    #         cursor = db.cursor()
    #         cursor.execute("SELECT COUNT(*) AS count FROM usuario;")
    #         count = cursor.fetchone()[0]
    #         if count > 0:
    #             return
    #         usuarios_iniciais = [
    #             ("20231in001", "123456"),
    #             ("20231in002", "234567"),
    #             ("20231in003", "345678"),
    #             ("20231in004", "456789"),
    #             ("20231in005", "567890"),
    #             ("20231in006", "678901"),
    #             ("20231in007", "789012"),
    #             ("20231in008", "890123"),
    #             ("20231in009", "901234"),
    #             ("20231in010", "012345")]
    #         for matricula, senha in usuarios_iniciais:
    #             cursor.execute(SQL_INSERIR_USUARIO, (matricula, senha))
    #         db.commit()