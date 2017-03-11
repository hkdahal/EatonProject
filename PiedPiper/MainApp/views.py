from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import ArtistForm

from .search_api import SearchAPI

import json


def index(request):
    return render(request, 'MainApp/pages/cool.html', {})


def artist_input(request):
    if request.method == "POST":
        # do stuff
        form = ArtistForm(request.POST)
        if form.is_valid():
            api = SearchAPI()
            result = api.search_term(form.cleaned_data['name'])
            return HttpResponse(json.dumps(result),
                                content_type="application/json")
    else:
        # form = ArtistForm()
        api = SearchAPI()
        result = api.search_term('jack johnson')
        return HttpResponse(json.dumps(result),
                            content_type="application/json")
    return render(request, 'MainApp/index.html', {'form': form})


"""
Provide following info:
Artist Name, Track Name, Release Date, Collection Name, Collection Price,
Track Price, Track Number, Track Count,
Image (bonus points),
Kind and Primary Genre Name.
"""


def file_read(file_name):
    # process the file
    #
    pass


def save_file(data):
    # process the data
    # write the data in the file
    # save the file
    pass


def instantiate_apple_api():
    # instantiate the API object
    pass


def connect_url_call_api(API, artist):
    # concatenate API url and artist
    # get the result
    # call to process the result
    pass


def process_api_result(data):
    # process the data
    # necessary displaying stuff
    pass

# function to get user's input
# process user input
# Apple's API Connector
# call Apple's API
# process the API result
# display API result
# AJAX call handling?
# file saving handled
# file read handled

