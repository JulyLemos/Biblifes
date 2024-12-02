from fastapi import APIRouter, Form, Path, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.livro_model import LivroModel
from models.usuario_model import UsuarioModel
from repositories.livro_repo import LivroRepo
from repositories.usuario_repo import UsuarioRepo
from utils.mensagens import *

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_root(request: Request):
    livros = LivroRepo.obter_todos_livro()
    response = templates.TemplateResponse(
        "admin/index.html", {"request": request, "livros": livros})
    return response

@router.get("/alterar_livro/{id}")
def get_alterar_livro(request: Request, id: int = Path(...)):
    livro = LivroRepo.obter_livro_por_id(id)
    response = templates.TemplateResponse(
        "admin/alterar_livro.html", {"request": request, "livro": livro}
    )
    return response

@router.post("/alterar_livro/{id}")
def post_alterar_livro(
    request: Request, 
    id: int = Path(...),
    titulo: str = Form(...),
    autor: str = Form(...),
    ano: int = Form(...),
    paginas: int = Form(...),
    edicao: str = Form(...),
    idioma: str = Form(...),
    editora: str = Form(...),
    isbn: str = Form(...),
    genero1: str = Form(...),
    genero2: str = Form(...),
    sinopse: str = Form(...)):
    livro = LivroModel(id, titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse)
    if LivroRepo.alterar_livro(livro):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Livro alterado com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/alterar_livro.html", {"request": request, "livro": livro})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.get("/cadastro_livro")
def get_cadastro_livro(request: Request):
    livro = LivroModel(None, None, None, None, None, None, None, None, None, None, None)
    response = templates.TemplateResponse(
        "admin/cadastro_livro.html", {"request": request, "livro": livro}
    )
    return response

@router.post("/cadastro_livro")
def post_cadastro_livro(
    request: Request,
    titulo: str = Form(...),
    autor: str = Form(...),
    ano: int = Form(...),
    paginas: int = Form(...),
    edicao: str = Form(...),
    idioma: str = Form(...),
    editora: str = Form(...),
    isbn: str = Form(...),
    genero1: str = Form(...),
    genero2: str = Form(...),
    sinopse: str = Form(...)):
    livro = LivroModel(None, titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse)
    if LivroRepo.inserir_livro(livro):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Livro inserido com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/cadastro_livro.html", {"request": request, "livro": livro})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.get("/excluir_livro/{id}")
def get_excluir_livro(request: Request, id: int = Path(...)):
    livro = LivroRepo.obter_livro_por_id(id)
    if livro:
        response = templates.TemplateResponse(
            "admin/excluir_livro.html", {"request": request, "livro": livro}
        )
        return response
    else:
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_erro(response, "O livro que você tentou excluir não existe!")
        return response
    
@router.post("/excluir_livro")
def post_excluir_livro(id: int = Form(...)):
    if LivroRepo.excluir_livro(id):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Livro excluído com sucesso!")
        return response
    else:
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_erro(response, "Não foi possível excluir o livro!")
        return response
    
@router.get("/usuarios")
def get_root(request: Request):
    usuarios = UsuarioRepo.obter_todos_usuario()
    response = templates.TemplateResponse(
        "admin/usuarios.html", {"request": request, "usuarios": usuarios})
    return response

@router.get("/alterar_usuario/{id}")
def get_alterar_usuario(request: Request, id: int = Path(...)):
    usuario = UsuarioRepo.obter_usuario_por_id(id)
    response = templates.TemplateResponse(
        "admin/alterar_usuario.html", {"request": request, "usuario": usuario}
    )
    return response

@router.post("/alterar_usuario/{id}")
def post_alterar_usuario(
    request: Request, 
    id: int = Path(...),
    matricula: str = Form(...),
    senha: str = Form(...)):
    usuario = UsuarioModel(id, matricula, senha)
    if UsuarioRepo.alterar_usuario(usuario):
        response = RedirectResponse("/admin/usuarios", 303)
        adicionar_mensagem_sucesso(response, "Usuario alterado com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/alterar_usuario.html", {"request": request, "usuario": usuario})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.get("/excluir_usuario/{id}")
def get_excluir_usuario(request: Request, id: int = Path(...)):
    usuario = UsuarioRepo.obter_usuario_por_id(id)
    if usuario:
        response = templates.TemplateResponse(
            "admin/excluir_usuario.html", {"request": request, "usuario": usuario}
        )
        return response
    else:
        response = RedirectResponse("/admin/usuarios", 303)
        adicionar_mensagem_erro(response, "O usuario que você tentou excluir não existe!")
        return response
    
@router.post("/excluir_usuario")
def post_excluir_usuario(id: int = Form(...)):
    if UsuarioRepo.excluir_usuario(id):
        response = RedirectResponse("/admin/usuarios", 303)
        adicionar_mensagem_sucesso(response, "Usuario excluído com sucesso!")
        return response
    else:
        response = RedirectResponse("/admin/usuarios", 303)
        adicionar_mensagem_erro(response, "Não foi possível excluir o usuario!")
        return response