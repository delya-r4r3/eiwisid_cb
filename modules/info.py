from aiogram import types
import aiogram.utils.markdown as fmt
from main import dp


@dp.message_handler(commands='info')
async def inform(message: types.Message):
    await message.reply(
        fmt.text(
            fmt.text("Чат бот для упрощения работы с группами"),
            fmt.text(fmt.hbold("Powered by eiwisid")),
            fmt.text(fmt.hitalic('est.2021')),
            sep='\n'
        ), parse_mode='HTML'
    )
