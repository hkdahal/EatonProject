from django.conf.urls import url
import MainApp.views as v

urlpatterns = [
    url(r'^', v.index),
]
