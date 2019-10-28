from django.urls import path

from . import views


app_name = 'twitteru'

urlpatterns = [
    path('home/', views.UserHomeView.as_view(), name='home'),
    path('user/<int:pk>/', views.UserPageView.as_view(), name='userpage'),
    path('user/follow/', views.ajax_follow, name='ajax_follow'),
    path('post/<int:pk>/', views.PostPageView.as_view(), name='post'),
    path('post/tweet/', views.tweet, name='tweet'),
    path('post/<int:pk>/reply/', views.reply, name='reply'),
    path('post/like/', views.ajax_like, name='ajax_like'),
]
