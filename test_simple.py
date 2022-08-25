import pytest
import time


@pytest.fixture()
def browser():
    """
    Фикстура возвращает браузер
    """
    time.sleep(1.5)


# @pytest.mark.skip(reason="Этот тест еще не завершен TASK-123")
def test_first(browser):
    time.sleep(1)


@pytest.mark.xfail(reason="Причина", raises=(AssertionError, ZeroDivisionError))
def test_second():
    time.sleep(2)


def test_third():
    import random
    a = random.randint(0, 10)
    assert a > 5
    time.sleep(3)
