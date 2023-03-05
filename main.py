import telebot

from config import TOKEN, GROUP_ID
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

bot = telebot.TeleBot(TOKEN)

text = {
    'welcome': "Привет студент Мэи,\n"
               "Салом, Меи талабаси"
}

btn = {
    "btn_uz": KeyboardButton(text="Uz"),
    "btn_ru": KeyboardButton(text="Русс")
}

inline_btn = dict({})  # инлайн кнопки
actions = dict({})  # ответы бота


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(btn['btn_uz'], btn['btn_ru'])

    bot.send_message(message.chat.id, text['welcome'], reply_markup=kb)


@bot.message_handler(content_types=['text'])
def main_func(message):

    if message.text == "Uz" or message.text == "Русс":
        language_down(message)


@bot.callback_query_handler(func=lambda call: True)
def direction(call):
    req = int(call.data.split('_')[0])
    if req == 1:
        print('asdasd')


def language_down(message):  # выбор языка
    global text01, btn1, actions1, inline_btn1
    if message.text == "Uz":
        from text_uz import text01, btn1, actions1,  inline_btn1
    elif message.text == "Русс":
        from text_ru import text01, btn1, actions1, inline_btn1
    text.update(text01)
    btn.update(btn1)
    actions.update(actions1)
    inline_btn.update(inline_btn1)

    kb = ReplyKeyboardMarkup(resize_keyboard=True)  # отправка запросов
    kb.add(btn['btn1'], btn['btn2'], btn['btn3'])
    user_choice = bot.send_message(message.chat.id, text['actions'], reply_markup=kb)
    bot.register_next_step_handler(user_choice, func)


def func(message):
    if message.text == actions['answer']:  # отправка расписания
        kb = InlineKeyboardMarkup(row_width=1)
        for x, i in inline_btn.items():
            kb.add(i)
        bot.send_message(message.chat.id, text['well_done'], reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, text['direction'], reply_markup=kb)

    elif message.text == actions['answer2']:  # отправка руководства МЭИ
        bot.send_message(message.chat.id, text['management'])

        btn_1 = ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1.add(btn['btn1'], btn['btn2'], btn['btn3'])
        user_choice = bot.send_message(message.chat.id, text['actions'], reply_markup=btn_1)  # отправка запросов
        bot.register_next_step_handler(user_choice, func)

    elif message.text == actions['answer3']:  # отправка заявки
        recall = bot.send_message(message.chat.id, text['recall'], reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(recall, recall_func)


def recall_func(message):  # принятие заявки и отправка в группу
    bot.send_message(GROUP_ID, message.text)
    bot.send_message(message.chat.id, text['recall_send'])

    btn_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1.add(btn['btn1'], btn['btn2'], btn['btn3'])
    user_choice = bot.send_message(message.chat.id, text['actions'], reply_markup=btn_1)  # отправка запросов
    bot.register_next_step_handler(user_choice, func)


bot.polling()
