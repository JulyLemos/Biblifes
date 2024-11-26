from typing import List, Optional
from models.livro_model import LivroModel
from sql.livro_sql import *
from utils.db import obter_conexao

class LivroRepo:
    @staticmethod
    def criar_tabela_livro():
        with obter_conexao() as conexao:
            db = conexao.cursor()
            db.execute(SQL_CRIAR_TABELA_LIVRO)
    
    @staticmethod
    def inserir_livro(livro: LivroModel) -> Optional[LivroModel]:
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
                livro.sinopse))
            if db.rowcount > 0:
                livro.id = db.lastrowid
                return livro
            else:
                return None

    @staticmethod
    def alterar_livro(livro: LivroModel) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ALTERAR_LIVRO,
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
                livro.sinopse,
                livro.id))
            if cursor.rowcount > 0:
                return True
            else:
                return False

    @staticmethod
    def excluir_livro(id_livro: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR_LIVRO, (id_livro,))
            if cursor.rowcount > 0:
                return True
            else:
                return False

    @staticmethod
    def obter_livro_por_id(id_livro: int) -> Optional[LivroModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_LIVRO_POR_ID, (id_livro,))
            linha = cursor.fetchone()
            if linha:
                return LivroModel(
                    id=linha["id"],
                    titulo=linha["titulo"],
                    autor=linha["autor"],
                    ano=linha["ano"],
                    paginas=linha["paginas"],
                    edicao=linha["edicao"],
                    idioma=linha["idioma"],
                    editora=linha["editora"],
                    isbn=linha["isbn"],
                    genero1=linha["genero1"],
                    genero2=linha["genero2"],
                    sinopse=linha["sinopse"])
            else:
                return None

    @staticmethod
    def obter_todos_livro() -> List[LivroModel]:
        with obter_conexao() as conexao:
            db = conexao.cursor()
            tuplas = db.execute(SQL_OBTER_TODOS_LIVRO).fetchall()
            livros = [LivroModel(*t) for t in tuplas]
            return livros
        
    @staticmethod
    def inserir_livros_iniciais():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) AS count FROM livros;")
            count = cursor.fetchone()[0]
            if count > 0:
                return
            livros_iniciais = [
                ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223, 1, "Português", "Rocco", "9788532511010", "Fantasia", "Aventura",
                "Harry Potter descobre que é um bruxo e embarca em uma aventura em Hogwarts."),
                ("Harry Potter e a Câmara Secreta", "J.K. Rowling", 1998, 251, 1, "Português", "Rocco", "9788532512024", "Fantasia", "Aventura",
                "Harry retorna a Hogwarts e precisa enfrentar os perigos da Câmara Secreta."),
                ("Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling", 1999, 318, 1, "Português", "Rocco", "9788532512055", "Fantasia", "Aventura",
                "Harry descobre mais sobre seu passado e enfrenta Sirius Black."),
                ("Harry Potter e o Cálice de Fogo", "J.K. Rowling", 2000, 535, 1, "Português", "Rocco", "9788532512062", "Fantasia", "Aventura",
                "Harry participa do Torneio Tribruxo e enfrenta desafios perigosos."),
                ("Harry Potter e a Ordem da Fênix", "J.K. Rowling", 2003, 702, 1, "Português", "Rocco", "9788532512079", "Fantasia", "Aventura",
                "Harry lida com a opressão do Ministério e organiza a Armada de Dumbledore."),
                ("Harry Potter e o Enigma do Príncipe", "J.K. Rowling", 2005, 512, 1, "Português", "Rocco", "9788532512086", "Fantasia", "Mistério",
                "Harry descobre os segredos de Voldemort enquanto se prepara para a batalha final."),
                ("Harry Potter e as Relíquias da Morte", "J.K. Rowling", 2007, 607, 1, "Português", "Rocco", "9788532512093", "Fantasia", "Aventura",
                "Harry, Rony e Hermione partem em busca das Horcruxes para derrotar Voldemort."),
                ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96, 1, "Português", "Agir", "9788522031444", "Fábula", "Filosofia",
                "A história de um pequeno príncipe e suas reflexões sobre a vida e o amor."),
                ("A Culpa é das Estrelas", "John Green", 2012, 288, 1, "Português", "Intrínseca", "9788580572261", "Romance", "Drama",
                "Dois adolescentes com câncer se apaixonam e refletem sobre a vida e a morte."),
                ("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005, 400, 1, "Português", "Intrínseca", "9788580570878", "Fantasia", "Aventura",
                "Percy descobre que é um semideus e precisa impedir uma guerra entre os deuses."),
                ("1984", "George Orwell", 1949, 328, 1, "Português", "Companhia das Letras", "9788535914848", "Distopia", "Ficção Científica",
                "Em um regime totalitário, Winston Smith luta contra a opressão do Grande Irmão."),
                ("O Hobbit", "J.R.R. Tolkien", 1937, 310, 1, "Português", "HarperCollins", "9780007440849", "Fantasia", "Aventura",
                "Bilbo Bolseiro parte em uma jornada para recuperar um tesouro guardado por um dragão."),
                ("Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 576, 1, "Português", "Martins Fontes", "9788533616270", "Fantasia", "Aventura",
                "Frodo inicia sua jornada para destruir o Um Anel e salvar a Terra Média."),
                ("Dom Quixote", "Miguel de Cervantes", 1605, 1072, 1, "Português", "Penguin", "9780142437230", "Clássico", "Aventura",
                "A história de um cavaleiro que decide viver aventuras heroicas em um mundo realista."),
                ("Orgulho e Preconceito", "Jane Austen", 1813, 435, 1, "Português", "Martins Fontes", "9788533616973", "Romance", "Clássico",
                "Elizabeth Bennet e Mr. Darcy enfrentam barreiras sociais e emocionais em sua história de amor."),
                ("O Código Da Vinci", "Dan Brown", 2003, 489, 1, "Português", "Sextante", "9788575421137", "Mistério", "Suspense",
                "Robert Langdon desvenda segredos religiosos enquanto investiga um assassinato no Louvre."),
                ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, 224, 1, "Português", "Editora do Autor", "9780316769488", "Romance", "Ficção",
                "Holden Caulfield reflete sobre a vida enquanto explora Nova York."),
                ("As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis", 1950, 206, 1, "Português", "Martins Fontes", "9788578273429", "Fantasia", "Infantil",
                "Quatro irmãos descobrem o mundo mágico de Nárnia e enfrentam a Feiticeira Branca.")
            ]
            for titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse in livros_iniciais:
                cursor.execute(SQL_INSERIR_LIVRO, (titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse))
            db.commit()
