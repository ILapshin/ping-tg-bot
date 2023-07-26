import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.builtin import Text

from service import Service
from config import *
from strings import *
from keyboards import get_keyboard
from users import read_users, write_user


logging.basicConfig(level=logging.INFO)


service = Service(url_list=URL_LIST)


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


users = read_users(USERS_FILE_PATH)

def add_user(user_id: int):
    users.append(user_id)
    write_user(USERS_FILE_PATH, user_id)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    markup = get_keyboard()
    user_id = str(message.from_user.id)

    msg = USER_ALREADY_ADDED

    if user_id not in users:
        add_user(user_id)
        msg = USER_ADDED.format(user_id=user_id)
        
    await bot.send_message(user_id, msg, reply_markup=markup)


@dp.message_handler(Text(equals=CHECK_NOW))
async def process_check_now(message: types.Message):
    response = service.ping_all()  
    msg = ALL_HOSTS_UP  
    if response:
        msg = get_not_responding_msg(response)        
    await bot.send_message(message.from_user.id, msg)


def get_not_responding_msg(response):
    return FOLLOWING_HOSTS_DOWN + '\n'.join(response)


async def broadcast():
    response = service.ping_all()

    if not response:
        return

    msg = get_not_responding_msg(response)

    for user_id in users:        
        await bot.send_message(user_id, msg)


async def run_service():
    while True:
        time_offset_seconds = TIME_OFFSET * 60
        await asyncio.sleep(time_offset_seconds, result=(await broadcast()))     


if __name__ == '__main__':
    asyncio.Task(run_service())
    executor.start_polling(dp, skip_updates=True)