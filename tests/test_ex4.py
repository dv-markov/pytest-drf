import pytest
from django.contrib.auth.models import User


# Доступ к БД через фикстуру и тестовую функцию
@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")


@pytest.mark.django_db
def test_set_check_password1(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True


# Доступ к БД только через фикстуру, без дополнительного декоратора с маркером
@pytest.fixture()
def user_2(db):
    user = User.objects.create_user("test-user")
    return user


def test_set_check_password2(user_2):
    assert user_2.username == "test-user"


# Подключение к БД на все время сессии
@pytest.fixture(scope="session")
def user_3(db):
    user = User.objects.create_user("test-user")
    print('create-user')
    return user


def test_set_check_password3(user_3):
    print('check-user-1')
    assert user_3.username == "test-user"


def test_set_check_password4(user_3):
    print('check-user-4')
    assert user_3.username == "test-user"

