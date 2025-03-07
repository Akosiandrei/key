import random
import string
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# File to store generated keys
KEYS_FILE = "keys.json"

def load_keys():
    try:
        with open(KEYS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_keys(keys):
    with open(KEYS_FILE, "w") as f:
        json.dump(keys, f)

def generate_key(update: Update, context: CallbackContext):
    """Generate a new key and store it."""
    new_key = "premiumkey" + ''.join(random.choices(string.digits, k=6))
    keys = load_keys()
    keys.append(new_key)
    save_keys(keys)
    
    update.message.reply_text(f"Generated Key: {new_key}\nUse it on the key system!")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Use /generate to get a key.")

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("generate", generate_key))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
