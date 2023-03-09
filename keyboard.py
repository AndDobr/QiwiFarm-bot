from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(KeyboardButton(text='💫Добавить токен💫'))
start_keyboard.add(KeyboardButton(text='🌐 Добавить несколько токенов🌐'))
start_keyboard.add(KeyboardButton(text='🔰Информация🔰'), KeyboardButton(text='📊Статистика📊'))
start_keyboard.add(KeyboardButton(text='📥Указать реквизиты📥'))

props = InlineKeyboardMarkup()
props.add(InlineKeyboardButton(text='🏵Ввести реквизиты🏵', callback_data='props'))

check_payment = ReplyKeyboardMarkup(resize_keyboard=True)
check_payment.add(KeyboardButton(text='Проверить оплату'))
check_payment.add(KeyboardButton(text='Отмена'))

admin = ReplyKeyboardMarkup(resize_keyboard=True)
admin.add(KeyboardButton(text='Забрать доступ'))
admin.add(KeyboardButton(text='Выдать доступ'))
