import requests


class SearchAPI:

    def __init__(self):
        self.api_search_url = "https://itunes.apple.com/search?"
        self.api_lookup_url = "http://itunes.apple.com/lookup?"

    def search_term(self, term):
        url = "term="+"+".join(term.split())
        return self.call_api(url)

    def search_artist(self, term):
        url = self.api_search_url + "term="+"+".join(term.split()) + "&entity=musicTrack"
        return self.call_api(url)

    def lookup_id(self, given_id):
        url = self.api_lookup_url + "id=" + given_id
        return self.call_api(url)

    def call_api(self, url):
        the_url = url
        try:
            response = requests.get(the_url)
            data = response.json()
            if 'results' in data:
                data = data['results']
            return data
        except requests.exceptions.ConnectionError:
            return 'Connection Error'

