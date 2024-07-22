from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



main_menu = ReplyKeyboardMarkup(resize_keyboard=True)


main_menu.add(KeyboardButton('Menu'))

restaurant_menu = ReplyKeyboardMarkup(resize_keyboard=True)
restaurant_menu.add(
    KeyboardButton(text='🌯Lavashlar🌯'),
    KeyboardButton(text='🍔Burgerler🍔'),

    
)
restaurant_menu.add(
    KeyboardButton(text='🍣Sushilar🍣'),
    KeyboardButton(text='🍟Freelar🍟'))

restaurant_menu.add(
    KeyboardButton(text='🍕Pizzalar🍕'),
    KeyboardButton(text='🥤Ishimlikler🥤')
)

lavash_menu = InlineKeyboardMarkup()

lavash_menu.add(
    InlineKeyboardButton(text='Standart Lavash',callback_data='standart'),
    InlineKeyboardButton(text='Double Lavash',callback_data='double'),
    )

lavash_menu.add(
    InlineKeyboardButton(text='Mini Lavash',callback_data='mini'),
    InlineKeyboardButton(text='Cheese Lavash',callback_data='cheese'))

lavash_menu.add(
    InlineKeyboardButton(text='Tandir Lavash',callback_data='tandir'),
    InlineKeyboardButton(text='Spicy Lavash',callback_data='spicy')
)


lavash_menu = InlineKeyboardMarkup()

lavash_menu.add(
    InlineKeyboardButton(text='Standart Lavash',callback_data='standart'),
    InlineKeyboardButton(text='Double Lavash',callback_data='double'),)





