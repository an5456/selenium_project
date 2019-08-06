import allure
import pytest


@allure.feature('出口业务')
@allure.story('创建出库单')
@pytest.mark.run_bb
def test_case_01():
    """
    出口流程可以正常创建
    """
    assert 0


@allure.feature('入库业务')
@allure.story('创建入库单')
@pytest.mark.repeat(7)
@pytest.mark.run_aa
def test_case_02():
    """
    入库流程可以正常创建
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
