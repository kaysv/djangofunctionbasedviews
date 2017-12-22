from django.db import models
from django.urls import reverse


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# Generic Editing views ko laagi model

class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('GenericEditingView', kwargs={'pk': self.pk})
