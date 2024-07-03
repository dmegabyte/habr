from django.db import models
from django. contrib.auth .models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Room(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def comments(self):
        return Comment.objects.filter(room=self)
    @property
    def count_comments(self):
        return Comment.objects.filter(room=self).count()



    def __str__(self):
        return self.name+"|"+str(self.id)
    

class Comment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    text = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)+"|"+self.text



