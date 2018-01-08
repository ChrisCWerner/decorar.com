from django.db import models

# Create your models here.
class Verse(models.Model):
    reference = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.reference