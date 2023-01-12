from pytest import fixture

from auth.models import User
from db.testing_database import TestingSessionLocal

from .data import test_users


@fixture(scope='package')
def create_users():
    db = TestingSessionLocal()

    db.add_all(test_users)
    db.commit()

    yield

    db.query(User).filter(User.username.in_(
                        [user.username for user in test_users])
                        ).delete(synchronize_session='fetch')
    db.commit()
    