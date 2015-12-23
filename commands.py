from utils import get_tweet_rating, tweet_reply, user_reply
from loklak import Loklak

l = Loklak()


def status():
    status_reply = l.hello()['status']
    if status_reply == 'ok':
        return 'I am okay!'
    return status_reply


def search(query):
    """Search Loklak for a specific query.

    Args:
        query: the query to search for.
    Returns:
        search results for query.

    """
    tweets = l.search(query)['statuses']
    if tweets:
        tweets.sort(key=get_tweet_rating)
        tweet = tweets.pop()
        return tweet_reply(tweet, len(tweets))
    else:
        # Try to search for a weaker query by deleting the last word
        # "An awesome query" -> "An awesome" -> ...
        query = query.split()[:-1]
        if query:
            query = ' '.join(query)
            search(query)
        else:
            return 'Sorry, but I haven\'t found any tweets for your query'


def user(screen_name):
    """Search Loklak for a specific user.

    Args:
        name: the name of the user to search for.
    Returns:
        user's name, picture, description; followers, following and friends count.

    """
    try:
        user = l.user(screen_name)['user']
    except KeyError:
        return 'Sorry, I haven\'t found any informarion about {}'.format(screen_name)
    return user_reply(user)


def serveOptions():
    options = """
            Search API Wrapper which helps to query loklak for JSON results.
            Status API Wrapper for the loklak status check.
            Suggestions API Wrapper , Works better with local loklak instance.
            Crawler API Wrapper on Loklak to crawl for tweets for a particular crawl depth.
            Loklak status check API.
            Geocode API for geolocation based information.
            Loklak API for peers connected on the distributed network.
            Public API to push geojson objects to the loklak server.
            User API to show twitter user information.
            Map Visualization render using Loklak service.
            Markdown conversion API to render markdown as image using Loklak.
            """
    return options
