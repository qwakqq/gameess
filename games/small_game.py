from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import randint

app = FastAPI()
templates = Jinja2Templates(directory='templates')


playrs_data = {
    "test_gamer": {
        'coords': [0, 0]
    }
}


@app.get('/get_playrs_data')
def get_playrs_data():
    return playrs_data

@app.get('/', response_class=HTMLResponse)
def index(
    request: Request, 
    name: str):
    playrs_data[name] = {
            'coords': [ randint(0, 500), randint(0, 400) ]
            }
    return templates.TemplateResponse(name='index.html', request=request)
