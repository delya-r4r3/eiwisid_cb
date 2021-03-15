from aiogram import types
import aiogram.utils.markdown as fmt
from main import dp


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


@dp.message_handler(commands='text')
async def answ(message: types.Message):
    await message.answer(
        fmt.text('Напиши', fmt.hbold('/help')), parse_mode="HTML"
    )
