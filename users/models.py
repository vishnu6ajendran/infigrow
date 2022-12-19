from django.db import models
from django.contrib.auth.models import AbstractUser
class InfigrowUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"  # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

class Ledger(models.Model):
    name = models.CharField(max_length=10)
    recurrent_amount = models.IntegerField()
    date = models.DateField()
    amount = models.FloatField()
    status = models.SmallIntegerField(default=1)

