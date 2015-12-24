from utils import get_tweet_rating, tweet_reply, user_reply, place_text_reply
from loklak import Loklak

l = Loklak()


def status():
    """Get the server status.

    Returns:
        server status.

    """
    status_reply = l.hello()['status']
    if status_reply == 'ok':
        status_reply = 'I am okay!'
    context = {
        'text': status_reply
    }
    return context


def search(query):
    """Search Loklak for a specific query.

    Args:
        query: the query to search for.
    Returns:
        tweet object for the query.

    """
    tweets = l.search(query)['statuses']
    if tweets:
        tweets.sort(key=get_tweet_rating)
        tweet = tweets.pop()
        context = {
            'text': tweet_reply(tweet, len(tweets))
        }
        return context
    else:
        # Try to search for a weaker query by deleting the last word
        # "An awesome query" -> "An awesome" -> ...
        query = query.split()[:-1]
        if query:
            query = ' '.join(query)
            search(query)
        else:
            return {
                'text': 'Sorry, I haven\'t found any informarion for your query'
            }


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
        return {
            'text': 'Sorry, I haven\'t found any informarion about {}'.format(
                screen_name)
        }
    context = {
        'text': user_reply(user)
    }
    return context


def geocode(places_names):
    """Search Loklak for a specific geolocation.

    Args:
        places: comma separated list of places.
    Returns:
        place, population, country, country_code and location from Google.

    """
    context = []
    places = l.geocode(places_names)['locations']
    for place_name, place in places.iteritems():
        if place:
            place_reply = {
                'text': place_text_reply(place_name, place),
                'location': {
                    'longitude': place['location'][0],
                    'latitude': place['location'][1]
                }
            }
            context.append(place_reply)
        else:
            context.append(dict(
                text='Sorry, I haven\'t found any geo informarion for {}'.format(place_name)))
    return context


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
    context = {
        'text': options
    }
    return context
