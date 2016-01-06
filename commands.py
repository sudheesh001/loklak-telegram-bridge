from utils import get_tweet_rating, tweet_reply, user_reply, place_text_reply
import textrazor
from loklak import Loklak
from token import TEXT_TOKEN

l = Loklak()
textrazor.api_key = TEXT_TOKEN
client = textrazor.TextRazor(extractors=["entities"])

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
    score = {}
    try:
        tweets = l.search(query)['statuses']
        tweet = tweets.pop()
        context = {
            'text': tweet_reply(tweet, len(tweets))
        }
    except IndexError:
		print "Searching for the most Relavent Item..!"
		response = client.analyze(query)
		for e in response.entities():
			score[e.id] = e.confidence_score
		key = sorted(score.values())[-1]
		tweets = l.search(
			score.keys()[score.values().index(key)])['statuses']
		tweet = tweets.pop()
		context = {
            'text': tweet_reply(tweet, len(tweets))
        }
    return context


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
