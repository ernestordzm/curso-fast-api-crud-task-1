

from fastapi import FastAPI, Depends, APIRouter, Query, Path
from sqlalchemy.orm import Session

from fastapi import Request 
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



app.include_router(router)
app.include_router(task_router, prefix='/task')

app.include_router(upload_router, prefix='/upload')


