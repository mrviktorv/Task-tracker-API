from django.conf.urls import url
from myapp import views
from django.urls import path

urlpatterns=[

    url(r'^tasks$', views.taskApi),
    url(r'^tasks/([0-9]+)$', views.taskOneApi)

]
