from rest_framework import serializers
from .models import Product

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','date','user_name','location_suggestion','date_suggestion','time_suggestion')
        