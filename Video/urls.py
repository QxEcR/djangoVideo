from django.urls import path
from . import views

app_name="video"

urlpatterns = [
    path('upload/',views.upload_video_view,name='upload'),
    path('watch=<slug>/',views.watch_video_view,name="watch"),
    path('<slug>/delete/',views.video_delete_view,name='video_delete'),
]
