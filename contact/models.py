from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

def __str__(self):
    return 'Message from ' + self.name + ' _ ' + self.email