from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

text01 = {
    "actions": "Выбери действие",
    "management": f"Ректор: Далиев",
    "recall": "Оставь отзыв",
    "well_done": "Отлично!",
    "direction": "Выберите направление",
    "recall_send": "Ваш отзыв отправлен"
}

btn1 = {
    "btn1": KeyboardButton(text="Информация о руководстве"),
    "btn2": KeyboardButton(text="Расписание"),
    "btn3": KeyboardButton(text="Оставить отзыв"),
    "btn4": KeyboardButton(text="Информация о руководстве"),

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
    "answer": "Расписание",
    "answer2": "Информация о руководстве",
    "answer3": "Оставить отзыв",

}