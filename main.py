import telebot
from datetime import datetime, timedelta


#telegarm bot token to connect 
BOT_TOKEN = '5605538577:AAFILijcsfGyPLrhJLa4NkrXdMAyKfwT4JU'

#creating an instance for bot with the token
bot = telebot.TeleBot(BOT_TOKEN)

#created messgae handler to response to the user queries at start.
@bot.message_handler(commands=['start', 'hello'])
#function to response as soon as a user starts the telebot
def send_welcome(message):
    bot.reply_to(message, "Hello, how are you doing?")

#created message handlerfor /book or /Book command
@bot.message_handler(commands=['book','Book'])

#function to get user name 
def getName(message):
    text = 'Please type in your Name'
    user_name = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(user_name, getLocation)
    
#function to get location of booking from user
def getLocation(message):
    #text to ask user to give his desired location
    text = 'Please type in your Location'
    user_location = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(user_location, getDate)

#function to get date of slot booking from user
def getDate(message):
    #get today's date 
    today = datetime.now()
    #making todays date in user readable format 
    firstday = today.strftime("%d"+" "+"%B"+" "+"%Y")
    #getting date for tomorrow's day
    secondday = (today + timedelta(days=1)).strftime("%d"+" "+"%B"+" "+"%Y")
    #getting third date
    thirdday = (today + timedelta(days=2)).strftime("%d"+" "+"%B"+" "+"%Y")
    #text to ask user the query to give date of booking
    text = f'Which date you want to book your slot? {firstday} /n {secondday} /n {thirdday}'
    booking_date = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(booking_date, getTime)

#function to get time of booking from user
def getTime(message):   
    text = f'Which time you want to book your slot? 10:00 AM /n 2:00 PM /n 5:00 PM'
    booking_time = bot.send_message(message.chat.id, text, parse_mode="Markdown")

#function to echo back the text from user
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
