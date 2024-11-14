SQL_CRIAR_TABELA_LIVRO = """
    CREATE TABLE IF NOT EXISTS livros ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        paginas INTEGER NOT NULL,
        edicao TEXT NOT NULL,
        idioma TEXT NOT NULL,
        editora TEXT NOT NULL,
        isbn TEXT NOT NULL,
        genero1 TEXT NOT NULL,
        genero2 TEXT NOT NULL,
        sinopse TEXT NOT NULL
    )
"""

SQL_INSERIR_LIVRO = """
    INSERT INTO livros (
       titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_ALTERAR_LIVRO = """
    UPDATE livros SET
    titulo=?, autor=?, ano=?, paginas=?, edicao=?, idioma=?, editora=?, isbn=?, genero1=?, genero2=?, sinopse=?
    WHERE id=?
"""

SQL_EXCLUIR_LIVRO = """
    DELETE FROM livros
    WHERE id=?
"""
SQL_OBTER_POR_ID = """
    SELECT titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse
    FROM livros
    WHERE id=?
"""

SQL_OBTER_TODOS_LIVRO = """
    SELECT id, titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse
    FROM livros
    ORDER BY titulo
"""