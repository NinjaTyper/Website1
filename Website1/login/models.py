from django.db import models
from unicodedata import name

# Create your models here.
class AccountLevel(models.Model):
    chatspeed = models.IntegerField(default=5)


class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    accountLvl = models.ForeignKey(AccountLevel, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return "Username = " + self.username + ", Password = " + self.password + ", Account Level = " + str(self.accountLvl)
    
