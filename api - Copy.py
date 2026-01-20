
from fastapi import FastAPI
app = FastAPI()


@app.get('/test')
def hello_world2():
    return { "Hola": "mundo 22"}


@app.get('/detail/{id}/{id2}')
def detail(id: int, id2: str):
    return { "Detail": id}


@app.get('/')
def get():
    return { "get": "get"}

@app.post('/')
def post():
    return { "post": "post"}

@app.put('/')
def put():
    return { "put": "put"}

@app.delete('/')
def delete():
    return { "delete": "delete"}
