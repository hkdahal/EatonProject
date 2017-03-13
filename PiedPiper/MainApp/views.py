from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import ArtistForm

from .search_api import SearchAPI

import json
import MainApp.api as my_api


def index(request):
    url, term = None, None

    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data['name']
            url = '/api/artist/'+term
    else:
        form = ArtistForm()

    saved_artists = my_api.lookup_saved_files()

    return render(request, 'MainApp/pages/index.html',
                  {
                      'form': form,
                      'url': url,
                      'term': term,
                      'saved_artists': saved_artists,
                      'current': 'Homepage'
                   })


def details(request, id):
    data = SearchAPI().lookup_id(id)[0]
    return render(request, 'MainApp/pages/details.html', {'data': data})


def save_data(request, term):
    data = SearchAPI().search_artist(term)

    # Writing JSON data
    with open('MainApp/saved-data/'+term+'.json', 'w') as f:
        json.dump(data, f)

    return HttpResponse('Saved ' + term + ' file.')


def show_saved_result(request, artist):
    form = ArtistForm(initial={'name': artist})
    return render(request, 'MainApp/pages/index.html',
                  {
                      'form': form,
                      'url': '/api/saved/'+artist,
                      'saved_artists': my_api.lookup_saved_files(),
                      'saved_data': True,
                      'current': 'Homepage'
                   })


def load_file(request):
    if request.method == 'POST':
        file = request.FILES.getlist('my_file')[0]
        file_name = request.POST['file_name']
        if my_api.handle_uploaded_file(file, file_name):
            return HttpResponseRedirect('/show/'+file_name)
    else:
        return render(request, 'MainApp/pages/upload_file.html',
                      {'current': 'LoadFile'})


def usage_guide(request):
    return render(request, 'MainApp/pages/usage_guide.html',
                  {'current': 'UsageGuide'})



