#telegram_bot

import pyowm
import telebot

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = pyowm.OWM('4ecd09d1d2a7375673797f77c4b84899', config_dict)
mgr = owm.weather_manager()


bot = telebot.TeleBot('1636422665:AAFBrkQpE-jvMR4Mcz6DsVnY3tfVQS7zlfw')

@bot.message_handler(content_types=['text'])
def send_echo(message):
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
	#bot.reply_to(message, message.text)


        temp = w.temperature('celsius')["temp"]

        answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
        answer += 'Температура сейчас в районе ' + str(temp) + '\n\n'

        if temp < -10:
            answer += 'Одевайтесь как мамонт'
        elif temp < 0:
            answer += 'Одевайтесь тепло'
        elif temp < 10:
            answer += 'Одевайтесь по теплее'
        elif temp < 20:
            answer += 'Не забудьте одеть свитер'
        elif temp > 20:
            answer += 'Советую выйти на улицу налегке'
        
        bot.send_message(message.chat.id, answer)

        
	
bot.polling( none_stop = True)

