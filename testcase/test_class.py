import pytest


def setup_module():
    print("setup_module:在模块之前运行的方法")


def teardown_module():
    print("teardown_module:在模块之后运行的方法")


class TestClass(object):

    def setup_class(self):
        print("setup_class:每个类之前执行一次")

    def teardown_class(self):
        print("teardown_class:每个类之后运行的方法")

    def setup_method(self):
        print("setup_method:每个方法之前执行一次")

    def teardown_method(self):
        print("teardown_method:每个方法之后执行一次")

    def test_01(self):
        print("test_01")
        assert 1 == 1

    def test_s(self):
        print("test_02")
        assert 5 == 5


class TestA:
    def test_001(self):
        print("TestA:执行方法test_001")
        assert 1==1

