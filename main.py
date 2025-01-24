from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

user_date = {}

bot = TeleBot(token = "8106082048:AAFueovRPcYZVvBNCLi5a6BW3YJ8doH_P-c")

@bot.message_handler(commands =["start"] )
def boshlanishi(message:types.Message):
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True)
    mark_up.add(KeyboardButton(text = "Ro'yhatdan o'tish"))
    bot.send_message(message.chat.id,"Assalomu aleykum botimizga hush kelibsiz",
                     reply_markup = mark_up)

@bot.message_handler(func = lambda message: message.text == "Ro'yhatdan o'tish")
def Royhatdan_otish(message:types.Message):
    markup = ReplyKeyboardRemove()
    user_date[message.from_user.id] = {}
    bot.send_message(message.chat.id, "Ismingizni kiriting", reply_markup = markup)

@bot.message_handler(func = lambda message: message.from_user.id in user_date and 'name' not in user_date[message.from_user.id])
def Ismi(message:types.Message):
    user_date[message.from_user.id]['name'] = message.text
    bot.send_message(message.chat.id, "Familiyangizni kiriting")

@bot.message_handler(func = lambda message: message.from_user.id in user_date and 'surname' not in user_date[message.from_user.id])
def Familiya(message:types.Message):
    user_date[message.from_user.id]['surname'] = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text = "Kontakni yuborish", request_contact=True))
    bot.send_message(message.chat.id, "Telefoningizni kiriting", reply_markup = markup)

@bot.message_handler(content_types = ["contact"])
def Telefon(message:types.Message):
    user_date[message.from_user.id]['phone'] = message.contact.phone_number
    bot.send_message(message.chat.id, "Ro'yhatdan muvofaqiyatli otingiz ")

bot.polling()
