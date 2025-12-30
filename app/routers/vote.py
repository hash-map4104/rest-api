from .. import models,schemas,utils,oauth2 ,database
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends ,APIRouter
from ..database import get_db,engine
from .. import oauth2
from typing import Optional


router=APIRouter(
    prefix="/vote",
    tags=["VOTES"])



@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: schemas.Vote,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    # 1. Check post exists
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {vote.post_id} does not exist"
        )

    # 2. Check existing vote
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id,
        models.Vote.user_id == current_user.id
    )

    found_vote = vote_query.first()

    # 3. Add vote
    #if dir is 1 then the like will be added and if you use dir=0 then if there is a like then it will be deleted
    
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="You have already voted on this post"
            )

        new_vote = models.Vote(
            post_id=vote.post_id,
            user_id=current_user.id
        )
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}

    # 4. Remove vote
    elif vote.dir == 0:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist"
            )

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully deleted vote"}
