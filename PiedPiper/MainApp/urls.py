from django.conf.urls import url
import MainApp.views as v
import MainApp.api as api

urlpatterns = [
    url(r'^api/artist/(?P<name>[a-zA-Z\s]+)', api.get_data),
    url(r'^api/saved/(?P<artist>[a-zA-Z\s]+)', api.load_saved_data),
    url(r'^details/(?P<id>\d+)', v.details),
    url(r'^save/(?P<term>[a-zA-Z\s]+)', v.save_data),
    url(r'^show/(?P<artist>[a-zA-Z\s]+)', v.show_saved_result),
    url(r'^load-file', v.load_file),
    url(r'^$', v.index),
]
