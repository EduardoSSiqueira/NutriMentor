from re import template
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from repositories.ConsumoRepo import ConsumoRepo
from repositories.SuplementoRepo import SuplementoRepo
from repositories.UsuarioRepo import UsuarioRepo
from routes.RootRouter import router as rootRouter
from util. seguranca import atualizar_cookie_autenticacao


UsuarioRepo.criar_tabela()
UsuarioRepo.criar_administrador_padrao()
UsuarioRepo.criar_usuario_padrao()

ConsumoRepo.criar_tabela()
SuplementoRepo.criar_tabela()

SuplementoRepo.inserir_suplemento_json("sql/suplementos.json")



app = FastAPI()
app.middleware("http")(atualizar_cookie_autenticacao)

app.mount(path="/static", app=StaticFiles(directory="static"),name="static")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(rootRouter)


if __name__=="__main__":
    uvicorn.run(app="main:app", reload=True)


    