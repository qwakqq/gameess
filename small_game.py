from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import randint
from pydantic import BaseModel

class UpdateCoordsPlayer(BaseModel):
    x: int
    y: int
    name_player: str


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

@app.post('/move_player')
def move_player(move_data: UpdateCoordsPlayer):
    name = move_data.name_player
    if not playrs_data.get(name):
        raise HTTPException(status_code=404, detail='такого игрока нет')
    playrs_data[name]['coords'] = [move_data.x, move_data.y]
    return {'status': 'ok'}