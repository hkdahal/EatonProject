from django.conf.urls import url
import MainApp.views as v

urlpatterns = [
    url(r'^artist/(?P<name>[a-zA-Z\s]+)', v.get_data),
    url(r'^details/(?P<id>\d+)', v.details),
    url(r'^save/(?P<term>[a-zA-Z\s]+)', v.save_data),
    url(r'^saved/(?P<artist>[a-zA-Z\s]+)', v.load_saved_data),
    url(r'^show/(?P<artist>[a-zA-Z\s]+)', v.show_saved_result),
    url(r'^load-file', v.load_file),
    url(r'^$', v.index),
]
