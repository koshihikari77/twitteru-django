from django.urls import path

from . import views


app_name = 'twitteru'

urlpatterns = [
    path('home/', views.user_home, name='home'),
    path('user/<int:pk>/', views.UserPageView.as_view(), name='userpage'),
    path('user/follow/', views.ajax_follow, name='ajax_follow'),
    path('post/<int:pk>/', views.PostPageView.as_view(), name='post'),
    path('post/like/', views.ajax_like, name='ajax_like'),
]
