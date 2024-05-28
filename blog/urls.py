from django.urls import path
from .views import home, category_list, category_detail, article, contact, about

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('category_list/', category_list, name='category_list'),
    path('category_detail/<slug:slug>/', category_detail, name='category_detail'),
    path('article/<slug:slug>/', article, name='article'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
