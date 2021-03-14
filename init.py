from aiogram import Bot, Dispatcher
from loguru import logger
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

logger.info('Welcome to PilotTelegramBot!\nStarting init...')
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
logger.info('aiogram init                   [ OK ]')
