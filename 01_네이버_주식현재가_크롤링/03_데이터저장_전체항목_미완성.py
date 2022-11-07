import requests
from bs4 import BeautifulSoup
import openpyxl
import os

fpath = r'K:\My files\PA개인폴더(stand.lee)\88. AWS Toy Project\Crawling\data_standlee2.xlsx'


wb = openpyxl.load_workbook(fpath)
ws = wb.active  # 현재 활성화된 시트 선택

# 종목코드리스트
codes = [
    '005930', #삼성전자
    '000660', #하이닉스
    '035720'  #카카오
]


row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text  # id 값은 앞에 # 붙여줌
    price = price.replace(',', '')  # , 제거
    print(price)
    ws[f'B{row}'] = int(price)
    row = row + 1

wb.save(fpath)