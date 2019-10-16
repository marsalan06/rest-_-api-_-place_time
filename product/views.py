from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import Productserializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@api_view(['GET','POST'])
def Product_list(request):
    if request.method == 'GET':
        obj= Product.objects.all()
        serializer=Productserializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])       
def product_detail(request,pk):
    try:
        obj= Product.objects.get(id= pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': #CREATED CONDITION
        serializer=Productserializer(obj)
        return Response(serializer.data)
    elif request.method=='PUT': #CREATED CONDITION
        serializer=Productserializer(obj,data=request.data) #REQUIRES OBJECT 
  # AND THE CHANGE 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

