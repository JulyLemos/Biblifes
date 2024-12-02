SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matricula TEXT NOT NULL,
        senha TEXT NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO usuario (matricula, senha)
    VALUES (?, ?)
"""

SQL_OBTER_SENHA_POR_MATRICULA = """
    SELECT senha
    FROM usuario
    WHERE matricula = ?
"""

SQL_OBTER_DADOS_POR_MATRICULA= """
    SELECT id, matricula
    FROM usuario
    WHERE matricula = ?
"""

SQL_OBTER_POR_ID = """
    SELECT id, matricula
    FROM usuario
    WHERE id = ?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET matricula = ?
    WHERE id = ?
"""

SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha = ?
    WHERE id = ?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario
    WHERE id = ?
"""

SQL_OBTER_TODOS = """
    SELECT id, matricula, senha
    FROM usuario
    ORDER BY matricula
"""