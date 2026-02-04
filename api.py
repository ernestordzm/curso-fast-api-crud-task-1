

from fastapi import FastAPI, Depends, APIRouter, Query, Path
from sqlalchemy.orm import Session

#from fastapi import APIRouter
from task import task_router
from myupload import upload_router

from database.database import Base, engine, get_database_session
from database.models import Task

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

app.include_router(router)
app.include_router(task_router, prefix='/task')

app.include_router(upload_router, prefix='/upload')
