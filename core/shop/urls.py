from django.urls import path,include
from . import views
app_name = 'shop'
urlpatterns = [
path('',views.Allproduct.as_view(),name="allproduct"),
path("<str:slug>/",views.ProductList.as_view(),name='detail'),
path("category/<str:slug>/",views.CategoryList.as_view(),name='category'),
path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
path('api/',include('shop.api.api_urls')),
path('order-summary', views.OrderSummaryView.as_view(), name='order-summary'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
]

