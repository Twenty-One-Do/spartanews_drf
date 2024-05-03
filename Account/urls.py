from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenBlacklistView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='index'),
    path('refresh/', TokenRefreshView.as_view(), name='index'),
    path('refresh/blacklist/', TokenBlacklistView.as_view(), name='index'),

    path('', views.signup),
    path('<int:pk>', views.AccountView.as_view()),
    path('<int:pk>/password', views.change_password),
]