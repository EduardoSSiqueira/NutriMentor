from re import template
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.RootRouter import router as rootRouter
app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"),name="static")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(rootRouter)


if __name__=="__main__":
    uvicorn.run(app="main:app", reload=True)


    