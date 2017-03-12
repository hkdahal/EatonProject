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
    result = SearchAPI().search_artist(name)
    return HttpResponse(json.dumps(result), content_type="application/json")


def details(request, id):
    data = SearchAPI().lookup_id(id)[0]
    return render(request, 'MainApp/pages/details.html', {'data': data})


def save_data(request, term):
    return HttpResponse('saved ' + term + ' file.')


def file_read(file_name):
    # process the file
    #
    pass


def save_file(data):
    # process the data
    # write the data in the file
    # save the file
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

