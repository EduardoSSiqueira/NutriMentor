from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.Usuario import Usuario
from util.seguranca import obter_usuario_logado


router = APIRouter()
templates= Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(
    request: Request,
    usuario: Usuario = Depends (obter_usuario_logado),
):
    return templates.TemplateResponse(
        "root/Cadastro_User.html",
        {"request": request,"usuario" : usuario},
    )



@router.get("/login", response_class=HTMLResponse)
async def get_login(
    request: Request,
    usuario: Usuario = Depends(obter_usuario_logado),
    ):
    return templates.TemplateResponse(
        "root/login.html",
        {"request": request, "usuario": usuario},
    )