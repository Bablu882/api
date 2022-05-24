from .models import Order
from rest_framework import serializers




class OrderCreationSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=20)
    order_status=serializers.HiddenField(default='PENDING')
    quantity=serializers.IntegerField()
    created_date=serializers.DateTimeField()
    updated_date=serializers.DateTimeField()


    class Meta:
        model=Order
        fields=['id','size','order_status','quantity','created_date','updated_date']


class OrderDetailsSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=20)
    order_status=serializers.CharField(default='PENDING')
    quantity=serializers.IntegerField()
    created_date=serializers.DateTimeField()
    updated_date=serializers.DateTimeField()


    class Meta:
        model=Order
        fields=['id','size','order_status','quantity','created_date','updated_date']
