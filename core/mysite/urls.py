from django.urls import re_path
from django.urls.conf import include,path,include
from . import views
urlpatterns = [
    re_path(r'^contact$',views.contact_form.as_view(),name='contact'),
    path(r'',views.Index.as_view(),name='contact'),
    re_path(r'^about$',views.About.as_view(),name='contact'),
    path('api/',include('mysite.api.api_urls')),
]
