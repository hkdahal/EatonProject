import requests


class SearchAPI:

    def __init__(self):
        self.api_url = "https://itunes.apple.com/search?"

    def search_term(self, term):
        url = "term="+"+".join(term.split())
        return self.call_api(url)

    def call_api(self, url):
        the_url = self.api_url + url
        response = requests.get(the_url)
        data = response.json()['results']
        return data
