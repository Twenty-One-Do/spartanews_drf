from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('latest', views.LatestArticleListView.as_view()),
    path('<int:pk>', views.ArticleDetailView.as_view()),
    path('<int:pk>/likes', views.article_likes),
    path('<int:pk>/comment/', views.CommentListView.as_view()),
    path('comment/<int:pk>', views.CommentDetailView.as_view()),
    path('comment/<int:pk>/likes', views.comment_likes),
]