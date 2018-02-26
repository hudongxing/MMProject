__author__ = "VioLet"
import os
import requests
from bs4 import BeautifulSoup

Base_path ="/Users/violet/Downloads/mypresent/113/"
start_url = "http://www.mm131.com"


def get_mm113_changes():
    changes = []
    web_data = requests.get(start_url)
    web_data.encoding = "gb18030"
    soup = BeautifulSoup(web_data.text, 'lxml')
    changes_list = soup.select("body > div.nav > ul > li > a")
    for item in changes_list[1:]:
        item_url = item.get("href")
        item_name = item.string
        item_dict = {"item_url": item_url, "item_name": item_name}
        changes.append(item_dict)
    return changes

def get_mm113_change(changes):

    for change in changes:
        print("+++++++++++++")
        item_url = change.get("item_url")
        item_name = change.get("item_name")
        type_path = Base_path + item_name + "/"
        item_type = None
        for i in range(1, 20):
            if i <= 1:
                web_respone = requests.get(item_url)
                web_respone.encoding = "gb18030"
            else:
                more_url = item_url + "list_6_" + str(i)
                web_respone = requests.get(more_url)
                web_respone.encoding = "gb18030"
            print("===========")
            soup = BeautifulSoup(web_respone.text, 'lxml')
            item_list = soup.select("body > div.main > dl.list-left > dd > a")
            for item in item_list:
                if item.get("target") is not None:
                    path = type_path + item.get_text() + "/"
                    down_url = item.get("href")
                    isExists = os.path.exists(path)
                    if not isExists:
                        print(path)
                        os.makedirs(path)
                    else:
                        print("[+]名为" + path + '的文件夹已经存在')
                    for mm in range(1, 20):
                        down_mm113(down_url, mm, path)

def down_mm113(url, page, path):
    Picreferer = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': 'http://img1.mm131.me'
    }
    if page <= 1:
        mm_url = url
    else:
        tt = url.split(".")
        ss = tt[-2] + "_" + str(page)
        tt[-2] = ss
        mm_url = "".join(tt)
    req = requests.get(mm_url)
    req.encoding = "gb18030"
    soup = BeautifulSoup(req.text, 'lxml')
    pic = soup.select("body > div.content > div.content-pic > a > img")
    print(mm_url)
    print(type(pic))
    down_url = pic[0].get("src")

    try:
        html = requests.get(down_url, headers=Picreferer)
        fileName = path + '{}.jpg'.format(page)
        fph = open(fileName, "wb")
        fph.write(html.content)
        fph.flush()
        fph.close()
    except Exception as e:
        print('[!]Address Error!!!!!!!!!!!!!!!!!!!!!')


def test():
    url = "http://www.mm131.com/xinggan/"
    web_respone = requests.get(url)
    web_respone.encoding = "gb18030"
    soup = BeautifulSoup(web_respone.text, 'lxml')
    item_list = soup.select("body > div.main > dl.list-left > dd > a")
    for item in item_list:
        if item.get("target") is not None:
            print(item.get("href"))


def down_mm113_222():
    Picreferer = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': 'http://img1.mm131.me'
    }
    url = "http://www.mm131.com/xinggan/3501.html"
    pic = "http://img1.mm131.me/pic/3501/1.jpg"
    path = "/Users/violet/Downloads/mypresent/11/"

    req = requests.get("http://www.mm131.com/xinggan/3501.html")
    req.encoding = "gb18030"
    soup = BeautifulSoup(req.text, 'lxml')
    pic = soup.select("body > div.content > div.content-pic > a > img")
    down_url = pic[0].get("src")
    try:
        html = requests.get(pic, headers=Picreferer)
        fileName = path + 'dd.jpg'
        fph = open(fileName, "wb")
        fph.write(html.content)
        fph.flush()
        fph.close()
    except Exception as e:
        print('[!]Address Error!!!!!!!!!!!!!!!!!!!!!')


if __name__ == "__main__":

    changes = get_mm113_changes()
    get_mm113_change(changes)
    # # # test()
    # down_mm113()
