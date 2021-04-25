import config
import telebot
import get_weather


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['weather1'])
def send(message):
    """Return today's weather"""
    text = get_weather.get_weather(1)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['weather7'])
def send(message):
    """Return weather for a week"""
    text = get_weather.get_weather(7)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['start', 'help'])
def send(message):
    """Start message"""
    start_msg = "Хочешь узнать погоду в прекрсаном городе Долгопрудный?\n " \
                "команда \\weather1 - вернет погоду на сегодня, " \
                "вместе с народным прогнозом \n" \
                "команды \\weather7 - вернет погоду на неделю."
    bot.send_message(message.chat.id, start_msg)


if __name__ == '__main__':
    bot.polling(none_stop=True)
