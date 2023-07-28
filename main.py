import telebot
import re
import datetime

bot = telebot.TeleBot('6088414708:AAGoiwUpesiVJij-v9ibpUVIGEBNvV_6oK0')


@bot.message_handler(content_types=['text'])
def check_trigger_words(message):
    # Список триггерных слов
    trigger_words = ['знакомый', 'знакомые', 'знакомых', 'друзья', 'знакомого', 'знакомыми', 'знакомая', 'знакомому',
                     'знакомым', 'друга', 'друзей', 'друг', 'знакомой', 'знакомую']

    # Используем регулярное выражение для поиска триггерных слов в тексте
    pattern = r'\b(?:' + '|'.join(trigger_words) + r')\b'

    # Поиск совпадений в тексте
    matches = re.findall(pattern, message.text, re.IGNORECASE)

    # Отправляем сообщение, если нашли соответствие
    if matches and message.from_user.username == 'yuventus89':

        # Читаем содержимое файла, получаем дату прошлого сообщения
        date_file = open('date.txt', mode='r')
        date = date_file.read()
        date_file.close()
        last_message_date = datetime.datetime.fromtimestamp(int(date))

        # Высчитываем разницу времени
        delta_time = last_message_date - datetime.datetime.now()
        delta_time = int(delta_time.total_seconds()) * -1

        # Перезаписываем дату нового сообщения
        date_file = open('date.txt', mode='w')
        date_file.write(str(message.date))
        date_file.close()

        # Обработка дней, часов, минут, секунд
        if delta_time >= 86400:
            word_value = 'Дней'
            delta_time_value = (((delta_time // 60) // 60) // 24)
            bot.reply_to(message, f'{word_value} без историй со знакомыми от Сани: {delta_time_value} → 0')

        elif 86400 > delta_time >= 3600:
            word_value = 'Часов'
            delta_time_value = (delta_time // 60) // 60
            bot.reply_to(message, f'{word_value} без историй со знакомыми от Сани: {delta_time_value} → 0')

        elif 3600 > delta_time >= 60:
            word_value = 'Минут'
            delta_time_value = (delta_time // 60)
            bot.reply_to(message, f'{word_value} без историй со знакомыми от Сани: {delta_time_value} → 0')

        elif delta_time < 60:
            word_value = 'Секунд'
            delta_time_value = delta_time
            bot.reply_to(message, f'{word_value} без историй со знакомыми от Сани: {delta_time_value} → 0')

# Бесконечная работа бота
bot.infinity_polling()

