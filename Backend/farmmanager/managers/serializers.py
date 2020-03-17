from rest_framework import serializers
from .models import Income

#Income Serialiser
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'