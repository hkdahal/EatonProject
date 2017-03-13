from io import TextIOWrapper

from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import ArtistForm

from .search_api import SearchAPI

import glob
import json
import ntpath
import os
import MainApp


def index(request):
    url, term = None, None

    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data['name']
            url = '/artist/'+term
    else:
        form = ArtistForm()

    saved_artists = lookup_saved_files()

    return render(request, 'MainApp/pages/index.html',
                  {
                      'form': form,
                      'url': url,
                      'term': term,
                      'saved_artists': saved_artists,
                      'current': 'Homepage'
                   })


def get_data(request, name):
    result = SearchAPI().search_artist(name)
    return HttpResponse(json.dumps(result), content_type="application/json")


def details(request, id):
    data = SearchAPI().lookup_id(id)[0]
    return render(request, 'MainApp/pages/details.html', {'data': data})


def save_data(request, term):
    data = SearchAPI().search_artist(term)

    # Writing JSON data
    with open('MainApp/saved-data/'+term+'.json', 'w') as f:
        json.dump(data, f)

    lookup_saved_files()
    return HttpResponse('saved ' + term + ' file.')


def load_saved_data(request, artist):
    file = os.path.dirname(MainApp.__file__) + '/saved-data/' + artist + '.json'

    # Reading data back
    with open(file, 'r') as f:
        data = json.load(f)
    return HttpResponse(json.dumps(data), content_type="application/json")


def show_saved_result(request, artist):
    form = ArtistForm(initial={'name': artist})
    return render(request, 'MainApp/pages/index.html',
                  {
                      'form': form,
                      'url': '/saved/'+artist,
                      'saved_artists': lookup_saved_files(),
                      'saved_data': True,
                      'current': 'Homepage'
                   })


def load_file(request):
    if request.method == 'POST':
        file = request.FILES.getlist('my_file')[0]
        file_name = request.POST['file_name']
        # the_data = TextIOWrapper(file.file, encoding=request.encoding)
        if handle_uploaded_file(file, file_name):
            return HttpResponseRedirect('/show/'+file_name)
    else:
        return render(request, 'MainApp/pages/upload_file.html',
                      {'current': 'LoadFile'})


def lookup_saved_files():
    path = os.path.dirname(MainApp.__file__)
    file_paths = glob.glob(path+'/saved-data/*.json')
    return [path_leaf(path).split('.')[0] for path in file_paths]


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def handle_uploaded_file(file, file_name):
    try:
        file_path = os.path.dirname(
            MainApp.__file__) + '/saved-data/' + file_name
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return True
    except:
        return False


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

