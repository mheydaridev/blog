from django.urls import path
from .views import home, article

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('article/<slug:slug>/', article, name='article'),
]
