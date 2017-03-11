from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import ArtistForm

from .search_api import SearchAPI

import json


def index(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            return render(request, 'MainApp/pages/index.html',
                          {'form': form,
                           'url': '/artist/'+form.cleaned_data['name']
                           }
                          )
    else:
        form = ArtistForm()

    return render(request, 'MainApp/pages/index.html', {'form': form})


def get_data(request, name):
    print(name)
    api = SearchAPI()
    result = api.search_term(name)
    return HttpResponse(json.dumps(result), content_type="application/json")


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

