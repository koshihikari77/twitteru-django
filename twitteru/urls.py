from django.urls import path

from . import views


app_name = 'twitteru'

urlpatterns = [
    path('user/<int:pk>/', views.UserPageView.as_view(), name='userpage'),
    path('post/<int:pk>/', views.PostPageView.as_view(), name='post'),
    path('post/<int:pk>/like/', views.ajax_like, name='like')
]
