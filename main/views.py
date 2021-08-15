from django.shortcuts import render
from Video.models import Video
# Create your views here.
def main(request):
    videos = Video.objects.all()
    
    context = {
        "videos":videos
    }
    return render(request, "main.html", context)