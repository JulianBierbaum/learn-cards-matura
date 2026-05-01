from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from app.models.card import Card
from app.schemas.card import CardCreate, CardUpdate
from backend.app.exceptions.card import CardDatabaseException, MissingCardException


def create_card(*, db: Session, card: CardCreate, user_id: int):
    db_card = Card(
        name=card.name,
        front=card.front,
        back=card.back,
        tags=card.tags,
        user_id=user_id,
    )

    try:
        db.add(db_card)
        db.commit()
        db.refresh(db_card)
        return db_card
    except IntegrityError as e:
        db.rollback()
        raise CardDatabaseException(err=str(e))


def get_card(*, db: Session, card_id: int, user_id: int) -> Card | None:
    return db.query(Card).filter(Card.id == card_id, Card.user_id == user_id).first()


def get_cards(*, db: Session, user_id: int) -> List[Card]:
    return db.query(Card).filter(Card.user_id == user_id).all()


def get_cards_by_name(*, db: Session, name: str, user_id: int) -> List[Card]:
    return db.query(Card).filter(Card.name == name, Card.user_id == user_id).all()


def update_card(*, db: Session, card_id: int, user_id: int, card: CardUpdate) -> Card:
    db_card = get_card(db=db, card_id=card_id, user_id=user_id)

    if not db_card:
        raise MissingCardException(card_id=card_id)

    try:
        if card.name is not None:
            db_card.name = card.name
        if card.front is not None:
            db_card.front = card.front
        if card.back is not None:
            db_card.back = card.back
        if card.tags is not None:
            db_card.tags = card.tags

        db.commit()
        db.refresh(db_card)
        return db_card
    except IntegrityError as e:
        db.rollback()
        raise CardDatabaseException(err=str(e))


def delete_card(*, db: Session, card_id: int, user_id: int) -> Card:
    db_card = get_card(db=db, card_id=card_id, user_id=user_id)

    if not db_card:
        raise MissingCardException(card_id=card_id)

    try:
        db.delete(db_card)
        db.commit()
        return db_card
    except IntegrityError as e:
        db.rollback()
        raise CardDatabaseException(err=str(e))
