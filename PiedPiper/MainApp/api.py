from django.shortcuts import HttpResponse
from .search_api import SearchAPI

import glob
import json
import ntpath
import os

import MainApp


def get_data(request, name):
    result = SearchAPI().search_artist(name)
    return HttpResponse(json.dumps(result), content_type="application/json")


def load_saved_data(request, artist):
    file = os.path.dirname(MainApp.__file__) + '/saved-data/' + artist + '.json'

    # Reading data back
    with open(file, 'r') as f:
        data = json.load(f)
    return HttpResponse(json.dumps(data), content_type="application/json")


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



