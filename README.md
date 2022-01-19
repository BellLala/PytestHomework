# PytestHomework
pytest + allure自动化生成测试报告

## 安装说明
### 1. 安装pytest
- 可通过命令安装：pip3 install pytest
- 或者通过pycharm 搜索安装

### 2. 安装allure
- 通过命令安装：brew install allure
- 使用allure 还需要安装 allure-pytest 
  - 可通过命令安装：pip3 install allure-pytest
  - 或者通过pycharm搜索安装

## 使用说明
- 文件 Calculator.py 是被测试代码
- 文件 pytest.ini 是自定义的标签
- 文件 test_calculator.py 是测试用例
- 文件 run.py 执行该文件可以自动运行test_calculator.py 并自动打开生成的测试报告