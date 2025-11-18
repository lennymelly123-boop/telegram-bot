import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = "8583596428:AAFjuLaGTNB5mtWG0M0CFoqEYBXoPnsglqk"   # <-- встав свій токен бота!!!
ADMIN_ID = 7649095248         # <-- твій адмін ID (все ок)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Напишіть повідомлення, і я передам його адміну псих лікарні м.Івано-Франківськ!.")


@dp.message()
async def forward_all(message: Message):
    await message.forward(chat_id=ADMIN_ID)
    await message.answer("Очікуйте…")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

