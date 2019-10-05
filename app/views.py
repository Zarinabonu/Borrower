from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from app.model import Borrower


class BorrowerList(ListView):
    def get(self, request, *args, **kwargs):
        b = Borrower.objects.all()
        return render(request, 'administrator/borrower/create.html',{'borrower':b})


# Create your views here.
