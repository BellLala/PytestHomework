import yaml

def get_yaml():
    with open("./case.yaml", "r", encoding="utf-8") as fp:
        f = fp.read()  # 读出来是字符串
        d = yaml.load(f, Loader=yaml.FullLoader)
    return d

# with open("./case.yaml", "r", encoding="utf-8") as fp:
#     f = fp.read()  # 读出来是字符串
#     d = yaml.load(f, Loader=yaml.FullLoader)
# print(d)
