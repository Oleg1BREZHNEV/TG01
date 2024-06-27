
import random
import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

#Прописываем хендлер и варианты ответов:
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://img.freepik.com/free-photo/adorable-looking-kitten-with-box_23-2150886284.jpg?size=626&ext=jpg','https://img.freepik.com/premium-photo/a-cute-furry-cats-indoors_862994-171023.jpg?size=626&ext=jpg','https://img.freepik.com/premium-photo/cute-burmese-kitten-curled-up_1308-139607.jpg?size=626&ext=jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')


@dp.message(F. text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\\n/start\\n/help")

if __name__ == "__main__":
    asyncio.run(main())