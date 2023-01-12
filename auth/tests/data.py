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