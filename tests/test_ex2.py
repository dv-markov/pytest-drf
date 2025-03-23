import pytest


@pytest.fixture
def yield_fixture():
    print('Start test phase')
    yield 6
    print('End test phase')


def test_ex_1(yield_fixture):
    print('run-example-1')
    assert yield_fixture == 6
