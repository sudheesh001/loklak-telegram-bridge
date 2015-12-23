def get_tweet_rating(tweet):
    """
    Function that returns tweet rating based on its favourites and retweets
    """
    return (tweet['retweet_count'] * 2) + tweet['favourites_count']

def tweet_reply(tweet, tweets_left):
    """
    Function that returns a tweet from the loklak object
    """
    reply = '"{message}" - {author} \n\n{link}\n\n and {more} more tweets.'.format(
        message=unicode(tweet['text']),
        author=unicode(tweet['screen_name']),
        link=unicode(tweet['link']),
        more=tweets_left
    )
    return reply