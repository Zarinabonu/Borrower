from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('borrower/', include('app.api.borrower.urls'))
]