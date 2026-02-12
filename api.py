

from fastapi import FastAPI, Depends, APIRouter, Query, Path, Request, Header, HTTPException, status
from sqlalchemy.orm import Session

import time
from typing import Optional
from typing_extensions import Annotated

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")


#from fastapi import APIRouter
from task import task_router
from myupload import upload_router

from database.database import Base, engine, get_database_session
from database.task import crud

from database.models import Task, Category


app = FastAPI()
router = APIRouter()

Base.metadata.create_all(bind=engine)



# Middlewares
@app.middleware('http')
async def add_process_time_to_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time 
    response.headers['X-Process_Time'] = str(process_time)
    print(process_time)
    return response

# Middlewares


# @app.get('/test')
@router.get('/hello')
def hello_world(db: Session = Depends(get_database_session)):
    return { "Hola": "mundo 22"}

@app.get('/e_page')
def page(page: int = Query(1, ge=1, le=20, title='Pagina...'), size: int = Query(5, ge=5, le=20)):
    return {'page': page}

@app.get('/e_phone')
def phone(phone: str = Query(regex=r"^(\+52)?\d{10}$", example="+52 1234-5678")):
    return {'phone': phone}

@app.get('/ep_phone/{phone}')
def phone(phone: str = Path(regex=r"^(\+52)?\d{10}$")):
    return {'phone': phone}


# templates
@app.get('/page')
def index(request: Request, db: Session = Depends(get_database_session)):
    categories = db.query(Category).all()
    return templates.TemplateResponse('task/index.html',{"request": request, 'tasks': crud.getAll(db), 'categories': categories})


# Depends
def pagination(page: Optional[int] = 1, limit: Optional[int] = 10):
    return{'page': page-1, 'limit': limit}

@app.get('/p-task')
def index(pag:dict=Depends(pagination)):
    # print(pag.get('limit'))
    return pag
# -------------------------------------------------------------------

#Path

def validate_token(token: str = Header()): 
    if token != 'TOKEN':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.get('/route-protected', dependencies=[Depends(validate_token)])
def protected_route(index:int):
    return {'hello': 'FastAPI'}

# -------------------------------------------------------------------

# Var
CurrentTaskId = Annotated[int, Depends(validate_token)]

@app.get('/route-protected2')
def protected_route2(CurrentTaskId, index:int):
    return {'hello': 'FastAPI'}

@app.get('/route-protected3')
def protected_route3(CurrentTaskId, index:int):
    return {'hello': 'FastAPI'}

@app.get('/route-protected4')
def protected_route4(CurrentTaskId, index:int, user_id:int):
    return {'hello': 'FastAPI'}

# Depends


# -------------------------------------------------------------------

app.include_router(router)
app.include_router(task_router, prefix='/task')

app.include_router(upload_router, prefix='/upload')


