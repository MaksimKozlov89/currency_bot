import telebot
import bcusdbr

TOKEN = '1892581132:AAEYKR9BLf5WpMK1ZkbuvpHReeC7PCABif4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text =='Привет':
        bot.send_message(message.from_user.id,
                         'Привет, чем я могу помочь?')
    elif message.text =='/help':
        bot.send_message(message.from_user.id, 'Для того, чтобы узнать самые выгодные курсы '
                                               'покупки или продажи USD - напиши: "best currency"')
    elif message.text.lower() == 'best currency':
        messages = bcusdbr.parse()
        for ms in messages:
            bot.send_message(message.from_user.id, ms)
    else:
        bot.send_message(message.from_user.id, 'Незнакомая команда! Напиши /help')


bot.polling(none_stop=True, interval=0)
