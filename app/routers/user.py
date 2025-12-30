
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends ,APIRouter
from ..database import get_db,engine

router=APIRouter(
    prefix="/users",
    tags = ["USERS"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut
)

def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    new_user = models.User(
        **user.dict(exclude={"password"}),
        password=utils.hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id -> {id} was not found"
        )

    return user
