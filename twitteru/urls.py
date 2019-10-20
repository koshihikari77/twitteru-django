from django.urls import path

from . import views


app_name = 'twitteru'

urlpatterns = [
    path('home/', views.user_home, name='home'),
    path('user/<int:pk>/', views.UserPageView.as_view(), name='userpage'),
    path('user/<int:pk>/follow/', views.follow, name='follow'),
    path('post/<int:pk>/', views.PostPageView.as_view(), name='post'),
    path('like/', views.ajax_like, name='ajax_like'),
]
