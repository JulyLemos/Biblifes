from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
from repositories import livro_repo, usuario_repo
from routes.admin_router import router as admin_router
from routes.public_router import router as public_router

usuario_repo.UsuarioRepo.criar_tabela_usuario()
livro_repo.LivroRepo.criar_tabela_livro()
livro_repo.LivroRepo.inserir_livros_iniciais()

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="4b4106088eb972ea5495e9d6ff82fe474aee15e75ebcf630100845d16306ebb0d7dadd6e54a8f95169053db3ab6ccd738fcb69902f8ca5641986d6e2888cc319")

app.mount("/static", StaticFiles(directory="static"))
app.include_router(public_router)
app.include_router(admin_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)