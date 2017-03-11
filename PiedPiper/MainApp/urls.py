from django.conf.urls import url
import MainApp.views as v

urlpatterns = [
    url(r'^artist', v.artist_input),
    url(r'^', v.index),

]
