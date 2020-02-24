from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


class Student(models.Model):
    """Model representing a book name."""
    name = models.CharField(max_length=200, help_text='Enter your name')
    perm_number = models.CharField(max_length=200, help_text='Enter your perm number')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} ({self.perm_number})'