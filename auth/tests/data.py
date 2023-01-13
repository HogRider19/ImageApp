import datetime

from auth.utils import get_hashed_password
from auth.models import User


test_users = [
    User(
        username='Tom',
        email='tom@gmail.com',
        hashed_password=get_hashed_password('tom1234'),
        registed_at=datetime.datetime.utcnow(),
        is_superuser=False),
    User(
        username='Harry',
        email='harry@gmail.com',
        hashed_password=get_hashed_password('harry1234'),
        registed_at=datetime.datetime.utcnow(),
        is_superuser=True),
]

test_user_template = {
        "username": "testuser",
        "email": "testuser@gamil.com",
        "registed_at": "2023-01-13T14:37:15.479Z",
        "is_active": True,
        "is_superuser": False,
        "role_id": 0,
        "password": "supersecret",
        "password_repeat": "supersecret"}