from django.db import models
from django.contrib.auth.models import User


class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    work_place = models.TextField(null=True, blank=True)


class Operator(models.Model):
    borrower = models.OneToOneField('Borrower', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

