from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_user = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.username}: {self.message}'