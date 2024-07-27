from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, callback_query, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
import random

from configg import TOKEN_API

# TOKEN_API = '7288474971:AAG6bMyUfNmww9jnWJHzDKU_xoh2AA3NeJQ'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('бот запущен✅')


async def send_random(message: types.Message):
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)



all_photo = ["https://pikuco.ru/upload/test_stable/9d7/9d7163f11810f89276e2d3aac68e94ae.webp",
             "https://pibig.info/uploads/posts/2021-05/1619960716_25-pibig_info-p-anime-tyan-na-more-anime-krasivo-30.jpg",
             "https://fotobase.co/files/img/photo/anime-tianki/anime-tianki-27.webp"]

photos = dict(zip(all_photo,['3 девочки на фотке'
                             ,'девочка в купальнике',
                             'девочка на фоне солнышка']))


random_photo = random.choice(list(photos.keys()))

flag = False

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/yo')
b3 = KeyboardButton('random photo')
b4 = KeyboardButton('/locate')

kb.add(b1,b2).add(b3).add(b4)


kbp = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton('рандом')
bp2 = KeyboardButton('главное меню')
kbp.add(bp1,bp2)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤',
                           callback_data='like')
ib2 = InlineKeyboardButton(text='💔',
                           callback_data='dislike')
ib3 = InlineKeyboardButton(text='next pictures',
                           callback_data='next')
ib4 = InlineKeyboardButton(text='главное меню',
                           callback_data='main')
ikb.add(ib1,ib2).add(ib3).add(ib4)


@dp.message_handler(Text(equals='random photo'))
async def open_fp(message: types.Message):
    await message.answer(text='Рандомная фотка!😍',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()



# @dp.message_handler(Text(equals='рандом'))
# async def send_random_photo(message: types.Message):
#     await  send_random(message)    



@dp.message_handler(Text(equals='главное меню'))
async def open_fp(message: types.Message):
    await message.answer(text='вы попали в главное меню',
                         reply_markup=kb)



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id,
                         text='добро пожаловать в телеграмм бота!💫',
                         reply_markup=kb)
    

@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id,
                         text='<b>тут тебе никто не поможет😇</b>',
                         parse_mode='html')
    

@dp.message_handler(commands=['yo'])
async def start_command(message: types.Message):
    await message.answer('как тебе стик?')
    await bot.send_sticker(message.chat.id,
                         sticker='CAACAgIAAxkBAAEMgrxmmTSnHqMVa4kao5dcI0NGR_BxNAACOR4AAkMSmErsHoy4qOmE4DUE')



@dp.message_handler(commands=['locate'])
async def loc_pok(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(28,100),
                            longitude=random.randint(28,100))



@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('вам понравилась фотка!')
            flag = not flag
        else:    
            await callback.answer('вы уже лайкнули фото!😴')
    elif callback.data == 'dislike':
        await callback.answer('вам  не понравилась фотка!')
    elif callback.data == 'main':
        await callback.message.answer(text='главное меню!',
                              reply_markup=kb)
        await callback.message.delete()
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=photos[random_photo]),
                                                           reply_markup=ikb)
        await callback.answer()




if __name__ == '__main__':
    executor.start_polling(dp,
                        skip_updates=True, 
                        on_startup=on_startup)