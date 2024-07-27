import os
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor


TOKEN_API = "7349293261:AAEh5V3nTF4psSumorurbSGVJAJghTaG9L0"
SAVE_PATH = "photos/"


logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
 

async def on_startup(_):
    print('bot started')


HELP = """
<b>Добро пожаловать в телеграмм бот по покупке тортов!</b>
<b>Выберите ваши дальнейшие действия</b>"""


kb1 = ReplyKeyboardMarkup(resize_keyboard=True) #desa
b1 = KeyboardButton('/выбрать-торт') 
kb1.add(b1)
# .insert(b2).add(b3)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True) #desa
b2 = KeyboardButton('/Какой-вид-бисквита?')
kb2.add(b2)


kb3 = ReplyKeyboardMarkup(resize_keyboard=True) #desa
b3 = KeyboardButton('/Какой-крем-Вы-хотели-бы?')
kb3.add(b3)


kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
b4 = KeyboardButton('/Выберите-вид-начинки')
kb4.add(b4)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, 
                           text=HELP,
                           parse_mode='HTML',
                           reply_markup=kb1)

    
    
@dp.message_handler(commands=["выбрать-торт"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('16 см ( ~1,2 кг)', callback_data='button1'))
    keyboard.add(InlineKeyboardButton('18 см (~2,5 кг)', callback_data='button2'))
    keyboard.add(InlineKeyboardButton('20 см ( ~3,3 кг)', callback_data='button3'))
    await message.answer('Выберите размер:', 
                         reply_markup=keyboard)
    user_log_file = f"user_{message.from_user.id}_log.log"
    user_logger = logging.getLogger(f"user_{message.from_user.id}")
    user_logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(user_log_file)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    user_logger.addHandler(file_handler)



@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "вы выбрали - 16 см ( ~1,2 кг)", 
                           reply_markup=kb2)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: 16 cm ( ~1,2 kg)")


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "вы выбрали - 18 см (~2,5 кг)",
                           reply_markup=kb2)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: 18 cm (~2,5 kg)")


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали - 20 см ( ~3,3 кг)", 
                           reply_markup=kb2)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: 20 cm ( ~3,3 kg)")
    

@dp.message_handler(commands=["Какой-вид-бисквита?"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Шоколадный', callback_data='button4'))
    keyboard.add(InlineKeyboardButton('Ванильный', callback_data='button5'))
    keyboard.add(InlineKeyboardButton('Медовые коржи', callback_data='button6'))
    keyboard.add(InlineKeyboardButton('Молочная девочка', callback_data='button7'))
    keyboard.add(InlineKeyboardButton('Морковный', callback_data='button8'))
    keyboard.add(InlineKeyboardButton('Красный бархат', callback_data='button9'))
    # keyboard.add(InlineKeyboardButton('Диасик в шоколаде', callback_data='button10'))
    await message.answer('Выберите бисквит:', reply_markup=keyboard)
    

@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "вы выбрали Шоколданый",
                            reply_markup=kb3)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: shokolad")


@dp.callback_query_handler(lambda c: c.data == 'button5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "вы выбрали Ванильный", 
                           reply_markup=kb3)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Vanilniy")



@dp.callback_query_handler(lambda c: c.data == 'button6')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, " Вы выбрали Медовые коржи",
                            reply_markup=kb3)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Medovie korji")


@dp.callback_query_handler(lambda c: c.data == 'button7')
async def process_callback_яbutton1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, " Вы выбрали Молочную девочку", 
                           reply_markup=kb3)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Molochnyu devochky")


@dp.callback_query_handler(lambda c: c.data == 'button8')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, " Вы выбрали Морковный",
                            reply_markup=kb3)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Morkovniy")


@dp.callback_query_handler(lambda c: c.data == 'button9')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, " Вы выбрали Красный бархат", 
                           reply_markup=kb3)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Krasniy barhat")



@dp.message_handler(commands=["Какой-крем-Вы-хотели-бы?"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Классический крем-чиз', callback_data='button10'))
    keyboard.add(InlineKeyboardButton(' Шоколадный крем', callback_data='button11'))
    keyboard.add(InlineKeyboardButton('Заварной крем', callback_data='button12'))
    keyboard.add(InlineKeyboardButton('Крем с кусочками шоколада', callback_data='button13'))
    keyboard.add(InlineKeyboardButton('Мусс на белом шоколаде', callback_data='button14'))
    keyboard.add(InlineKeyboardButton('Мусс на темном шоколаде', callback_data='button15'))
    # keyboard.add(InlineKeyboardButton('Диасик в шоколаде', callback_data='button10'))
    await message.answer('Выберите крем:', reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'button10')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Классический крем-чиз",
                           reply_markup=kb4)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Klassicheskiy krem-chiz")


@dp.callback_query_handler(lambda c: c.data == 'button11')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Шоколадный крем",
                           reply_markup=kb4)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Shokolasniy krem")
    

@dp.callback_query_handler(lambda c: c.data == 'button12')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Заварной крем",
                           reply_markup=kb4)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Zavarnoy krem")
    

@dp.callback_query_handler(lambda c: c.data == 'button13')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Крем с кусочками шоколада",
                           reply_markup=kb4)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Krem c kyco4kami shokolada")


@dp.callback_query_handler(lambda c: c.data == 'button14')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Мусс на белом шоколаде",
                           reply_markup=kb4)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Mycc na belom shokolade")


@dp.callback_query_handler(lambda c: c.data == 'button15')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Мусс на темном шоколаде",
                           reply_markup=kb4)
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Mycc na temnom shokolade")
    


@dp.message_handler(commands=["Выберите-вид-начинки"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Вишня-Шоколад', callback_data='button16'))
    keyboard.add(InlineKeyboardButton('Сникерс', callback_data='button17'))
    keyboard.add(InlineKeyboardButton('Манго-Маракуйа', callback_data='button18'))
    keyboard.add(InlineKeyboardButton('Банан-Шоколад', callback_data='button19'))
    keyboard.add(InlineKeyboardButton('пропустить', callback_data='button20'))
    # keyboard.add(InlineKeyboardButton('Диасик в шоколаде', callback_data='button10'))
    await message.answer('Выберите бисквит:', reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'button16')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Вишня-Шоколад")
    await bot.send_message(callback_query.from_user.id, "отлично, теперь отправьте фото примера вашего торта!")
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Bishnya-Shokolad")
    

@dp.callback_query_handler(lambda c: c.data == 'button17')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Сникерс")
    await bot.send_message(callback_query.from_user.id, "отлично, теперь отправьте фото примера вашего торта!")
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Snikers")


@dp.callback_query_handler(lambda c: c.data == 'button18')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Манго-Маракуйа")
    await bot.send_message(callback_query.from_user.id, "отлично, теперь отправьте фото примера вашего торта!")
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Mango--Marakuya")


@dp.callback_query_handler(lambda c: c.data == 'button19')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы выбрали Банан-Шоколад")
    await bot.send_message(callback_query.from_user.id, "отлично, теперь отправьте фото примера вашего торта!")
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: Banan-shokolad")


@dp.callback_query_handler(lambda c: c.data == 'button20')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы пропустили выбор")
    await bot.send_message(callback_query.from_user.id, "отлично, теперь отправьте фото примера вашего торта!")
    user_id = callback_query.from_user.id
    user_logger = logging.getLogger(f"user_{user_id}")
    user_logger.info("chelovek vibral: propystit'")



if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def save_photo(message: Message):
    file_id = message.photo[-1].file_id
    file_path = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_path.file_path)
    
    file_name = f"{SAVE_PATH}{file_id}.jpg"
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file.read())

    await message.answer("Фото успешно сохранено!")


# Функция для отправки рассылки
async def send_broadcast(message: str):
    users = [6019731272, 963619015, 6586349018]  # ID пользователей, которым будет отправлена рассылка
    for user_id in users:
        await bot.send_message(chat_id=user_id, text=message, parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['broadcast'])
async def broadcast(message: types.Message):
    await send_broadcast("📢 Спи Спи, Диасик...)")


@dp.message_handler(commands=['developer'])
async def developer_xxx(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, 
                           text='https://t.me/endlessonelove')



if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())

    loop.run_forever()
    executor.start_polling(dp, skip_updates=True)