from django.conf.urls import url
from myapp import views
from django.urls import path

urlpatterns=[
    # path('tasks/', views.taskApi),
    # path('tasks/<int:TaskId>/', views.taskApi)\
    url(r'^tasks$', views.taskApi),
    url(r'^tasks/([0-9]+)$', views.taskOneApi)
    # url(r'^tasks/([0-9]+)$', views.taskOneApi)
    # 
    # path('tasks/<int:TaskId>', views.taskOneApi)
]