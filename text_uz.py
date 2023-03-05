from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

text01 = {
    "actions": "Салом",
    "management": f"Ректор: Далиев",
    "recall": "Шарҳ қолдиринг",
    "well_done": "Ажойиб!",
    "direction": "Йўналишни танланг",
    "recall_send": "Сизнинг фикрингиз юборилди"
}

btn1 = {
    "btn1": KeyboardButton(text="Қўлланма ҳақида маълумот"),
    "btn2": KeyboardButton(text="Жадвал"),
    "btn3": KeyboardButton(text="Шарҳ қолдиринг"),
    "btn4": KeyboardButton(text="Қўлланма ҳақида маълумот"),

}

inline_btn1 = {
    "btn_inline_1": InlineKeyboardButton(text='ТТ', callback_data=1),
    "btn_inline_2": InlineKeyboardButton(text='ЭЭ', callback_data=2),
    "btn_inline_3": InlineKeyboardButton(text='Нано', callback_data=3),
    "btn_inline_4": InlineKeyboardButton(text='ЭК', callback_data=4),
    "btn_inline_5": InlineKeyboardButton(text='УТС', callback_data=5),
    "btn_inline_6": InlineKeyboardButton(text='УК', callback_data=6),

}

actions1 = {
    "answer": "Жадвал",
    "answer2": "Қўлланма ҳақида маълумот",
    "answer3": "Шарҳ қолдиринг",

}