from aiogram.types import ReplyKeyboardMarkup

from strings import CHECK_NOW


def get_keyboard():
    command_list = [[CHECK_NOW]]
    markup = ReplyKeyboardMarkup(keyboard=command_list, resize_keyboard=True, one_time_keyboard=False)
    return markup