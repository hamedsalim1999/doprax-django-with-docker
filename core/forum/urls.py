from django.urls import path,re_path,include
from . import views 

# app_name = 'forum'
urlpatterns = [
    re_path(r'^$', views.ThreadFormSend.as_view(), name='index'),
    path('newthread/', views.new_thread.as_view(), name='new_thread'),
    path('newreplay/', views.new_replay.as_view(), name='newreplay'),
    path("<str:slug>/",views.ThreadView.as_view(),name='detail'),
    path('api/',include('forum.api.api_urls'))
]


