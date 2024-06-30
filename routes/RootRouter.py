from fastapi import APIRouter, Depends, Form, Query, Request , status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.Usuario import Usuario
from repositories.UsuarioRepo import UsuarioRepo
from util.mensagem import redirecionar_com_mensagem
from util.seguranca import conferir_senha, gerar_token, obter_usuario_logado, atualizar_cookie_autenticacao, adicionar_cookie_autenticacao,obter_usuario_logado


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


@router.get("/Menu", response_class=HTMLResponse)
async def get_root(
    request: Request,
    usuario: Usuario = Depends (obter_usuario_logado),
):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request,"usuario" : usuario},
    )

@router.get("/cadastroSuplemento", response_class=HTMLResponse)
async def get_templates(
    request: Request,
    usuario: Usuario = Depends (obter_usuario_logado),
):
    return templates.TemplateResponse(
        "cadastroSuplemento.html",
        {"request": request,"usuario" : usuario},
    )

@router.get("/perfil", response_class=HTMLResponse)
async def get_templates(
    request: Request,
    usuario: Usuario = Depends (obter_usuario_logado),
):
    return templates.TemplateResponse(
        "perfil.html",
        {"request": request,"usuario" : usuario},
    )

@router.get("/RegistroConsumo", response_class=HTMLResponse)
async def get_templates(
    request: Request,
    usuario: Usuario = Depends (obter_usuario_logado),
):
    return templates.TemplateResponse(
        "registro_consumo.html",
        {"request": request,"usuario" : usuario},
    )

@router.get("/SobreProjeto", response_class=HTMLResponse)
async def get_templates(
    request: Request,
    usuario: Usuario = Depends (obter_usuario_logado),
):
    return templates.TemplateResponse(
        "sobre.html",
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


@router.post("/login", response_class=RedirectResponse)
async def post_login(
    email: str = Form(...),
    senha: str = Form(...),
    return_url: str = Query("/Menu"),
):
    hash_senha_bd = UsuarioRepo.obter_senha_por_email(email)
    
    if hash_senha_bd is None:
        response = redirecionar_com_mensagem(
            "/login",
            "Credenciais inválidas. Tente novamente.",
        )
        return response

    if conferir_senha(senha, hash_senha_bd):
        token = gerar_token()
        UsuarioRepo.alterar_token_por_email(token, email)
        response = RedirectResponse(return_url, status.HTTP_302_FOUND)
        adicionar_cookie_autenticacao(response, token)
    else:
        response = redirecionar_com_mensagem(
            "/login",
            "Credenciais inválidas. Tente novamente.",
        )
    return response
