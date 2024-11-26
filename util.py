import sqlite3

NOME_PASTA_HTML= "html/"

def ler_html(nome_arquivo: str) -> str:
    caminho_arquivo_html = f"{NOME_PASTA_HTML}{nome_arquivo}.html"
    with open(caminho_arquivo_html, "r", encoding="utf-8") as arquivo:
        conteudo_html = arquivo.read()
    return conteudo_html

def obter_conexao():
    return sqlite3.connect("dados.db")