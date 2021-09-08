
from django.urls import path,re_path,include
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.post_view.as_view(),name='index'),
    path("category/<str:slug>/",views.CategoryList.as_view(),name='category'),
    path("tag/<str:slug>/",views.TagList.as_view(),name='tag'),
    re_path(r'^success/$',views.success.as_view(),name='success'),
    path("<str:slug>",views.post_detail.as_view(),name='detail'),
    path('api/',include('blog.api.api_urls')),
    path('search/',views.SearchList.as_view(),name='search'),

]
