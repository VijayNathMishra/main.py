from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.routers.courses import router as courses_router

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(courses_router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/html")
def html_page(request: Request):
    return templates.TemplateResponse("html.html", {"request": request})


@app.get("/css")
def css_page(request: Request):
    return templates.TemplateResponse("css.html", {"request": request})


@app.get("/python")
def python_page(request: Request):
    return templates.TemplateResponse("python.html", {"request": request})

