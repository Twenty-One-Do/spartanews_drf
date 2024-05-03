from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('Account.urls')),
    path('api/article/', include('Article.urls')),
]
