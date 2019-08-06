from collections import namedtuple
import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, True)

#
# def test_defaults():
#     t1 = Task()
#     t2 = Task(None, None, False, True)
#     assert t1 == t2


@pytest.mark.run_group1
def test_aa():
    assert 1 == 1


@pytest.mark.run_group1
def test_bb():
    assert 2 == 5


@pytest.mark.run_group2
def test_cc():
    assert 4 == 4
