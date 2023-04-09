import requests
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
from datetime import datetime
from xlsxwriter.workbook import Workbook


def get_bilibili_rankings(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_bilibili_rankings(html):
    soup = BeautifulSoup(html, 'html.parser')
    video_list = soup.find_all('li', class_='rank-item')

    data = []
    for idx, video in enumerate(video_list, start=1):
        info_div = video.find('div', class_='info')
        title = info_div.a.get('title')
        if not title:
            title = info_div.a.text.strip()
        link = "https:" + info_div.a['href']
        data.append((idx, title, link))
    return data


def save_to_excel(data):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_path = os.path.join(desktop_path, f"哔哩哔哩排行榜数据-{now}.xlsx")

    with Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', '抓取时间', bold)
        worksheet.write('B1', '序号', bold)
        worksheet.write('C1', '标题', bold)
        worksheet.write('D1', '链接', bold)

        for idx, row in enumerate(data, start=1):
            worksheet.write_datetime(idx, 0, datetime.now())
            worksheet.write_number(idx, 1, row[0])
            worksheet.write_string(idx, 2, row[1])
            worksheet.write_url(idx, 3, row[2])

        worksheet.hide_gridlines(2)

        # 设置所有单元格的字体为微软雅黑
        cell_format = workbook.add_format({'font_name': 'Microsoft YaHei'})
        worksheet.set_column('A:D', None, cell_format)

    print(f"数据已保存到桌面的 '哔哩哔哩排行榜数据-{now}.xlsx' 文件中。")


def main():
    url = "https://www.bilibili.com/v/popular/rank/all"
    html = get_bilibili_rankings(url)
    if html:
        data = parse_bilibili_rankings(html)
        save_to_excel(data)
    else:
        print("Failed to fetch data from the website.")


if __name__ == '__main__':
    main()
