from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)  # max=255
    text = models.TextField()  # more then 255
    date = models.DateTimeField(default=timezone.now)  # (auto_now_add=True) - time now. Cant change
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # wen user deleted, article is delete

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
