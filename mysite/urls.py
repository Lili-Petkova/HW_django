from django.urls import path

from mysite.views import index, new_person, select, triangle, update_person


app_name = "mysite"
urlpatterns = [
    path('triangle/', triangle, name="triangle"),
    path('person/', new_person, name="new_person"),
    path('index/', index, name="index"),
    path('person/<int:pk>/', update_person, name="update_person"),
    path('person/select/', select, name='select')
]
