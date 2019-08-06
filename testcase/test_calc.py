import pytest

# @pytest.mark.parametrize("x,y,z", [
#     (3, 5, 9),
#     (2, 4, 6),
#     (6, 9, 42),
#     (1, 5, 6)
# ])
# def test_add(x, y, z):
#     assert x + y == z


import logging

logging.basicConfig(level=logging.DEBUG)


def setup_module():
    logging.info('module开始')


def teardown_module():
    logging.info('module完成，清理数据')


@pytest.mark.run(order=1)
class TestA:
    def setup_class(self):
        logging.info('TestA')

    def teardown_class(self):
        logging.info('TestA完成环境清理')


    def test_1(self):
        assert 1 == 3

    def test_2(self):
        assert 4 == 4

    def test_3(self):
        assert 7 ==7


@pytest.mark.run(order=2)
class TestB:
    def setup_method(self):
        logging.info('TestB初始化')

    @pytest.mark.parametrize("a,b,c", [
        (1, 2, 3),
        (4, 5, 8),
        (3, 4, 7)
    ])
    def test_4(self, a, b, c):
        logging.info('test_4')
        assert a + b == c

    def test_5(self):
        logging.info('test_5')

    def test_6(self):
        logging.info('test_6')


@pytest.mark.run(order=3)
class TestC:
    @pytest.mark.run(order=6)
    def test_7(self):
        logging.info('test_7')

    @pytest.mark.run(order=4)
    def test_8(self):
        logging.info('test_8')

    @pytest.mark.run(order=5)
    def test_9(self):
        logging.info('test_9')





