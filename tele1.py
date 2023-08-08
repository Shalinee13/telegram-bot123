import telegram.ext

Token="6574685899:AAGLgYyPb3AL0oRLt7bbHt13c5hku_X9VY8"

updater=telegram.ext.updater("6574685899:AAGLgYyPb3AL0oRLt7bbHt13c5hku_X9VY8",use_context=True)
dispatcher=updater.dispatcher

def start(update,context):
    update.message.reply_text("Hello! welcome to sigmoid academy")

def help(update,context):
    update.message.reply_text(

    """
    /start -> welcome to the github
    /help -> this particular message
    /content -> about telegram bot
    /contact -> contact information
    """    
    )  

def content(update,context):
    update.message.reply_text("we have various bots availabe")      

def start(update,context):
    update.message.reply_text("provide your github profile")   

def help(update,context):
    update.message.reply_text("How may i help you")

def contact(update,context):
    update.message.reply_text("give me your contact info.")     

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('content',content))
dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
dispatcher.add_handler(telegram.ext.CommandHandler('contact',contact)) 

updater.start_polling()
updater.idle()