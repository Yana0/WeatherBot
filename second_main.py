import config
import telebot
import requests
from bs4 import BeautifulSoup as BS
import datetime
import json


bot = telebot.TeleBot(config.token)
url = 'https://sinoptik.ua/погода-долгопрудный/'
current_day = datetime.datetime.today()
msg_start = "Погода на: "
msg_res = ""
msg_today = ""
for i in range(7):
    msg_res += msg_start + str(current_day.date()) + '\n'
    request = requests.get(url + str(current_day.date()))
    html = BS(request.content, 'html.parser')
    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text
        mem_text = el.select('.oDescription .description')[0].text

    msg_res += t_min + ', ' + t_max + '\n' + text + '\n\n'  # + mem_text + '\n\n'
    if len(msg_today) == 0:
        msg_today = msg_res + mem_text
    current_day += datetime.timedelta(days=1)


@bot.message_handler(commands=['weather1'])
def send(message):
    bot.send_message(message.chat.id, msg_today)


@bot.message_handler(commands=['weather7'])
def send(message):
    bot.send_message(message.chat.id, msg_res)


if __name__ == '__main__':
    bot.polling(none_stop=True)
