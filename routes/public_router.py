import bcrypt
from fastapi import APIRouter, Form, Path, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario_model import Usuario
from repositories.livro_repo import LivroRepo
from repositories.usuario_repo import UsuarioRepo
from util.mensagens import *

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

#rota para a biblioteca do sistema, com todos os livros cadastrados
@router.get("/biblioteca", name="biblioteca")
def get_lar(request: Request):
    livros = LivroRepo.obter_todos_livro()
    response = templates.TemplateResponse("biblioteca.html", {"request": request, "livros": livros})
    return response

@router.get("/livro/{id}")
def get_livro(request: Request, id: int = Path(...)):
    livro = LivroRepo.obter_livro_por_id(id)
    response = templates.TemplateResponse(
        "/livro.html", {"request": request, "l": livro})
    return response

#rota para a página de estante do usuário
@router.get("/estante", name="estante")
def get_login(request: Request): 
    response = templates.TemplateResponse("estante.html", {"request": request})
    return response

#rota para as configurações, seja de conta ou do comportamento do site
@router.get("/conf")
def get_configuracao(request: Request):
    response = templates.TemplateResponse("conf.html", {"request": request})
    return response

@router.get("/login", name="login")
def get_login(request: Request):
    response = templates.TemplateResponse(
        "login.html", {"request": request})
    return response

@router.post("/login")
def post_login(
    request: Request, 
    matricula: str = Form(),
    senha: str = Form()):
    senha_hash = UsuarioRepo.obter_senha_por_matricula(matricula)
    # se não encontrou senha para o e-mail, 
    # é porque não está cadastrado
    if not senha_hash:
        response = RedirectResponse("/login", 303)
        adicionar_mensagem_erro(response, "Credenciais inválidas!")
        return response
    # se encontrou senha e ela não confere com a cadastrada,
    # permanece no formulário de login
    if not bcrypt.checkpw(senha.encode(), senha_hash.encode()):
        response = RedirectResponse("/login", 303)
        adicionar_mensagem_erro(response, "Credenciais inválidas!")
        return response
    # se encontrou o usuário e a senha confere,
    # cria a sessão e manda o usuário para a página principal
    usuario = UsuarioRepo.obter_dados_por_matricula(matricula)
    request.session["usuario"] = {
        "matricula": usuario.matricula
    }
    response = RedirectResponse("/", 303)
    adicionar_mensagem_sucesso(response, f"Olá, <b>{usuario.matricula}</b>. Você está autenticado!")
    return response   
    
@router.get("/sair", name="sair")
def get_sair(request: Request):
    request.session.clear()
    response = RedirectResponse("/", 303)
    adicionar_mensagem_info(response, "Você não está mais autenticado.")
    return response

@router.get("/cadastro", name="cadastro")
def get_cadastro(request: Request):
    response = templates.TemplateResponse(
        "cadastro.html", {"request": request})
    return response

@router.post("/cadastro")
def post_cadastro(
    request: Request, 
    matricula: str = Form(pattern='^\d{5}[a-z]{2}\d{3}$'),
    senha: str = Form()):
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    novo_usuario = Usuario(None, matricula, senha_hash.decode())
    novo_usuario = UsuarioRepo.inserir(novo_usuario)
    if novo_usuario:
        response = RedirectResponse("/login", 303)
        adicionar_mensagem_sucesso(response, "Cadastro realizado com sucesso! Use suas credenciais para entrar.")
        return response
    else:
        response = RedirectResponse("/cadastro", 303)
        adicionar_mensagem_erro(response, "Ocorreu algum problema ao tentar realizar seu cadastro. Tente novamente.")
        return response