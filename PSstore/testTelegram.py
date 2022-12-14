import telebot

bot = telebot.TeleBot('5573811919:AAFM0EG5FREx2Sf5j8qf_Whb9g963ixKzAE')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}  im bot, whenever I"ll kill you after you choise gameboy')

@bot.message_handler(commands=['1','2','3','4',])
def PS(message):
    print(message.text)
    bot.send_message(message.chat.id, 'Оставь свой номер телефона')


@bot.message_handler()
def get_message(message):
    print(message.text)
    if message.text == "suck":
        bot.send_message(message.chat.id, 'suck свой')
    if str(message.text).replace("+","").isdigit():
        bot.send_message(message.chat.id, 'напиши имя')


bot.polling(none_stop=True)