from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from repositories.livro_repo import LivroRepo
from repositories.usuario_repo import UsuarioRepo
from routes.admin_router import router as admin_router
from routes.public_router import router as public_router

LivroRepo.criar_tabela_livro()
LivroRepo.inserir_livros_iniciais()
UsuarioRepo.criar_tabela()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
app.add_middleware(SessionMiddleware, secret_key="4b4106088eb972ea5495e9d6ff82fe474aee15e75ebcf630100845d16306ebb0d7dadd6e54a8f95169053db3ab6ccd738fcb69902f8ca5641986d6e2888cc319")
app.include_router(public_router)
app.include_router(admin_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)