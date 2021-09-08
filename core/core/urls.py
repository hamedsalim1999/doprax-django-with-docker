from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import re_path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls'),name='blog'),
    path('forum/',include('forum.urls'),name='forum'),
    path('shop/',include('shop.urls'),name='shop'),
    path('',include('mysite.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^ckeditor/$', include('ckeditor_uploader.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL , document_root = settings.MEDIA_ROOT)
