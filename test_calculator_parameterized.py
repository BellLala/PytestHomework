import pytest

from Calculator import Calculator
from getyaml import get_yaml
case = get_yaml()

class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.parametrize("a, b, c", case)
    def test_add(self, a, b, c):
        s = self.cal.add(a, b)
        assert c == s
