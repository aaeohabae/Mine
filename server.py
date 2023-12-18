def get_api(update,context):
    keyboard = [
                [InlineKeyboardButton("Get Token", url="EZ4short.xyz/member/tools/api")],
                
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = """• First Visit EZ4short.xyz/member/tools/api
• Copy the API TOKEN and come back to Bot.
• Input  /token and Paste The token Copied from EZ4short.xyz/member/tools/api
• Now bot will successfully connected to your  EZ4short.xyz account."""
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)

def api_Logout(update, context):
    user = update.message.from_user
    username = user.username
    resp=logout(username)
    if resp == True:
        update.message.reply_text("You are Logged Out SuccessFully")
    elif resp == False:
        update.message.reply_text("You Haven't Login Yet Please Login First")
    else:
        update.message.reply_text("Something Went Wrong")
# Set up the bot and its message handler
def main():
    bot = telegram.Bot("6708893772:AAERnYm2-JsuOUvjsr84UiYNn2HJg7kmWzU")
    updater = telegram.ext.Updater(bot.token, use_context=True)
    disp = updater.dispatcher
    disp.add_handler(telegram.ext.CommandHandler('start',start))
    disp.add_handler(telegram.ext.CommandHandler('help',help))
    disp.add_handler(telegram.ext.CommandHandler('login',api_Login))
    disp.add_handler(telegram.ext.CommandHandler('get_api',get_api))
    disp.add_handler(telegram.ext.CommandHandler('logout',api_Logout))
    disp.add_handler(telegram.ext.CommandHandler('features',feature))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.all, handle_message))
    updater.start_polling()

if name == "main":
    main()
