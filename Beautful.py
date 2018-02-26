__author__ = "VioLet"
import os
import requests
from bs4 import BeautifulSoup
import urllib.request

start_url = "http://www.mzitu.com/"
Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}
URL="http://i.meizitu.net/2017/12/06b01.jpg"

def get_mm_changel():
    web_data = requests.get(start_url, headers=Hostreferer)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup)
    channel = soup.select('body > div.header > div.mainnav > ul.menu > li > a')
    channels = channel[1:]
    print(channel)
    return channels
    # for list in channels:
    #     print(list.get('href'))


def get_page_from(channel, pages):
    channel = channel + '/page/{}'.format(pages)
    print(channel)
    web_data = requests.get(channel)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find('body > div.main > div.main-content > div.currentpath'):
        pass
    else:
        lists = soup.select('#pins > li > span > a')
        print(lists)
        for lists in lists:
            path = '/Users/violet/Downloads/mypresent/{}/'.format(lists.get_text())
            isExists = os.path.exists(path)
            if not isExists:
                print(path)
                os.mkdir(path)
            else:
               pass
            # for i in range(1, 101):
            #     get_list_info(lists.get('href'), i, path)


def get_list_info(url, page, mmpath):
    mm_url = None
    if page <= 1 :
        mm_url = url
    else:
        mm_url = url + "/" + str(page)
    web_data = requests.get(mm_url,headers = Hostreferer)
    soup = BeautifulSoup(web_data.text, 'lxml')
    src = soup.select('body > div.main > div.content > div.main-image > p > a > img')
    print(src)
    m_url = src[0].get("src")
    try:
        html = requests.get(m_url, headers= Picreferer)
        fileName = mmpath + '{}.jpg'.format(page)
        fph = open(fileName, "wb")
        fph.write(html.content)
        fph.flush()
        fph.close()
    except Exception as e:
        print('[!]Address Error!!!!!!!!!!!!!!!!!!!!!')


def run():
    get_mm = get_mm_changel()
    for item in get_mm:
        for i in range(10):
            get_page_from(item.get("href"), i)


if __name__ == "__main__":
    # get_mm_changel()
    run()