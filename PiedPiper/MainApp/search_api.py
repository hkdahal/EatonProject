import json
import requests


def make_request(url):
    try:
        return 'success', requests.get(url)
    except requests.exceptions.ConnectionError:
        return 'connection error', None


def call_api(url):

    response = make_request(url)

    if response[0] == 'success':
        data = response[1].json()
        if 'results' in data:
            return data['results']
    elif response[0] == 'connection error':
        return 'Connection Error'


class SearchAPI:

    def __init__(self):
        self.api_search_url = "https://itunes.apple.com/search?"
        self.api_lookup_url = "http://itunes.apple.com/lookup?"

    def search_artist(self, term):
        url = self.make_search_url(term)
        return call_api(url)

    def lookup_id(self, given_id):
        url = self.api_lookup_url + "id=" + given_id
        return call_api(url)

    def make_search_url(self, term):
        return self.api_search_url + "term="+"+".join(term.split()) + \
               "&entity=musicTrack"
