from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import delete

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/blog/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
