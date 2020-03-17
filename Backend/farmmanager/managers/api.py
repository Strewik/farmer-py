from .models import Income 
from rest_framework import viewsets, permissions
from .serializers import IncomeSerializer

#Inome Viewset
class IncomeViewset(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = IncomeSerializer