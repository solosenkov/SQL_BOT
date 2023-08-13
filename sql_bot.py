import telebot
import sqlite3


TOKEN = 'сюда вставить токен'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для работы с SQL. Отправьте мне SQL-запрос, и я верну вам результат.')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = message.text
        c.execute(query)
        data = c.fetchmany(10)
        response = ''
        for row in data:
            response += str(row) + '\n'
        bot.send_message(message.chat.id, response)
        conn.close()
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')

bot.polling()
