from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Рассчитать')],
        [KeyboardButton(text = 'Информация')],
        [KeyboardButton(text = 'Купить')]
    ], resize_keyboard = True
)
ikb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')],
        [InlineKeyboardButton(text = 'Формула расчёта', callback_data = 'formulas')]
    ]
)
ikb_2 = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Зелёный чай с лимоном', callback_data = 'product_buying')],
        [InlineKeyboardButton(text = 'Смуси из шпината и банана', callback_data = 'product_buying')],
        [InlineKeyboardButton(text = 'Имбирный чай с медом', callback_data = 'product_buying')],
        [InlineKeyboardButton(text = 'Коктейль из огурца и мяты', callback_data = 'product_buying')]
    ]
)