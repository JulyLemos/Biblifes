from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates


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


#criar arquivos sql
@router.post("/post_cadastro_livros")
def post_cadastro_livros(
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
        return RedirectResponse("/cadastro_livros", 303)
    


#fazer rota de login com sql
