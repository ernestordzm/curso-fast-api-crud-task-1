

from fastapi import APIRouter, Depends, Body, Path, status # HTTPException
from sqlalchemy.orm import Session

from database.database import get_database_session

# from database import models
from database.task import crud
# from database import models

from schemes import Task, TaskRead, TaskWrite # StatusType
from dataexample import TaskWithORM

task_router = APIRouter()

# task_list = []


@task_router.get('/',status_code=status.HTTP_200_OK)
# def get(db: Session = Depends(get_database_session)):
def get(db: Session = Depends(get_database_session)):
    # return {"tasks": crud.getAll(db) }
    return {"task": [TaskRead.model_validate(task) for task in crud.getAll(db) ]}
    # return {"task": [Task.model_validate(task) for task in crud.getAll(db) ]}

@task_router.get('/{id}',status_code=status.HTTP_200_OK)
def get(id: int = Path(ge = 1), db: Session = Depends(get_database_session)):
    return crud.getById(id, db)
    # return Task.model_validate(crud.getById(id, db))

#    print(crud.getById(db = db, id = 1).name)
#    print(crud.getById(db = db, id = 1).name)
    # print(crud.getAll(db = db)[1].name)

# ----------------------------------------
#     task = crud.getById(db = db, id=1)

#     print(task.category.name)
#     print(task.user.website)
# ----------------------------------------

    # Relacion inversa, categoria 1, 2 tareas
    # print(db.query(models.Category).get(1).tasks[2])

    # Relacion inversa, usuario 1, 2 tareas
    # print(db.query(models.User).get(1).tasks[2])

    # crud.create(Task(name='Task 22', description='Desc 22', status=StatusType.DONE, category_id=1, user_id=1),db=db)
    # crud.update(1, Task(name='Test2222', description='Desc2222', status=StatusType.DONE, category_id=2, user_id=1), db=db)

    # print(crud.pagination(1,2, db))

#    task = db.query(models.Task).filter(models.Task.id == 1).first()
#    task = db.query(models.Task).get(models.Task.id == 1).first()
#    print(task.name)

    # return {'tasks': task_list}
    # return {'tasks':  crud.getAll(db)}

@task_router.post('/', status_code=status.HTTP_201_CREATED)
# def add(task: str = Body()):
def add(task: Task = Body(
    openapi_examples=TaskWithORM
), db: Session = Depends(get_database_session)):

# ----------------------------------------------
    # Verifica que la task no se repita
    # if task in task_list:
        # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#--        raise HTTPException(status_code=404,
                            # detail='Task '+ task.name + ' already exist')
# ----------------------------------------------

    # crud.create(Task(name='Test1', description='Desc1', status=StatusType.DONE),db=db)
    # crud.create(task, db=db)

    # task_list.append(task)
    
#    task_list.append({
#        'task': task,
#        'status': StatusType.PENDING,
#    })
    return {'tasks': crud.create(task, db=db)}



@task_router.post('/form-create', status_code=status.HTTP_201_CREATED)
# def add(task: str = Body()):
def addForm(task: Task = Depends(Task.as_form), db: Session = Depends(get_database_session)) -> dict:

    # return {'tasks': crud.create(task, db=db)}
    return {'tasks': Task.from_orm(crud.create(task, db=db)) }



@task_router.put('/{id}',status_code=status.HTTP_200_OK)
# def update(index: int, task: str = Body(), status: StatusType = Body()):
# def update(index: int, task: Task):
def update(id: int = Path(ge=1), task: TaskWrite = Body(
    openapi_examples = TaskWithORM

#    examples= [
#         {
#            "id": 1234,
#            "name": "salvar el mundo 2",
#            "description": "hola mundo 2",
#            "tag": ["Tag1", "Tag2", "Tag3"]
#        }
#    ]


), db: Session = Depends(get_database_session)):

#    task_list[index] = {
#        'task' : task.name
#        'status' : task.status
#        'description' : task.description,
#    }


# --------------------------------------------------------
#     # Verifica que el indice exista
#     if len(task_list) <= index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #        raise HTTPException(status_code=404,
#                             detail='Task ID does not exist')

# --------------------------------------------------------

#    print(index)
#    crud.update(index, Task(name='Test2', description='Desc2', status=StatusType.DONE), db=db)


    # task_list[index] = task

    # return {'tasks': task_list}

    # crud.update(id, task, db)

    return{"tasks": crud.update(id, task, db)}

@task_router.delete('/{id}',status_code=status.HTTP_200_OK)
def delete(id: int = Path(ge=1), db: Session = Depends(get_database_session)):

    crud.delete(id, db)

# #--------------------------------------------
#     # Verifica que el indice exista
#     if len(task_list) <= index:
# #        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         raise HTTPException(status_code=404,
#                             detail='Task ID does not exist')

#     del task_list[index]
# #--------------------------------------------

    # return {'tasks': task_list}
    # return {"tasks": crud.getAll(db)}
    return {'msj' : 'Ok'}


#------------------------------------- TAG

@task_router.put('/tag/add/{id}',status_code=status.HTTP_200_OK)
def tagAdd(id: int = Path(ge = 1), idTag:int = Body(ge=1) , db: Session = Depends(get_database_session)):
    return crud.tagAdd(id, idTag, db)

@task_router.delete('/tag/remove/{id}',status_code=status.HTTP_200_OK)
def tagRemove(id: int = Path(ge = 1), idTag:int = Body(ge=1) , db: Session = Depends(get_database_session)):
    print(idTag)
    return crud.tagRemove(id, idTag, db)
