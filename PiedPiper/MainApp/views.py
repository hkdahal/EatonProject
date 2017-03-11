from django.shortcuts import render


def index(request):
    return render(request, 'MainApp/index.html', {})


def artist_input(request):
    if request.method == "POST":
        # do stuff
        pass
    else:
        pass


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

