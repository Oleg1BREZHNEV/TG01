import random
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
from config import WEATHER_API_KEY
# Ваш API ключ OpenWeatherMap
#WEATHER_API_KEY = '80adf0f917ab00389839d772b2d4f1e2'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

# Функция для получения погоды
async def get_weather(city: str):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(WEATHER_API_URL, params=params) as resp:
            print(WEATHER_API_URL)

            if resp.status == 200:
                data = await resp.json()
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                return f"Температура: {temperature}°C\nОписание: {description}"
            else:
                return "Не удалось получить данные о погоде."



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
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/weather")

    # Новый хендлер для получения погоды
@dp.message(Command('weather'))
async def weather(message: Message):
    weather_info = await get_weather('Москва')
    await message.answer(weather_info)


if __name__ == "__main__":
    asyncio.run(main())