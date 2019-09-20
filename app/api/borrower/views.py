from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.borrower.serializers import BorrowerSerialzier
from app.model import Borrower


class Borrower_createAPIView(CreateAPIView):
    serializer_class = BorrowerSerialzier
    queryset = Borrower.objects.all()