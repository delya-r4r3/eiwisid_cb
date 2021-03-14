from aiogram import types
import aiogram.utils.markdown as fmt
from main import dp


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
