from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from blog.oath2 import get_current_user
from blog import schemas, models, database, oath2
from blog.repository import blog
from typing import List

router = APIRouter(
    prefix='/blog', 
    tags=["Blogs"]
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db:Session=Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session=Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db:Session=Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.destroy(id, db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db:Session=Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.show(id, db)