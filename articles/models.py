from django.db import models
from .positions import *
from pytz import timezone
from sorl.thumbnail import ImageField, get_thumbnail

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    position = models.IntegerField(choices=STATUS_CHOICES, default=1)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = ImageField(default='no_image.png',upload_to='thumbnails')

    @property
    def created_at_korean_time(self):   
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)
 
    # py manage.py makemigrations
    # py manage.py migrate , those both commands have to be accessed!

# Object -> Str form
    def __str__(self):
        return self.title

# Cut down long text
    def snippet(self):
        return self.body[:50] + '...'

# class About(models.model):
    