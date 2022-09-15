import uuid
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    total_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='books')
    available_copies = models.IntegerField(name='available_copies')

    def __str__(self):
        return self.title

    @property
    def borrowers(self):
        query = self.borrower_set.all().values_list('student__id', flat=True)
        return query