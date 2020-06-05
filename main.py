import logging
import functions

from telegram.ext import Updater, CommandHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = '1194601727:AAFBiG4-47ugsxxhe6B7mJ_U8wR1Nrh3Xlk'


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def hello(update, context):
    menu = """
        This is a list of available commands:
        /albumList get the album list
        /songList <album name> : get the song list in a given album
        /songLength <song name> : get length of a given song
        /songLyrics <song name> : get lyrics of a given song
        /sourceAlbum <song name> : get source album of a given song
        /findSongName <song name> : find song by name
        /findSongLyrics <song lyrics> : find song by lyrics
        """
    update.message.reply_text(menu)


def album_list(update, context):
    update.message.reply_text(functions.get_album_list())


def song_list(update, context):
    chat_id = update.message.chat_id

    text = " ".join(context.args)
    update.message.reply_text(functions.get_song_list(text))


def song_length(update, context):
    chat_id = update.message.chat_id

    text = " ".join(context.args)
    update.message.reply_text(functions.get_song_length(text))


def song_lyrics(update, context):
    chat_id = update.message.chat_id

    text = " ".join(context.args)
    update.message.reply_text(functions.get_song_lyrics(text))


def source_album(update, context):
    chat_id = update.message.chat_id

    text = " ".join(context.args)
    update.message.reply_text(functions.get_source_album(text))


def find_song_name(update, context):
    chat_id = update.message.chat_id

    text = " ".join(context.args)
    update.message.reply_text(functions.find_song_name(text))


def find_song_lyrics(update, context):
    chat_id = update.message.chat_id

    text = " ".join(context.args)
    update.message.reply_text(functions.find_song_lyrics(text))


def main():
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", hello))
    dp.add_handler(CommandHandler("albumList", album_list))
    dp.add_handler(CommandHandler("songList", song_list, pass_args=True))
    dp.add_handler(CommandHandler("songLength", song_length, pass_args=True))
    dp.add_handler(CommandHandler("songLyrics", song_lyrics, pass_args=True))
    dp.add_handler(CommandHandler("sourceAlbum", source_album, pass_args=True))
    dp.add_handler(CommandHandler("findSongName", find_song_name, pass_args=True))
    dp.add_handler(CommandHandler("findSongLyrics", song_list, pass_args=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()


