import pytest


def setup_function():
    print ("setup_function():每个方法之前执行")


def teardown_function():
    print ("teardown_function():每个方法之后执行")


def test_01():
    print ("正在执行test1")
    x = "this"
    assert 'h' in x


def test_02():
    print ("正在执行test2")
    x = "hello"
    assert hasattr(x,"hello")


def add(a,b):
    return a+b


def test_add():
    print ("正在执行test_add()")
    assert add(3,4) == 7


