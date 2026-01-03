from .. import models,schemas,utils,oauth2 
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends ,APIRouter
from ..database import get_db,engine
from .. import oauth2
from typing import Optional
from sqlalchemy import func


router=APIRouter(
    prefix = "/posts",
    tags= ["POSTS"]
)




# ---------------------------------------------------------------
# GET ALL POSTS (ORM METHOD)
# response_model ensures clean API output
# ---------------------------------------------------------------

@router.get("/", response_model=list[schemas.PostOut])
def get_all_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = ""
):
    results = (
        db.query(
            models.Post,
            func.count(models.Vote.post_id).label("votes")
        )
        .join(
            models.Vote,
            models.Vote.post_id == models.Post.id,
            isouter=True
        )
        .filter(models.Post.title.contains(search))
        .group_by(models.Post.id)
        .limit(limit)
        .offset(skip)
        .all()
    )
    return results



# ---------------------------------------------------------------
# CREATE A POST
# NOTE: We use schemas.PostCreate to validate request body
# NOTE: Always return the new post object
# ---------------------------------------------------------------
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user :int = Depends(oauth2.get_current_user),
    user_id:  int  = Depends(oauth2.get_current_user)
):
    
    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# ---------------------------------------------------------------
# GET A POST BY ID
# If post not found → raise 404 error
# ---------------------------------------------------------------
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    post = (
        db.query(
            models.Post,
            func.count(models.Vote.post_id).label("votes")
        )
        .join(
            models.Vote,
            models.Vote.post_id == models.Post.id,
            isouter=True
        )
        .filter(models.Post.id == id)
        .group_by(models.Post.id)
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"id -> {id} was not found"
        )

    return post


# ---------------------------------------------------------------
# DELETE A POST
# If post not found → 404
# Use 204 NO CONTENT when delete succeeds
# ---------------------------------------------------------------
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),
    user_id:  int  = Depends(oauth2.get_current_user),
    current_user :int = Depends(oauth2.get_current_user),
    
    ):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"id -> {id} was not found"
        )
     
    if post.owner_id != current_user.id and current_user.id != 1: #this is done such that the user with the id 1 will act as admin
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN ,
            detail="not authorized to perform delete"
        )

    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)






# ---------------------------------------------------------------
# UPDATE A POST (PUT = full update)
# Using PostUpdate allows partial or full update
# exclude_unset=True means only provided fields are updated
# ---------------------------------------------------------------

@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostUpdate, db: Session = Depends(get_db), user_id:  int  = Depends(oauth2.get_current_user),
                current_user :int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"id -> {id} was not found"
        )
    
    if post.owner_id != current_user.id and current_user.id!=1:#here too the user with id 1 will act as admin
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN ,
            detail="not authorized to perform update"
        )

    post_query.update(updated_post.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return post_query.first()

