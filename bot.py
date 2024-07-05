# import logging
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hlink, hbold
from bot_config import TOKEN
from discount_parser import get_page_quantity, get_data
global page_number

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

start_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')]
],
    resize_keyboard=True)

sex_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мужские')], [KeyboardButton(text='Женские')]
    ], 
    resize_keyboard=True,)

continue_man_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да 😎')], [KeyboardButton(text='Нет')]
    ],
    resize_keyboard=True)

continue_woman_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да 🙂')], [KeyboardButton(text='Нет')]
    ],
    resize_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуй, {message.from_user.first_name}!\n"
                   "Для кого будем искать кроссовки?",
                   reply_markup=sex_kb)


@dp.message(F.text == 'Мужские')
async def get_man_sneakers(message: Message):
    global page_number
    await message.answer(text="Ищу мужские кроссовки, пожалуйста, ожидай... 🤔\n")

    page_number = 1
    data = get_data(sex='man')

    for item in data:
        card = f"{hlink(title=item.get('model'), url=item.get('url'))}\n"\
                f"{hbold('Бренд: ')}{(item.get('brand'))}\n"\
                f"{hbold('Старая цена: ')}{(item.get('old_price'))}\n"\
                f"🔥{hbold('Цена по скидке: ')}{item.get('new_price')}🔥\n"\
                f"{hbold(item.get('type'))}\n"\
                f"{hbold('Цвет: ')}{item.get('color')}\n"\
                f"{hbold('Доступные размеры: ')}{item.get('sizes')}"
        
        await message.answer(card)

    await message.answer(text=f'Вот, что я нашел по вкусным ценам!\n'\
                                'Показать больше?', reply_markup=continue_man_kb)
    page_number += 1


@dp.message(F.text == 'Женские')
async def get_woman_sneakers(message: Message):
    global page_number
    await message.answer(text="Ищу женские кроссовки, пожалуйста, ожидай... 🤔\n")

    page_number = 1
    data = get_data(sex='woman')

    for item in data:
        card = f"{hlink(title=item.get('model'), url=item.get('url'))}\n"\
                f"{hbold('Бренд: ')}{(item.get('brand'))}\n"\
                f"{hbold('Старая цена: ')}{(item.get('old_price'))}\n"\
                f"🔥{hbold('Цена по скидке: ')}{item.get('new_price')}🔥\n"\
                f"{hbold(item.get('type'))}\n"\
                f"{hbold('Цвет: ')}{item.get('color')}\n"\
                f"{hbold('Доступные размеры: ')}{item.get('sizes')}"
        
        await message.answer(card)
    
    await message.answer(text=f'Вот, что я нашел по вкусным ценам!\n'\
                                'Показать больше?', reply_markup=continue_woman_kb)
    page_number += 1
    

@dp.message(F.text == 'Да 😎')
async def get_more_man(message: Message):
    global page_number
    await message.answer(text="Продолжаю искать...")
    
    last_page = get_page_quantity()

    if page_number <= last_page:
        data = get_data(page=page_number)

        for item in data:
            card = f"{hlink(title=item.get('model'), url=item.get('url'))}\n"\
                    f"{hbold('Бренд: ')}{(item.get('brand'))}\n"\
                    f"{hbold('Старая цена: ')}{(item.get('old_price'))}\n"\
                    f"🔥{hbold('Цена по скидке: ')}{item.get('new_price')}🔥\n"\
                    f"{hbold(item.get('type'))}\n"\
                    f"{hbold('Цвет: ')}{item.get('color')}\n"\
                    f"{hbold('Доступные размеры: ')}{item.get('sizes')}"
            
            await message.answer(card)
        
        await message.answer(text=f'Вот, что я нашел по вкусным ценам!\n'\
                                'Показать больше?', reply_markup=continue_man_kb)
    if page_number > last_page:
        await message.answer(text="Это все предложения на сегодня! Надеюсь я помог!", reply_markup=start_kb)

    page_number += 1


@dp.message(F.text == 'Да 🙂')
async def get_more_woman(message: Message):
    global page_number
    await message.answer(text="Продолжаю искать...")
    
    last_page = get_page_quantity(woman=True)

    if page_number <= last_page:
        data = get_data(page=page_number, sex='woman')

        for item in data:
            card = f"{hlink(title=item.get('model'), url=item.get('url'))}\n"\
                    f"{hbold('Бренд: ')}{(item.get('brand'))}\n"\
                    f"{hbold('Старая цена: ')}{(item.get('old_price'))}\n"\
                    f"🔥{hbold('Цена по скидке: ')}{item.get('new_price')}🔥\n"\
                    f"{hbold(item.get('type'))}\n"\
                    f"{hbold('Цвет: ')}{item.get('color')}\n"\
                    f"{hbold('Доступные размеры: ')}{item.get('sizes')}"
            
            await message.answer(card)
        
        await message.answer(text=f'Вот, что я нашел по вкусным ценам\n'\
                                    'Показать больше?', reply_markup=continue_woman_kb)
    if page_number > last_page:
        await message.answer(text="Это все предложения на сегодня! Спасибо за использование!", reply_markup=start_kb)
    
    page_number += 1


@dp.message(F.text == 'Нет')
async def stop_searching(message: Message):
    await message.answer(text="Надеюсь я помог!\n", reply_markup=start_kb)


async def run_bot():
    await dp.start_polling(bot)

try:
    # logging.basicConfig(level=logging.INFO)
    if __name__ == "__main__":
        asyncio.run(run_bot())
except KeyboardInterrupt:
    print("Bot execution stopped.")
except Exception as e:
    print(e)
