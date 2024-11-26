SQL_CRIAR_TABELA_USUARIO = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matricula TEXT NOT NULL,
        senha TEXT NOT NULL
    )
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario (
        matricula, senha)
    VALUES (?, ?)
"""

SQL_ALTERAR_USUARIO = """
    UPDATE usuario SET
    matricula=?, senha=?
    WHERE id=?
"""

SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE id=?
"""

SQL_OBTER_USUARIO_POR_ID = """
    SELECT id, matricula, senha
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_TODOS_USUARIO = """
    SELECT id, matricula, senha
    FROM usuario
    ORDER BY matricula
"""