import logging
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from exceptions import BaseError
from settings import log_handler, BOT_TOKEN
from utils import template_render, create_audio_message, get_audio_file

logger = logging.getLogger(__name__)
logger.addHandler(log_handler)


def get_help(bot, update):
    help_info_str = template_render(tpl_path='help.txt', context={})
    update.message.reply_text(help_info_str)


def get_audio_message(bot, update):
    create_audio_message(update.message.text)
    audio_file = open(get_audio_file(), 'rb')
    bot.send_audio(
        chat_id=update.message.chat_id,
        audio=audio_file,
        title=datetime.datetime.now(),
    )


def error(bot, update, error):
    raise BaseError(msg='Update "%s" caused error "%s"' % (update, error), logger=logger)


def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", get_help))
    dp.add_handler(MessageHandler(Filters.text, get_audio_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
