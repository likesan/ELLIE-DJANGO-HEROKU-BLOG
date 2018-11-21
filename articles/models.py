from django.db import models
from pytz import timezone

# Create your models here. ( Capital letter is convention )
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
 
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