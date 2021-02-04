import json


def get_codelist(env):
    """
    读取指定json文件，返回代码列表
    :param env: porduct test others
    :return: list
    """
    fileurl = './file/code_list.json'
    with open(fileurl, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        code_list = list(json_data[env].keys())
    return code_list
