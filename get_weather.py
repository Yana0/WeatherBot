import requests
from bs4 import BeautifulSoup as BS
import datetime


def degrees_to_int(string):
    tmp = string.split(' ')
    tmp = tmp[1:-1]
    tmp = [int(i[:-1]) for i in tmp]
    return tmp


def int_to_degrees(temp):
    ans = '+' + str(temp) + '°'
    if temp < 0:
        ans[0] = '-'
    if temp == 0:
        return ans[1:]
    return ans


def get_weather(days):
    url = 'https://sinoptik.ua/погода-долгопрудный/'
    current_day = datetime.datetime.today()
    msg_start = "Погода на: "
    msg_res = ""
    for i in range(days):
        msg_res += msg_start + str(current_day.date()) + '\n'
        request = requests.get(url + str(current_day.date()))
        html = BS(request.content, 'html.parser')
        t_min = t_max = text = mem_text = ""
        for el in html.select('#content'):
            #t_min = [str(i).isdigit() for i in el.select('.weatherDetails .temperature')[0].text]
            temperature = degrees_to_int(el.select('.weatherDetails .temperature')[0].text)
            t_min = int_to_degrees(min(temperature))
            t_max = int_to_degrees(max(temperature))
            text = el.select('.wDescription .description')[0].text
            mem_text = el.select('.oDescription .description')[0].text

        msg_res += "мин: " + t_min + ', ' + "макс: " + t_max + '\n' + text + '\n\n'
        if days == 1:
            msg_res += mem_text + '\n\n'
        current_day += datetime.timedelta(days=1)
    return msg_res
