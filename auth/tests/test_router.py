import pytest
from fastapi import status

from auth.utils import get_user_by_username
from db.testing_database import TestingSessionLocal, client

from .data import test_user_template
from .fixtures import clean_users_db


def check_user_exist(username):
    db_session = TestingSessionLocal()
    user = get_user_by_username(username, db_session)
    return not user is None

def test_success_create_user(clean_users_db):
    
    assert check_user_exist(test_user_template['username']) == False

    response = client.post(url='/auth/createuser', json=test_user_template)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get('username') == test_user_template['username']
    assert not response.json() in ['password', 'hashed_password']

    assert check_user_exist(test_user_template['username']) == True

@pytest.mark.parametrize('replace_field', [
                                        (('username', 't')),
                                        (('username', 't'*500)),
                                        (('password', '1234')),])
def test_fail_create_user(clean_users_db, replace_field):
    
    failed_test_user_template = test_user_template.copy()
    failed_test_user_template[replace_field[0]] = replace_field[1]
    response = client.post(url='/auth/createuser', json=failed_test_user_template)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert check_user_exist(failed_test_user_template['username']) == False



