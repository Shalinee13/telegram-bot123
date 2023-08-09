import telebot

Token="6577074144:AAFXnVl-yQ1IXC8_7QiYVfa78ekvs6hD2ao"

bot=telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,
    """
    welcome to Sigmoid Health Care 

    /help -> For more details
    """ 
    )

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,
    """
    How may I help you?

    /About_us -> Know about   Sigmoid-Healthcare
    /Appointment -> Book Appointment
    /Contact -> Virtual assisstance
    /help -> Go back for options again
    """ 
    )
@bot.message_handler(['About_us'])
def About_us(message):
    bot.reply_to(message,
    """ Welcome to Sigmoid HealthBot, your all-in-one healthcare solution.Our specialized chatbot brings you expert consultations across distinct departments, ensuring comprehensive care tailored to your needs. From heart health in Cardiologyto brain and nerve concerns in Neurology, from mental well-being under Psychiatryto advanced imaging insights in Radiology, our certified professionals are at yourservice. Experience convenience, expertise, and personalized guidance as you navigateyour health journey with Sigmoid HealthBot. Your well-being, our priority.
      """
    )
@bot.message_handler(['Appointment'])
def Appointment(message):
    bot.reply_to(message,
    """ Select your department 
    /Cardiology
    /Neurology
    /Pyschiatry
    /Radiology
    """
    )
@bot.message_handler(['Cardiology'])
def Cardiology(message):
    bot.reply_to(message,
    """ Please give your preferred date and time for the appointment.

Then press /Next
    """
    )


@bot.message_handler(['Neurology'])
def Neurology(message):
    bot.reply_to(message,
    """ Please give your preferred date and time for the appointment.

Then press /Next
    """
    )

@bot.message_handler(['Pyschiatry'])
def Pyschiatry(message):
    bot.reply_to(message,
    """ Please give your preferred date and time for the appointment.
    
Then press /Next
    """
    )

@bot.message_handler(['Radiology'])
def Radiology(message):
    bot.reply_to(message,
    """ Please give your preferred date and time for the appointment.
    
Then press /Next
    """
    )

@bot.message_handler(['Next'])
def Next(message):
    bot.reply_to(message,"Thank you , Your appointment is booked")

 
@bot.message_handler(['Contact'])
def Contact(message):
    bot.reply_to(message,"For more assistance, call -9999988888")


bot.polling()

