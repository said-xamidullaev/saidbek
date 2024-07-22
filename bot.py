from aiogram import Dispatcher,Bot,executor,types
from keybords import main_menu,restaurant_menu,lavash_menu
api = '7497568630:AAHeIzDyxdb1qw_4_itgt-Ds591fVaYoaXo'
bot = Bot(api)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    logo = open(file='tg_bots/lesson_3/images/images.jfif',mode='rb')
    await sms.answer_photo(
        photo=logo,
        caption=f'''Assalamu aleykum {sms.from_user.first_name}.
Botimizga xosh keldiniz.
Menudi koriw ushin menu tuymesin basin
''',reply_markup=main_menu)
@dp.message_handler(text='Menu')#/
async def send_menu(sms:types.Message):
    await sms.answer(text='Bizdin kafenin menusi:',
                     reply_markup=restaurant_menu)
    
@dp.message_handler(text='🌯Lavashlar🌯')
async def send_lavashs(sms:types.Message):
    await sms.answer(
        text='Bizde tomendegishe lavash turleri bar:👇',
        reply_markup=lavash_menu
        )

@dp.message_handler(text='🍔Burgerler🍔')
async def send_lavashs(sms:types.Message):
    await sms.answer(
        text='Bizde tomendegishe Burgerler turleri bar:👇',
        reply_markup=lavash_menu
        )













@dp.callback_query_handler()
async def send_tamaqs(call:types.CallbackQuery):
    data = call.data
    if data=='standart':
        standart = open(file='tg_bots/lesson_3/images/Без названия.jfif',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=standart,
            caption='Siz standart lavashti sayladiniz bul lavasdin cenasi 27000 sum '
        )
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
