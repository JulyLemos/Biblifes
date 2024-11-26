from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from repositories import livro_repo, usuario_repo
from routes.admin_router import router as admin_router
from routes.public_router import router as public_router

usuario_repo.UsuarioRepo.criar_tabela_usuario()
usuario_repo.UsuarioRepo.inserir_usuarios_iniciais()
livro_repo.LivroRepo.criar_tabela_livro()
livro_repo.LivroRepo.inserir_livros_iniciais()


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
app.include_router(public_router)
app.include_router(admin_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)