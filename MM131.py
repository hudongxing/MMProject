__author__ = "VioLet"
import os
import requests
from bs4 import BeautifulSoup

Base_path = "/Users/violet/Downloads/mypresent/113/"
start_url = "http://www.mm131.com"


# 解析"http://www.mm131.com"网页,返回频道地址(["http://www.mm131.com/xinggan/","http://www.mm131.com/qingchun/"])
# 返回类型: List
def get_mm113_changes():
    changes = []
    web_data = requests.get(start_url)
    web_data.encoding = "gb18030"
    soup = BeautifulSoup(web_data.text, 'lxml')
    changes_list = soup.select("body > div.nav > ul > li > a")
    for item in changes_list[1:]:
        print(item)
        item_url = item.get("href")
        item_name = item.string
        item_type = item.string
        item_dict = {"item_url": item_url, "item_name": item_name, "item_type": item_type}
        changes.append(item_dict)
    print(changes)
    return changes


# 传入频道地址字典{'item_url': 'http://www.mm131.com/xinggan/', 'item_name': '性感美女'},解析频道页面返回[]
# 返回类型:
def analysis_mm131_change(changes):
    for change in changes:
        change_url = change.get("item_url")
        change_name = change.get("item_name")
        type_path = Base_path + change_name + "/"

        change_respone = requests.get(change_url)
        change_respone.encoding = "gb18030"
        soup = BeautifulSoup(change_respone.text, 'lxml')
        item_list = soup.select("body > div.main > dl.list-left > dd > a")
        print(item_list)
        break


def url_par(type):
    if type == "性感美女":
        return "list_6_"
    elif type == "清纯美眉":
        return "list_1_"
    elif type == "美女校花":
        return "list_2_"
    elif type == "性感车模":
        return "list_3_"
    elif type == "旗袍美女":
        return "list_4_"
    else:
        return "list_5_"


def test():
    change_respone = requests.get('http://www.mm131.com/xinggan/')
    change_respone.encoding = "gb18030"
    soup = BeautifulSoup(change_respone.text, 'lxml')
    item_list = soup.select("body > div.main > dl.list-left > dd > a")
    print(item_list)
    for item in item_list:
        # if item.get("target") is not None:
        #     # path = type_path + item.get_text() + "/"
        down_url = item.get("href")
        print(down_url)


if __name__ == "__main__":
    get_mm113_changes()

    # test()
