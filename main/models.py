from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+"|"+str(self.id)



