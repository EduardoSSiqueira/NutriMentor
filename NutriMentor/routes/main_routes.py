from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ler_html import ler_html


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/html/{arquivo}")
def get_html(arquivo: str):
    response = HTMLResponse(ler_html(arquivo))
    return response

@router.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



