import logging
import telegram
from token import TOKEN


LAST_UPDATE_ID = None

def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot(TOKEN)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)

def serveOptions(bot, chat_id, message):
    options = """
            Search API Wrapper which helps to query loklak for JSON results.\n
            Status API Wrapper for the loklak status check.\n
            Suggestions API Wrapper , Works better with local loklak instance.\n
            Crawler API Wrapper on Loklak to crawl for tweets for a particular crawl depth.\n
            Loklak status check API.\n
            Geocode API for geolocation based information.\n
            Loklak API for peers connected on the distributed network.\n
            Public API to push geojson objects to the loklak server.\n
            User API to show twitter user information.\n
            Map Visualization render using Loklak service.\n
            Markdown conversion API to render markdown as image using Loklak.\n
            """
    bot.sendMessage(chat_id=chat_id, text=options)

def stringParse(bot, messageString, LAST_UPDATE_ID):
    # String parser functions that are required for the bot.
    global LAST_UPDATE_ID

    # String parse as required according to the functions
    mQueryType = messageString.split(' ')[0] # First element containing the / element
    if mQueryType == '/search':
        # do some operations
    elif mQueryType == '/status':
        # do some operations
    elif mQueryType == '/suggest':
        # do some operations
    elif mQueryType == '/crawler':
        # do some operations
    elif mQueryType == '/geocode':
        # do some operations
    elif mQueryType == '/user':
        # do some operations
    else:
        return 'This command is not the command that the bot recognizes. Please try again.'

def echo(bot):
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')

        if message == '/start' or message == '/help':
            serveOptions(bot, chat_id, message)

        if (message):
            # Reply the message
            print str(chat_id) + ' :: ' + str(message)
            bot.sendMessage(chat_id=chat_id,
                            text=message)

            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1


if __name__ == '__main__':
    main()