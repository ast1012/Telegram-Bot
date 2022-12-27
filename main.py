import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import pytz
from datetime import datetime, date


telegram_token = "5870426743:AAF-xcemht8p3tQx2FI_T7_sq0OvXe4jrvA"
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]

    # try:
        # client.query(q.get(q.match(q.index("users_index"), chat_id)))
    # context.bot.send_message(chat_id=chat_id, text='''Welcome to Fauna Appointment Scheduler Bot \n\n
    #         To schedule an appointment enter /add_appointment \n To list al appointment enter 
    #         /list_appointments \n To list all 
    #         appointments you have today enter /list_today_appointments''')

    # except:
    #     user = client.query(q.create(q.collection("Users"), {
    #         "data": {
    #             "id": chat_id,
    #             "first_name": first_name,
    #             "username": username,
    #             "last_command": "",
    #             "date": datetime.now(pytz.UTC)
    #         }
    #     })) 

    context.bot.send_message(chat_id=chat_id, text='''Welcome! I am Olive a Bot, I am here to make your todo-list
    \n\n To make todo-task list  /make_todo_list \n 
     \n List all the tasks for today /tasks_for_today
    ''')


def make_list(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='''Enter the tasks you want to list seprated by coma''')


def echo(update, context):
    chat_id = update.effective_chat.id
    message = update.message.text
    todo_list = message.split(",")
    for item in todo_list:
        context.bot.send_message(chat_id=chat_id, text=f"Successfully made todo-list {item}")
    



dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("make_todo_list", make_list))
dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
