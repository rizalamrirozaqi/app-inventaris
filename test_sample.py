import logging

logger = logging.getLogger(__name__)

def test_addition():
    logger.info("Running test: 1 + 1")
    assert 1 + 1 == 2

def test_subtraction():
    logger.info("Running test: 3 - 1")
    assert 3 - 1 == 2

def test_failure():
    logger.warning("This test is expected to fail")
    assert 2 == 3