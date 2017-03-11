from django.conf.urls import url
import MainApp.views as v

urlpatterns = [
    url(r'^artist/(?P<name>[a-zA-Z\s]+)', v.get_data),
    url(r'^$', v.index),
]
