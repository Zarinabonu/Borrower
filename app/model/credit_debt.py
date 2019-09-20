from django.db import models
from django.contrib.auth.models import User
from .borrower import Borrower, Operator


class Debt(models.Model):
    borrower = models.ForeignKey('Borrower', on_delete=models.CASCADE)
    sum = models.IntegerField()
    created = models.DateField()


class Debt_operator(models.Model):
    paid = models.ForeignKey('Debt', on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey('Operator', on_delete=models.SET_NULL, null=True)

