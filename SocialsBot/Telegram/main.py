from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


class Telegram:
    def __init__(self) -> None:
        load_dotenv()
        self.token = os.getenv("TOKEN")
        self.give_up_chat_id = -1002424553540

    def sendMessage(self, msg):
        async def act():
            message = msg
            async with Bot(
                token=self.token,
                default=DefaultBotProperties(
                    parse_mode=ParseMode.HTML,
                ),
            ) as bot:
                await bot.send_message(chat_id=self.give_up_chat_id, text=message)
                print("Message sent!")
        
        asyncio.run(act())
        
