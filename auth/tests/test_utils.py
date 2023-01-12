import pytest
from pydantic import BaseModel

from auth.utils import (get_hashed_password, get_user_by_username,
                        verify_password)
from db.testing_database import TestingSessionLocal

from .fixtures import create_users, test_users


@pytest.mark.parametrize('password', [
                                    '54321',
                                    'aowsjvop2332',
                                    'lweIUCN832l'])
def test_hashed_password(password: str):
    fake_passwords = ['hwqecoh', 'wpirev', 'iqwcj23']
    hashed_password = get_hashed_password(password)
    for fake in fake_passwords:
        assert verify_password(fake, hashed_password) == False
    assert verify_password(password, hashed_password) == True

@pytest.mark.parametrize('username, user_results', [ 
                                (user.username, {
                                    'username': user.username, 
                                    'hashed_password': user.hashed_password,
                                    'email': user.email,
                                    'registed_at': user.registed_at,
                                    'is_superuser': user.is_superuser,
                                }) for user in test_users])
def test_get_user_by_username(create_users, username: str,  user_results: dict):
    db_session = TestingSessionLocal()
    user = get_user_by_username(username, db_session)
    assert isinstance(user, BaseModel)
    for field_name, field_value in user_results.items():
        assert getattr(user, field_name) == field_value


def test_get_user_by_username_not_exist(create_users):
    db_session = TestingSessionLocal()
    user = get_user_by_username('iuwahvikjahfvawhruibv', db_session)
    assert user is None
