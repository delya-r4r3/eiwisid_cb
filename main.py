import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from os import getenv
from sys import exit
import aiogram.utils.markdown as fmt

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands='info')
async def inform(message: types.Message):
    await message.reply("Чат бот для упрощения работы с группами\n"
                        "Powered by eiwi\n"
                        "est.2021")


@dp.message_handler(commands='start')
async def greetings(message: types.Message):
    await message.reply(
        fmt.text(
            fmt.text("Привет."),
            fmt.text("Я чат бот, призванный помочь управлять чатом."),
            fmt.text("Введи", fmt.hbold('/help,'), "чтобы получить список команд"),
            sep="\n"
        ), parse_mode="HTML"
    )


@dp.message_handler(commands='help')
async def helps(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold('/start:'), "используется для запуска, выводит приветственное сообщение"),
            fmt.text(fmt.hbold('/help:'), "выводит список команд"),
            fmt.text(fmt.hbold('/info:'), "выводит общую информацию"),
            sep='\n'
        ), parse_mode='HTML'
    )


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
