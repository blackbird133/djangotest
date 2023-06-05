from _ast import Return
from datetime import datetime

from django.db import models
from django.db.models import CASCADE


class BooksModel(models.Model):
    isbn = models.CharField(max_length=255)
    bookTitle = models.CharField(max_length=50)
    bookCategory = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now())
    isAvailable = models.BooleanField(default=False)

    def __str__(self):
        return self.bookTitle
