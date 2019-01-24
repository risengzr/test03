import allure


class TestAllure:

    @allure.step("我是测试步骤001")
    def test_01(self):
        allure.attach("描述：", "01")
        assert 1

    @allure.step('我是测试步骤002')
    def test_02(self):
        allure.attach("描述：", "02")
        assert 1

