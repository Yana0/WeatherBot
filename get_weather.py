import requests
from bs4 import BeautifulSoup as BS
import datetime


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
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            text = el.select('.wDescription .description')[0].text
            mem_text = el.select('.oDescription .description')[0].text

        msg_res += t_min + ', ' + t_max + '\n' + text + '\n\n'
        if days == 1:
            msg_res += mem_text + '\n\n'
        current_day += datetime.timedelta(days=1)
    return msg_res
