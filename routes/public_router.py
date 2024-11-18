from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.livro_model import Livro
from models.usuario_model import Usuario
from repositories import livro_repo, usuario_repo


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/") #rota para página raíz que é o index com as frases
def get_root(request: Request):
    response = templates.TemplateResponse("index.html", {"request": request})
    return response #vai retornar o response que contém o  template jinja com a página html

#rota para página lar
@router.get("/lar")
def get_lar(request: Request):
    response = templates.TemplateResponse("lar.html", {"request": request})
    return response

@router.get("/biblioteca")
def get_lar(request: Request):
    response = templates.TemplateResponse("biblioteca.html", {"request": request})
    return response

#rota para página de cadastro - com sql e mudando de página para alteração
@router.get("/cadastro")
def get_login(request: Request): #mudar depois
    response = templates.TemplateResponse("cadastro.html", {"request": request})
    return response


#rota para página de login - com validação e voltando para página inicial
@router.get("/login")
def get_login(request: Request): #mudar depois
    response = templates.TemplateResponse("login.html", {"request": request})
    return response

@router.post("/post_cadastro")
def post_cadastro(
    matricula: str = Form(...),
    senha: str = Form(...)):
    usuario = Usuario(None, matricula, senha)
    usuario = usuario_repo.inserir_usuario(usuario)
    if usuario:
        return RedirectResponse("/lar", 303)
    else:
        return RedirectResponse("/cadastro", 303)
    
@router.get("/cadastro_livro")
def get_cadastro_livro(request: Request):
    response = templates.TemplateResponse("cadastro_livro.html", {"request": request})
    return response

@router.post("/post_cadastro_livro")
def post_cadastro_livro(
    titulo: str = Form(...),
    autor: str = Form(...),
    ano: str = Form(...),
    paginas: str = Form(...),
    edicao: str = Form(...),
    idioma: str = Form(...),
    editora: str = Form(...),
    isbn: str = Form(...),
    genero1: str = Form(...),
    genero2: str = Form(...),
    sinopse: str = Form(...)):
    livro = Livro(None, titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse)
    livro = livro_repo.inserir_livro(livro)
    if livro:
        return RedirectResponse("/lar", 303)
    else:
        return RedirectResponse("/cadastro_livro", 303)



