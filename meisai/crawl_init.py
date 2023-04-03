#Copyright 2023(dtw)
import multiprocessing
import os

import pandas
import requests
import csv
import openpyxl
import concurrent.futures as cf
import re
import urllib.parse
import urllib.request
import os
from bs4 import BeautifulSoup
import collections
import random

def user_agent():
    """
    随机返回一个User-Agent 避免被识别为爬虫
    """
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    ]
    return random.choice(ua_list)
def getHeader():
    """
    返回一个基本的header，User-Agent会随机生成
    """
    return {'User-Agent': user_agent(),
            'Accept': '*/*',
            "referer": "https://www.baidu.com.com/",
    }
def genHeader():
    """
    随机生成一个request使用的header
    """

    headers = {
        "referer": "https://www.baidu.com.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    return headers
index=['Beam','S.A.(reported)','Draft(max)','Displacement','S.A./Disp.','KSP','Fuel','Mast Height from DWL','Water','Rigging Type','Make','Type']
single=collections.defaultdict(dict)
catamarans=collections.defaultdict(dict)

#并行函数
def parallel_do(func, args_list, max_workers=None, mode='thread'):
    max_workers = 4 if not max_workers else max_workers
    exe = cf.ThreadPoolExecutor(max_workers=4) if mode == 'thread' else cf.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())
    with exe as executor:
        executor.map(func, args_list)
        executor.shutdown(wait=True)

#爬取单个url
def parallel_crawler_single(can):
    i_index, boat_name=can[0],can[1]
    boat_name='-'.join(boat_name.split())
    url2='https://sailboatdata.com/sailboat/'+boat_name.lower()
    print(url2)
    single[i_index]={}
    try:
        res = requests.get(url2, headers=genHeader(), timeout=20)  # 伪装请求头，request.post()
        #print(res.status_code,type(res.status_code))
        if res.status_code//100==4:
            return
        soup = BeautifulSoup(res.content.decode(), 'html.parser')
        for key in index:
            first_p = soup.find('div',text=re.compile(r"\s*{}\s*".format(key)))
            if first_p is None:
                continue
            second_p = first_p.next_sibling.next_sibling
            single[i_index][key]=second_p.contents[0].strip()
            #print(second_p.contents[0].strip())

    except Exception as ex:
        print(ex)
    else:
        print("Done!")
    #print(url2,head_info[url2])

#爬取单个url
def parallel_crawler_Catamarans(can):
    i_index, boat_name=can[0],can[1]
    boat_name='-'.join(boat_name.split())
    url2='https://sailboatdata.com/sailboat/'+boat_name.lower()
    catamarans[i_index]={}
    print(url2)
    try:
        res = requests.get(url2, headers=genHeader(), timeout=20)  # 伪装请求头，request.post()
        #print(res.status_code,type(res.status_code))
        if res.status_code//100==4:
            return
        soup = BeautifulSoup(res.content.decode(), 'html.parser')
        for key in index:
            first_p = soup.find('div',text=re.compile(r"\s*{}\s*".format(key)))
            if first_p is None:
                continue
            second_p = first_p.next_sibling.next_sibling
            catamarans[i_index][key]=second_p.contents[0].strip()
            #print(second_p.contents[0].strip())

    except Exception as ex:
        print(ex)
    else:
        print("Done!")
    #print(url2,head_info[url2])

if __name__ == "__main__":
    Catamarans_data = list()
    Single_data = list()
    for root, dirs, files in os.walk(r"./train"):  # 获取train中所有文件
        for file in files:
            path = os.path.join(root, file)
            wb = openpyxl.load_workbook(path)  # 读取文件路径

            # 打开指定的工作簿中的指定工作表：
            Catamarans = wb["Catamarans"]
            # ws = wb.active  # 打开激活的工作表
            ws = list(Catamarans.values)  # 转为列表
            # 2.遍历进行读取数据
            for i_index,r in enumerate(ws):
                Catamarans_data.append([i_index,r[0] + ' ' + str(r[1])])

            # 打开指定的工作簿中的指定工作表：
            Single = wb["Monohulled Sailboats "]
            # ws = wb.active  # 打开激活的工作表
            ws = list(Single.values)  # 转为列表
            # 2.遍历进行读取数据
            for i_index,r in enumerate(ws):
                Single_data.append([i_index,r[0] + ' ' + str(r[1])])
    # Single_data = sorted(Single_data)
    # Catamarans_data = sorted(Catamarans_data)
    print(Single_data)
    print(Catamarans_data)

    try:
        parallel_do(parallel_crawler_single,Single_data)
    except Exception as ex:
        print(ex)
    else:
        print("main_single_Done!")

    try:
        parallel_do(parallel_crawler_Catamarans,Catamarans_data)
    except Exception as ex:
        print(ex)
    else:
        print("main_catamarans_Done!")

    single=sorted(single.items(),key=lambda a:a[0])
    catamarans=sorted(catamarans.items(),key=lambda a:a[0])

    df = pandas.DataFrame(single).T
    df.to_csv("finish_single_init.csv")
    df = pandas.DataFrame(catamarans).T
    df.to_csv("finish_Catamarans_init.csv")