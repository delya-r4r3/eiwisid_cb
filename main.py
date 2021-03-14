from loguru import logger
# imported some useful modules
from init import bot, dp
from aiogram import executor, Dispatcher
from modules import help, info, start
# set up local pycharm bot token variable

# configure logging
logger.info('Init finished! Starting polling...')

# initializing whole bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
