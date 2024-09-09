import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils import markdown as md
from dotenv import load_dotenv
import os
load_dotenv()

# using this code we can get incoming messages to employ bot or any channel that employ is a member of it.


TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Define handler for /start command
@dp.message(Command("start"))
async def handle_start(message: types.Message):
    chat_id = message.chat.id
    await message.reply(f"Your chat ID is: {chat_id}")

# Define handler for /get_chat_id command
@dp.message(Command("get_chat_id"))
async def get_chat_id(message: types.Message):
    chat_id = message.chat.id
    await message.reply(f"Your chat ID is: {chat_id}")


# Handle messages from channels
@dp.channel_post()
async def channel_post_handler(channel_post: types.Message): 
    print(channel_post)

async def on_startup():
    logging.info("Bot is starting...")

async def on_shutdown():
    logging.info("Bot is stopping...")

if __name__ == '__main__':
    import asyncio

    async def main():
        # Start polling
        await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)

    asyncio.run(main())
