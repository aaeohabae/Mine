import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_API_ENDPOINT' with the actual API endpoint for checking balance
API_ENDPOINT = '12b2d8281afa6d870f9b44bd0cba166704c7ea50'

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6710510477:AAE3YFDMHWT3d6prygYFzlc285OmpQPpZB0'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Use /balance to check the balance.')

def balance(update: Update, context: CallbackContext) -> None:
    try:
        # Replace 'YOUR_ACCOUNT_ID' and 'YOUR_API_KEY' with your actual account ID and API key
        account_id = '2'
        api_key = '6710510477:AAE3YFDMHWT3d6prygYFzlc285OmpQPpZB0'

        # Make a request to the API to get the balance
        headers = {'Authorization': f'Bearer {api_key}'}
        params = {'account_id': account_id}
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        data = response.json()

        # Extract the balance from the API response (adjust as per the API structure)
        balance = data.get('balance', 'Balance not found.')

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
  