from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.Usuario import Usuario
from repositories.UsuarioRepo import UsuarioRepo
from util.seguranca import (
    obter_usuario_logado,
)

router = APIRouter(prefix="/usuario")
templates = Jinja2Templates(directory="templates")

@router.get("/Menu", response_class=HTMLResponse)
async def get_index(
        request: Request,
        usuario: Usuario=Depends(obter_usuario_logado),
):
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    usuarios = UsuarioRepo.obter_todos()
    return templates.TemplateResponse(
        "usuario/dashboard.html",
        {"request":request, "usuario":usuario, "usuarios":usuarios},
)