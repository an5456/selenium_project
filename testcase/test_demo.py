import logging
import pytest


@pytest.mark.run(order=4)
def test_two():
    assert 1 == 1


@pytest.mark.run(order=2)
def test_one():
    assert True == False


@pytest.mark.run(order=3)
def test_three():
    assert 5==5


@pytest.mark.run(order=1)
def test_four():
    assert 3==8

