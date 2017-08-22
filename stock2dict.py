#  -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.google.com/finance/historical?q=MAGN&startdate=Nov+01%2C+2016&enddate=Dec+31%2C+2016'


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('div', id='prices')
    print(total)


def get_html(url):
    r = requests.get(url)
    return r.text


def get_dict(string):
    data = string.find_all('td')
    try:
        Date = data[0].text.strip('\n')
        Open = float(data[1].text.strip('\n'))
        High = float(data[2].text.strip('\n'))
        Low = float(data[3].text.strip('\n'))
        Close = float(data[4].text.strip('\n'))
        Volume = int(data[5].text.strip('\n').replace(',', ''))
    except:
        return
    data = {'Date': Date,
            'Open': Open,
            'High': High,
            'Low': Low,
            'Close': Close,
            'Volume': Volume}
    return data


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        strings = soup.find('div', id='prices').find('table').find_all('tr')
    except:
        return
    del strings[0]
    list_data = []
    for string in strings:
        list_data.append(get_dict(string))
    return list_data


def get_head():
    return {'Date': 'Date',
            'Open': 'Open',
            'High': 'High',
            'Low': 'Low',
            'Close': 'Close',
            'Volume': 'Volume'}


def get_pages_data(html):
    list = []
    start = 0
    while get_page_data:
        tmp_url = url + '&start=' + str(start) + '&num=200'
        page_data = get_page_data(get_html(tmp_url))
        if not page_data:
            return list
        list.extend(page_data)
        start += 200
    return list


def main():
    get_page_data(get_html(url))
    # get_total_pages(get_html(url))
    # print(len(get_pages_data(get_html(url))))
    print(get_pages_data(get_html(url)))


if __name__ == '__main__':
    main()
