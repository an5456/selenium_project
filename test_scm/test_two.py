import pytest
import logging
logging.basicConfig(level=logging.DEBUG)
@pytest.fixture(scope='module')
def test_001():
    logging.info("test_001")