from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d.%m.%Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+'...'
