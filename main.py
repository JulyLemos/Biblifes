from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.public_router import router as public_router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
app.include_router(public_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)