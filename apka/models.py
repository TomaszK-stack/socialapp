from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 120 , blank = True)
    surname = models.CharField(max_length = 120 , blank = True)
    username = models.CharField(max_length = 120 , default = "Tomek")
    user = models.OneToOneField(User , on_delete = models.CASCADE , related_name = 'to_user')

    def __str__(self):
        if self.name:
            return self.name + self.surname
        else:
            return self.username

    def get_absolute_url(self):
        return self.pk

class Friendship(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    friend = models.ForeignKey(Profile , related_name = "friends", on_delete = models.CASCADE)



class Invitation(models.Model):
    from_som = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = "from+")
    to_som = models.ForeignKey(Profile , on_delete = models.CASCADE, related_name = 'to')
    accepted = models.BooleanField(default = False)


    def __str__(self):
        return "Zaproszenie od " + str(self.from_som)

    def accept(self):
        self.accepted = True