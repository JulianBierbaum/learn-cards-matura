from typing import List
from fastapi import APIRouter, HTTPException, status

from app.crud import card as crud
from app.schemas.card import Card, CardCreate, CardUpdate
from app.api.deps import SessionDep, CurrentUser
import app.exceptions.card as card_exc


router = APIRouter(prefix="/card")


@router.get("/{card_id}", response_model=Card)
def get_card(session: SessionDep, card_id: int, current_user: CurrentUser):
    card = crud.get_card(db=session, user_id=current_user.id, card_id=card_id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="no card with this id"
        )
    return card


@router.get("/name/{name}", response_model=List[Card])
def get_card_by_name(session: SessionDep, name: str, current_user: CurrentUser):
    cards = crud.get_cards_by_name(db=session, name=name, user_id=current_user.id)
    if not cards:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="no card with this name"
        )
    return cards


@router.get("/", response_model=List[Card])
def get_cards(session: SessionDep, current_user: CurrentUser):
    return crud.get_cards(db=session, user_id=current_user.id)


@router.post("/", response_model=Card, status_code=status.HTTP_201_CREATED)
def create_card(session: SessionDep, card: CardCreate, current_user: CurrentUser):
    try:
        return crud.create_card(db=session, card=card, user_id=current_user.id)
    except card_exc.CardException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{card_id}", response_model=Card)
def update_card(
    session: SessionDep, card_id: int, card: CardUpdate, current_user: CurrentUser
):
    try:
        return crud.update_card(
            db=session, card_id=card_id, card=card, user_id=current_user.id
        )
    except card_exc.CardException as e:
        if isinstance(e, card_exc.MissingCardException):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{card_id}", response_model=Card)
def delete_card(session: SessionDep, card_id: int, current_user: CurrentUser):
    try:
        return crud.delete_card(db=session, card_id=card_id, user_id=current_user.id)
    except card_exc.CardException as e:
        if isinstance(e, card_exc.MissingCardException):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
