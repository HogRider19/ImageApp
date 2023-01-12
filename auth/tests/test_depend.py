import pytest
from auth.dependencies import get_hashed_password, verify_password



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



