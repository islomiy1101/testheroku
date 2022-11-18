from django.urls import path
from news.views import *
urlpatterns=[
    path('',home,name='home-page'),
    path('about/',about,name='about-page'),
    path('contact/',contact,name='contact-page'),
    path('article_detail/<slug:slug>/',article_detail,name='article_detail-page'),
]