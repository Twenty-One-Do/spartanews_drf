from django.urls import path
from . import views
from .views import summarize

urlpatterns = [
    path('summarize/', summarize, name='summarize'),
]
