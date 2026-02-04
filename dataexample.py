
from schemes import Task, StatusType

TaskWithOutORM = {
        "example1": {
            "summary": '1 example',
            "value": {
                "id": 12,
                "name": "Salvar al mundo",
                "description": "Hola mundo",
                "status": StatusType.PENDING,
                "tag": ["tag1", "tag2"]
            }
        },
        "example2": {
            "summary": '2 example',
            "value": {
                "id": 1,
                "name": "Salvar al mundo 2",
                "description": "Hola mundo 2",
                "status": StatusType.PENDING,
                "tag": ["tag1", "tag2", "tag3"]
            }
        }
}

TaskWithORM = {
        "example1": {
            "summary": '1 example',
            "value": {
                "id": 12,
                "name": "Salvar al mundo",
                "description": "Hola mundo",
                "status": StatusType.PENDING,
                "tag": ["tag1", "tag2"],
                "category_id": 2,
                "user_id": 1

            }
        },
        "example2": {
            "summary": '2 example',
            "value": {
                "id": 1,
                "name": "Salvar al mundo 2",
                "description": "Hola mundo 2",
                "status": StatusType.PENDING,
                "tag": ["tag1", "tag2", "tag3"],
                "category_id": 1,
                "user_id": 2
            }
        }
}