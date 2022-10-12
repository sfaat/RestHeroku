from pyexpat import model
from rest_framework import serializers


from .models import *

class StudentSrializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"




