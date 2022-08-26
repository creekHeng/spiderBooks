import re
from bs4 import BeautifulSoup
import requests
import json


# 获取书章节信息，以及章节网址
def get_chapters_info(url):
    html = requests.get(url, headers=headers, proxies=proxies)
    html = BeautifulSoup(html.text, 'html.parser')
    # print(html.text)
    # 1.筛选含有整个目录章节的代码
    toc_code = html.select("#list > dl ").__str__()
    # 2. 筛选只含有从头到尾的章节
    pattern = re.compile("正文</dt>(.*?)</dl>", re.S)
    toc = pattern.findall(toc_code).__str__()

    # 3.从上一步筛选的结果提取 超链接 和 章节标题
    toc_code = BeautifulSoup(toc, 'html.parser')
    toc = toc_code.find_all("a")
    books = {}
    for i in toc:
        href = i['href']
        text = i.string
        books[text] = href

    return books


# 写入文件
def write_text(title, url):
    html = requests.get(url=url, headers=headers, proxies=proxies)
    html = BeautifulSoup(html.text, "html.parser")

    content = html.select("#content>p")

    with open('data.txt', 'a+') as f:
        f.write(title)
        f.write("\n\n")
        print("正在写入 " + title)
        for i in content:
            f.write(i.string)
            f.write("\n")
        f.write("\n")


# 保存json文件
def save_json(books, json_path):

    with open(json_path,"w+") as f:
        try:
            content = json.load(f)

        except json.JSONDecodeError:
            print("文件不存在，正在创建 test.json……")
            print("正在导入数据……")
            with open("./test.json", 'w+') as fw:
                json.dump(books,fw,indent=4, ensure_ascii=False)
                print("写入完成")
            
            content = json.load(f)
            print("导入 {} 条数据".format(len(content)))
    
    cnt = 0
    flag = 0 if len(content)== len(books) else len(content)
    for chapter in books:
        if cnt >= flag:
            print("正在写入 {} ……".format(chapter))
            write_text(chapter,books[chapter])
        cnt += 1


if __name__ == "__main__":
    # headers，代理设置
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    # 代理设置
    proxy = '127.0.0.1:52810'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }

    print("请在下方键入你的网址：")
    # url = input()
    url = "http://www.b520.cc/147_147321/"
    books = get_chapters_info(url)
    cnt = 0
    save_json(books, "test.json")
    # # cnt：计数，用来控制爬取多少章内容
    # for chapter in books:
    #     cnt += 1
    #     get_text(chapter,books[chapter])
    #     if cnt == 30:
    #         break
