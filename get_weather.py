import requests
from bs4 import BeautifulSoup as BS
import datetime

url = 'https://sinoptik.ua/погода-долгопрудный/'


def degrees_to_int(string):
    """convert Celsius degrees to integer"""
    return [int(i[:-1]) for i in string.split(' ')[1:-1]]


def int_to_degrees(temp):
    """convert integer to Celsius degrees"""
    if temp > 0:
        return '+' + str(temp) + '°'
    if temp < 0:
        return str(temp) + '°'
    return '0°'


def get_weather(days):
    """Return weather for next days: min temperature, max temperature, text description,
    folk weather forecast(for current day)"""
    current_day = datetime.datetime.today()
    msg_start = "Погода на: "
    msg_res = ""
    for i in range(days):
        msg_res += msg_start + str(current_day.date()) + '\n'
        request = requests.get(url + str(current_day.date()))
        html = BS(request.content, 'html.parser')
        t_min = t_max = text = mem_text = ""
        for el in html.select('#content'):
            temperature = degrees_to_int(el.select('.weatherDetails .temperature')[0].text)
            t_min = int_to_degrees(min(temperature))
            t_max = int_to_degrees(max(temperature))
            text = el.select('.wDescription .description')[0].text
            mem_text = el.select('.oDescription .description')[0].text

        msg_res += '+'.join(["мин: ", t_min, ', ', "макс: ", t_max, '\n', text, '\n\n'])
        if days == 1:
            msg_res += mem_text + '\n\n'
        current_day += datetime.timedelta(days=1)
    return msg_res
