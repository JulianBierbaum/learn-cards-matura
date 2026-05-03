import app.crud.user as crud
import app.exceptions.user as user_exc
from app.schemas.user import UserUpdate
import pytest


def test_get_ok(db, test_client):
    result = crud.get_user(db=db, user_id=test_client.id)

    assert result is not None
    assert result.id == test_client.id

def test_update_user_duplicate(db, test_client, test_admin):
    user = UserUpdate(
        name=test_admin.name,
        email=test_client.email,
        is_admin=test_client.is_admin,
        password="Kennwort1"
    )

    with pytest.raises(user_exc.DuplicateUserException):
        crud.update_user(db=db, user=user, user_id=test_client.id)
