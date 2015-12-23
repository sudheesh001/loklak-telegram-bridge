def get_tweet_rating(tweet):
    """
    Function that returns tweet rating based on its favourites and retweets
    """
    return (tweet['retweet_count'] * 2) + tweet['favourites_count']


def tweet_reply(tweet, tweets_left):
    """
    Function that returns a tweet from the loklak object
    """
    reply = '"{message}" - {author}\n\n{link}\n\n and {more} more tweets.'
    reply = reply.format(
        message=tweet['text'],
        author=tweet['screen_name'],
        link=tweet['link'],
        more=tweets_left
    )
    reply = reply.encode('utf-8')
    return reply


def user_reply(user):
    reply = """
        {name} - {screen_name}\n
        {description}
        Statuses count: {statuses_count}
        Favourites count: {favourites_count}
        Followers count: {followers_count}
        Following: {following_count}

        {img}
    """
    reply = reply.format(name=user['name'], screen_name=user['screen_name'],
                         description=user['description'],
                         statuses_count=user['statuses_count'],
                         favourites_count=user['favourites_count'],
                         followers_count=user['followers_count'],
                         url=user['url'],
                         following_count=user['friends_count'],
                         img=user['profile_image_url'])
    reply = reply.encode('utf-8')
    return reply
