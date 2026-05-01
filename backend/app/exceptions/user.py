class UserException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UserDatabaseException(UserException):
    def __init__(self, err: str) -> None:
        super().__init__(f"Database Integrity error: {err}")


class MissingUserException(UserException):
    def __init__(self, user_id: int) -> None:
        super().__init__(f"User with ID {user_id} not found in DB")


class DuplicateUserException(UserException):
    def __init__(self, name: str | None, email: str | None) -> None:
        super().__init__(
            f"User with name '{name}' or email '{email}' already exists in DB"
        )
