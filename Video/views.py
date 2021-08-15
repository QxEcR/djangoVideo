from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Video,Comment
from .forms import NewVideoForm
import random
import string

'''''''''''''''''
    a function to create uniqe slug for each video
'''''''''''''''''
def slug_generator(length):
    small = string.ascii_lowercase
    cap     = string.ascii_uppercase
    num     = string.digits
    slug = ""
    choices = ["small","cap","num"]
    while len(slug) != length:
        choice = random.choice(choices)
        if choice == "small":
            slug = slug + random.choice(small)
        elif choice == "cap":
            slug = slug + random.choice(cap)
        elif choice == "num":
            slug = slug + str(random.choice(num))
    return slug

# Create your views here.
'''''''''''''''''
    a view to to display specfic video and it's details
'''''''''''''''''
def watch_video_view(request,slug):   
    #get the video by the slug
    video = get_object_or_404(Video,slug=slug)

    #get the comments
    comments = Comment.objects.filter(video=video)
    
    if request.method == "POST":
        Comment.objects.create(video=video,comment=request.POST['comment'])
        
    context = {
        'video':video,
        'comments':comments,
    }
    return render(request,'video/watch.html',context)

     
'''''''''''''''''
    a view to post a new comment to a specfic video using ajax
'''''''''''''''''
def new_comment_view(request,vid):
    # get the video using id
    video = get_object_or_404(Video,id=vid)
    if request.is_ajax():
        # if the request is ajax get the comment and assign it to a variable
        comment = request.POST['comment']

        # create a new comment object
        Comment.objects.create(username=request.user,video=video,comment=comment)
        data = {
            'messege':'comment submited'
        }
        return JsonResponse(data)


'''''''''''''''''
    a view to upload a new video
'''''''''''''''''
def upload_video_view(request):  
    if request.method == "POST":
        # if the request = POST initilize the form with post and files
        form = NewVideoForm(request.POST or None, request.FILES or None)

        # get the title and the description
        title = request.POST['title']
        if len(title) > 40:
            return HttpResponse("max length of title is 40 letter")
        description = request.POST['description']

        # get new random slug using slug_generator
        slug = slug_generator(random.randint(20,30))
        
        # create a new video
        vid = Video(
            title=title,
            slug=slug,
            thumbnail=request.FILES['thumbnail'],
            description=description,
            video=request.FILES['video'],
        )
        vid.save()

                       
        return redirect('video:watch',slug)
    else:
        # if the request != POST assign the empty form
        form = NewVideoForm()

    context = {
        "form": form,
        "upload":True # for the template to know this an upload view
    }
    return render(request,'video/upload.html',context)


'''''''''''''''''
    a view to delete a video
'''''''''''''''''
def video_delete_view(request,slug):
    # get the video by slug
    video = get_object_or_404(Video,slug=slug)
    if request.method == "POST":
        # if the request = POST then delete the video    
        video.delete()

        return redirect('main:main')
    context={
        "video":video
    }
    return render(request,"video/delete.html",context)


