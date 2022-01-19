import allure
import pytest

from Calculator import Calculator

class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.P0
    def test_add_001(self):
        b = self.cal.add(1, 1)
        assert b == 2

    @pytest.mark.P0
    def test_add_002(self):
        b = self.cal.add(-0.01, 0.02)
        assert b == 0.01

    @pytest.mark.P0
    def test_add_003(self):
        b = self.cal.add(10, 0.02)
        assert b == 10.02

    @pytest.mark.P1
    def test_add_004(self):
        b = self.cal.add(98.99, 99)
        assert b == 197.99

    @pytest.mark.P1
    def test_add_005(self):
        b = self.cal.add(99, 98.99)
        assert b == 197.99

    @pytest.mark.P1
    def test_add_006(self):
        b = self.cal.add(-98.99, -99)
        assert b == -197.99

    @pytest.mark.P1
    def test_add_007(self):
        b = self.cal.add(-99, -98.99)
        assert b == -197.99

    @pytest.mark.P1
    def test_add_008(self):
        b = self.cal.add(99.01, 0)
        assert b == "展示提示信息"

    @pytest.mark.P1
    def test_add_009(self):
        b = self.cal.add(-99.01, -1)
        assert b == "展示提示信息"

    @pytest.mark.P1
    def test_add_010(self):
        b = self.cal.add(2, 99.01)
        assert b == "展示提示信息"

    @pytest.mark.P1
    def test_add_011(self):
        b = self.cal.add(1, -99.01)
        assert b == "展示提示信息"

    @pytest.mark.P1
    def test_add_012(self):
        with pytest.raises(TypeError) as e:
            self.cal.add("文", 9.3)
        assert e.value == "展示提示信息"

    @pytest.mark.P1
    def test_add_013(self):
        with pytest.raises(TypeError) as e:
            self.cal.add(4, "字")
        assert e.value == "展示提示信息"

    @pytest.mark.P1
    def test_add_014(self):
        with pytest.raises(TypeError) as e:
            self.cal.add("nu", 0.2)
        assert e.value == "展示提示信息"

    @pytest.mark.P1
    def test_add_015(self):
        with pytest.raises(TypeError) as e:
            self.cal.add(30, "t")
        assert e.value == "展示提示信息"

    @pytest.mark.P1
    def test_add_016(self):
        with pytest.raises(TypeError) as e:
            self.cal.add("*&", 0.2)
        assert e.value == "展示提示信息"

    @pytest.mark.P1
    def test_add_017(self):
        with pytest.raises(TypeError) as e:
            self.cal.add(21.45, "@")
        assert e.value == "展示提示信息"

    @pytest.mark.P2
    def test_add_018(self):
        with pytest.raises(TypeError) as e:
            self.cal.add("", 20.93)
        assert e.value == "展示提示信息"

    @pytest.mark.P2
    def test_add_019(self):
        with pytest.raises(TypeError) as e:
            self.cal.add(-3, "")
        assert e.value == "展示提示信息"
