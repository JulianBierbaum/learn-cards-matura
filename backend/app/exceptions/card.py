class CardException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CardDatabaseException(CardException):
    def __init__(self, err: str) -> None:
        super().__init__(f"Database Integrity error: {err}")


class MissingCardException(CardException):
    def __init__(self, card_id: int) -> None:
        super().__init__(f"Card with ID {card_id} not found in DB")
