from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.crud import user as crud
from app.schemas.user import User, UserCreate, UserUpdate
from app.api.deps import SessionDep, get_current_active_admin
import app.exceptions.user as user_exc


router = APIRouter(prefix="/user")


@router.get("/{user_id}", response_model=User)
def get_user(session: SessionDep, user_id: int):
    user = crud.get_user(db=session, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="no user with this id"
        )
    return user


@router.get("/email/{email}", response_model=User)
def get_user_by_email(session: SessionDep, email: str):
    user = crud.get_user_by_email(db=session, email=email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_200_HTTP_204_NO_CONTENT,
            detail="no user with this email",
        )
    return user


@router.get("/", response_model=List[User])
def get_users(session: SessionDep):
    return crud.get_users(db=session)


@router.post(
    "/",
    response_model=User,
    dependencies=[Depends(get_current_active_admin)],
    status_code=status.HTTP_201_CREATED,
)
def create_user(session: SessionDep, user: UserCreate):
    if user.is_admin:
        return crud.create_admin(db=session, user=user)
    else:
        return crud.create_user(db=session, user=user)


@router.put(
    "/{user_id}", response_model=User, dependencies=[Depends(get_current_active_admin)]
)
def update_user(session: SessionDep, user_id: int, user: UserUpdate):
    try:
        return crud.update_user(db=session, user_id=user_id, user=user)
    except user_exc.UserException as e:
        if isinstance(e, user_exc.MissingUserException):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
