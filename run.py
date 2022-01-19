import pytest
import allure
import os

if __name__ =="__main__":
    # pytest.main(["-s", "test_calculator.py"])
    # pytest.main(['-m P0'])
    os.system("pytest --alluredir ./report/allure_raw")
    os.system("allure serve report/allure_raw")