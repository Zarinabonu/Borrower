from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Borrower

from rest_framework import serializers


class BorrowerSerialzier(ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Borrower
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone',
                  'image',
                  'work_place',
                  )

    def create(self, validated_data):
        b = Borrower(**validated_data)
        firstname = validated_data.pop('first_name')
        lastname = validated_data.pop('last_name')
        email = validated_data.pop('email')

        u = User.objects.create(last_name=lastname, first_name=firstname, email=email)

        b.user = u
        b.save()
        return b