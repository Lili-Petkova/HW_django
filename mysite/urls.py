from django.urls import path

from mysite.views import triangle

app_name = "mysite"
urlpatterns = [
    path('triangle/', triangle, name="triangle"),
]
