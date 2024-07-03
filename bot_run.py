import logging
import asyncio
import json
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hlink, hbold
from bot_config import TOKEN
from discount_parser import get_page_count, get_data

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
sex_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мужские')], [KeyboardButton(text='Женские')]
    ], 
    resize_keyboard=True,
    )

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуй, {message.from_user.first_name}!\n"
                   "Для кого будем искать кроссовки?",
                   reply_markup=sex_kb)

@dp.message(F.text == 'Мужские')
async def get_man_sneakers(message: Message):
    await message.answer(text="Ищу мужские кроссовки, пожалуйста, ожидай... 🤔\n"
                         "Если скидок много, это может занять до минуты, можешь смело свернуть бот, "
                         "я пришлю уведомление 😉")

    get_data(get_page_count())
    
    with open("result_for_man.json") as file:
        cards = json.load(file)
    
    for item in cards:
        card = f"{hlink(title=item.get('Модель'), url=item.get('Ссылка'))}\n"\
                f"{hbold('Бренд: ')}{(item.get('Бренд'))}\n"\
                f"{hbold("Старая цена: ")}{(item.get('Цена без скидки'))}\n"\
                f"{hbold("Цена по скидке: ")}🔥{item.get('Цена по скидке')}🔥\n"\
                f"{hbold(item.get('Тип'))}\n"\
                f"{hbold('Цвет: ')}{item.get('Цвет')}\n"\
                f"{hbold("Доступные размеры: ")}{item.get("Размеры")}"
        
        await message.answer(card)

@dp.message(F.text == 'Женские')
async def get_woman_sneakers(message: Message):
    await message.answer(text="Ищу женские кроссовки, пожалуйста, ожидай... 🤔\n"
                         "Если скидок много, это может занять до минуты, можешь смело свернуть бот, "
                         "я пришлю уведомление 😉")

    get_data(get_page_count(woman=True))

    with open("result_for_woman.json") as file:
        cards = json.load(file)
    
    for item in cards:
        card = f"{hlink(title=item.get('Модель'), url=item.get('Ссылка'))}\n"\
                f"{hbold('Бренд: ')}{(item.get('Бренд'))}\n"\
                f"{hbold("Старая цена: ")}{(item.get('Цена без скидки'))}\n"\
                f"{hbold("Цена по скидке: ")}🔥{item.get('Цена по скидке')}🔥\n"\
                f"{hbold(item.get('Тип'))}\n"\
                f"{hbold('Цвет: ')}{item.get('Цвет')}\n"\
                f"{hbold("Доступные размеры: ")}{item.get("Размеры")}"
        
        await message.answer(card)

async def run_bot():
    await dp.start_polling(bot)

try:
    logging.basicConfig(level=logging.INFO)
    if __name__ == "__main__":
        asyncio.run(run_bot())
except KeyboardInterrupt:
    print("Bot execution stopped.")
