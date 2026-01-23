

from fastapi import APIRouter, Body, status, HTTPException

from models import Task

task_router = APIRouter()

task_list = []


@task_router.get('/',status_code=status.HTTP_200_OK)
def get():
    return {'tasks': task_list}

@task_router.post('/', status_code=status.HTTP_201_CREATED)
# def add(task: str = Body()):
def add(task: Task):

    # Verifica que la task no se repita
    if task in task_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#        raise HTTPException(status_code=404,
                            detail='Task '+ task.name + ' already exist')


    task_list.append(task)
#    task_list.append({
#        'task': task,
#        'status': StatusType.PENDING,
#    })
    return {'tasks': task_list}

@task_router.put('/',status_code=status.HTTP_200_OK)
# def update(index: int, task: str = Body(), status: StatusType = Body()):
# def update(index: int, task: Task):
def update(index: int, task: Task = Body(
    openapi_examples={
        "example1": {
            "summary": '1 example',
            "value": {
                "id": 123,
                "name": "Salvar al mundo",
                "description": "Hola mundo",
                "tag": ["tag1", "tag2"]
            }
        },
        "example2": {
            "summary": '2 example',
            "value": {
                "id": 1234,
                "name": "Salvar al mundo 2",
                "description": "Hola mundo 2",
                "tag": ["tag1", "tag2", "tag3"]
            }
        }
    }

#    examples= [
#         {
#            "id": 1234,
#            "name": "salvar el mundo 2",
#            "description": "hola mundo 2",
#            "tag": ["Tag1", "Tag2", "Tag3"]
#        }
#    ]


)):

#    task_list[index] = {
#        'task' : task.name
#        'status' : task.status
#        'description' : task.description,
#    }

    # Verifica que el indice exista
    if len(task_list) <= index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#        raise HTTPException(status_code=404,
                            detail='Task ID does not exist')

    task_list[index] = task
    return {'tasks': task_list}

@task_router.delete('/',status_code=status.HTTP_200_OK)
def delete(index: int):

    # Verifica que el indice exista
    if len(task_list) <= index:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        raise HTTPException(status_code=404,
                            detail='Task ID does not exist')

    del task_list[index]
    return {'tasks': task_list}
