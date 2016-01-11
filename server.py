import logging
import telegram
from token import BOT_TOKEN

from commands import serveOptions, search, status, user, geocode, markdown
from utils import return_reply, return_image

LAST_UPDATE_ID = None

commands = {
    'no-args': ['/start', '/help', '/status'],
    'with-args': ['/search', '/suggest', '/crawler', '/geocode', '/user', '/markdown']
}


def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot(BOT_TOKEN)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)


def stringParse(bot, messageString):
    # String parser functions that are required for the bot.
    global LAST_UPDATE_ID

    # String parse as required according to the functions
    try:
        command, query = messageString.split(' ', 1)
    except ValueError:
        # single argument given
        command = messageString
        if command in commands['no-args']:
            if command == '/start' or command == '/help':
                return serveOptions()
            elif command == '/status':
                return status()
        else:
            if command in commands['with-args']:
                return 'Sorry, you have to pass some arguments to {}'.format(command)
            else:
                return 'Sorry, but I don\'t know what to do with {}'.format(command)

    if command in commands['with-args']:
        if command == '/search':
            return search(query)
        elif command == '/suggest':
            # do some operations
            'Sorry, but I don\'t know what to do with {}'.format(command)
        elif command == '/crawler':
            # do some operations
            'Sorry, but I don\'t know what to do with {}'.format(command)
        elif command == '/geocode':
            return geocode(query)
        elif command == '/user':
            return user(query)
        elif command == '/markdown':
            return markdown(query)
    else:
        return 'Sorry, but I don\'t know what to do with {}'.format(command)


def echo(bot):
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')

        if message:
            # Reply the message
            print str(chat_id) + ' :: ' + str(message)
            reply = stringParse(bot, message)
            if isinstance(reply, list):
                for reply_instance in reply:
                    return_reply(bot, chat_id, reply_instance)
            elif isinstance(reply, str):
                if "markdown" in message:
                    return_image(bot, chat_id, reply)
                else:
                    return_reply(bot, chat_id, {'text': reply})
            else:
                return_reply(bot, chat_id, reply)

            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1


if __name__ == '__main__':
    main()
