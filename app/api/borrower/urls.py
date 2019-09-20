from django.contrib import admin
from django.urls import path, include

from app.api.borrower import views

urlpatterns = [
    path('create/', views.Borrower_createAPIView.as_view(), name='api-borrower-create')
]