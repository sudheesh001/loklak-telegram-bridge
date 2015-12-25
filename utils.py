def return_reply(bot, chat_id, reply):
    """
    Function that sends different info depending on the bot reply
    """
    try:
        bot.sendMessage(chat_id=chat_id,
                        text=reply['text'])
    except KeyError:
        pass
    try:
        bot.sendLocation(chat_id=chat_id,
                        latitude=reply['location']['latitude'],
                        longitude=reply['location']['longitude'])
    except KeyError:
        pass


def get_tweet_rating(tweet):
    """
    Function that returns tweet rating based on its favourites and retweets
    """
    return (tweet['retweet_count'] * 2) + tweet['favourites_count']


def tweet_reply(tweet, tweets_left):
    """
    Function that returns a tweet from a loklak object
    """
    reply = '"{message}" - {author}\n\n{link}\n\n and {more} more tweets.'
    reply = reply.format(
        message=tweet['text'].encode('utf-8'),
        author=tweet['screen_name'].encode('utf-8'),
        link=tweet['link'].encode('utf-8'),
        more=tweets_left
    )
    return reply


def user_reply(user):
    """
    Function that returns a user from a loklak object
    """
    reply = """
        {name} - {screen_name}\n
        {description}
        Statuses count: {statuses_count}
        Favourites count: {favourites_count}
        Followers count: {followers_count}
        Following: {following_count}

        {img}
    """
    reply = reply.format(name=user['name'].encode('utf-8'),
                         screen_name=user['screen_name'].encode('utf-8'),
                         description=user['description'].encode('utf-8'),
                         statuses_count=user['statuses_count'],
                         favourites_count=user['favourites_count'],
                         followers_count=user['followers_count'],
                         url=user['url'],
                         following_count=user['friends_count'],
                         img=user['profile_image_url'])
    return reply

def place_text_reply(place_name, place):
    """
    Function that returns text for a place information using a loklak object
    """
    reply = """
        {place}\n
        Population: {population}
        Country: {country}
        Country code: {country_code}
    """
    reply = reply.format(place=place_name.encode('utf-8'),
                         population=place['population'],
                         country=place['country'].encode('utf-8'),
                         country_code=place['country_code'].encode('utf-8'))
    return reply
