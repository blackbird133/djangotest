from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models


def validate_max_picks(value):
    if len(value) > 3:
        raise ValidationError("Maximum of 3 Picks")


class Borrow(models.Model):
    bookID = models.ManyToManyField('book.BooksModel', validators=[validate_max_picks])
    borrowBy = models.CharField(max_length=20, default="")
    borrowDate = models.DateTimeField(default=datetime.now())
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.borrowBy
