from django.urls import path
from . import views

# for better to use set app name , if we set this app name we can remove movies in name
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name = 'detail')

]