from django.db import models
# Create your models here.
class Video(models.Model):
    title           = models.CharField(max_length=40)

    slug            = models.CharField(max_length=30,default="",unique=True)

    video           = models.FileField(upload_to='video/')

    thumbnail       = models.ImageField(upload_to='thumbnail/')

    description     = models.TextField(null=True,blank=True)

    date_field      = models.DateField(auto_now_add=True)

    date_time_field = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def url(self):
        return self.slug

    #get_abslotue url
    def delete(self, *args, **kwargs):
        self.video.delete()
        self.thumbnail.delete()
        super().delete(*args, **kwargs)






class Comment(models.Model):
    video           = models.ForeignKey(Video,on_delete=models.CASCADE)

    comment         = models.TextField()

    date            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment