from .password_handler import Passwordhandler

def test_encrypt():
    minha_senha = "123RocketENois"
    password_handler = Passwordhandler()

    hashed_password = password_handler.encrypt_password(minha_senha)
    # print(hashed_password)

    password_checked = password_handler.check_password(minha_senha, hashed_password)
    # print(password_checked)

    assert password_checked

# pytest -s -v src/drivers/password_handler_test.py