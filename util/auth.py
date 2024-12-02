from fastapi import HTTPException, Request


async def checar_autenticacao(request: Request, call_next):
    if "usuario" not in request.session:
        raise HTTPException(status_code=401, detail="Não autenticado")
    response = await call_next(request)
    return response

def verificar_autenticacao(request: Request):
    if "usuario" not in request.session:
        return False
    return True