from msilib.schema import Directory
import pathlib
from urllib.request import Request
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/ "templates"))


@app.get("/", response_class = HTMLResponse)
def home_view(request: Request):
    print(request)
    return templates.TemplateResponse("home.html",{"request":request,"abc":123})


@app.post("/")
def home_detail_view():
    return{"Hello":"World"}