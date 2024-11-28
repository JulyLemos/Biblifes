from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.livro_model import LivroModel
from models.usuario_model import UsuarioModel
from repositories import livro_repo, usuario_repo


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/") #rota para página raíz que é o index com as frases
def get_root(request: Request):
    response = templates.TemplateResponse("index.html", {"request": request})
    return response #vai retornar o response que contém o  template jinja com a página html

#rota para página lar
@router.get("/lar", name="lar")
def get_lar(request: Request):
    response = templates.TemplateResponse("lar.html", {"request": request})
    return response

@router.get("/biblioteca", name="biblioteca")
def get_lar(request: Request):
    response = templates.TemplateResponse("biblioteca.html", {"request": request})
    return response

#rota para página de cadastro - com sql e mudando de página para alteração
@router.get("/cadastro", name="cadastro")
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
    usuario = UsuarioModel(None, matricula, senha)
    usuario = usuario_repo.UsuarioRepo.inserir_usuario(usuario)
    if usuario:
        return RedirectResponse("/lar", 303)
    else:
        return RedirectResponse("/cadastro", 303)
    
