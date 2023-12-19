import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_WEBSITE_URL' with the actual URL you want to scrape
WEBSITE_URL = 'https://ez4short.xyz'

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6710510477:AAE3YFDMHWT3d6prygYFzlc285OmpQPpZB0'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Use /balance to check the balance.')

def balance(update: Update, context: CallbackContext) -> None:
    try:
        # Make a request to the website and parse the HTML
        response = requests.get(WEBSITE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the balance information (replace 'your_balance_selector' with the actual HTML selector)
        balance_element = soup.select_one('your_balance_selector')
        balance = balance_element.text if balance_element else 'Balance not found.'

        update.message.reply_text(f'Balance: {balance}')

    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}')

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("balance", balance))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
