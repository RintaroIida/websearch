from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    intro = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='media')
    posted_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    book = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    


    