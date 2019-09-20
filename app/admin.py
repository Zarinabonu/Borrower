from django.contrib import admin
from app.model import *

admin.site.register(Borrower)
admin.site.register(Operator)
admin.site.register(Paid)
admin.site.register(Paid_operator)
admin.site.register(Debt)
admin.site.register(Debt_operator)
# Register your models here.
