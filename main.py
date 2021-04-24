import config
import telebot
import get_weather


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['weather1'])
def send(message):
    text = get_weather.get_weather(1)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['weather7'])
def send(message):
    text = get_weather.get_weather(7)
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
