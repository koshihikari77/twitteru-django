from .veiws import LikeToggleAPIView

urlpatterns = [
    #path('<int:pk>/follow/', views.ajax_follow, name='follow'),
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like'),
   ]
