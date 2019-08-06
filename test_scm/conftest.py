import pytest
import requests


@pytest.fixture(scope='module', params=[
    (1),
    (3),
    (4),
])
def test_1(request):
    print("jjjjjjjjjjjj")
    return request.param
