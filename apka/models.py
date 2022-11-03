from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 120 , blank = True)
    surname = models.CharField(max_length = 120 , blank = True)
    username = models.CharField(max_length = 120 , default = "Tomek")
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'to_user')

    def __str__(self):
        if self.name:
            return self.name + self.surname
        else:
            return self.username
