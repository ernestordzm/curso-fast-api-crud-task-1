

from fastapi import APIRouter, File, UploadFile
import shutil
from typing import List

upload_router = APIRouter()

@upload_router.post("/file")
def upload_file(file: bytes = File()):
    return{"file_size" : len(file)}

# el Upload es mejor opcion para la carga de archivos.

@upload_router.post("/fileuploadfile")
def upload_uploadfile1(file: UploadFile):
    return{
        "file" : file.file,
        "content_type": file.content_type,
        }

# el Upload es mejor opcion para la carga de archivos.

@upload_router.post("/fileuploadfile2")
def upload_uploadfile2(file: UploadFile):

    with open("img/image.png","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return{
        "file" : file.file
        }

@upload_router.post("/fileuploadfile3")
def upload_uploadfile3(images: List[UploadFile] = File()):

    for image in images:
#        with open("img/image.png","wb") as buffer:
        with open("img/"+image.filename,"wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
