from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    rating = models.FloatField()

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} recommended by {self.user}'