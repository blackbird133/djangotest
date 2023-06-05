from datetime import datetime

from django.db import models
from django.db.models import CASCADE


class ReturnedBook(models.Model):
    # STATUSES = [("yes", "Yes"), ("no", "No")]
    borrowID = models.ForeignKey('borrow.Borrow', on_delete=CASCADE)
    returnDate = models.DateTimeField(default=datetime.now())
    # isLate = models.CharField(choices=STATUSES, max_length=10, blank=False)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)