from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todo.serializer import ProductSerializer
from todo.models import Product

# Create your views here.


@api_view(['POST'])
def createtodo(request):
    record = ProductSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)


@api_view(['GET'])
def alltodo(request):
    record= Product.objects.all()
    record = ProductSerializer(record, many=True)
    return Response(record.data)


@api_view(['DELETE'])
def deletetodo(request, id):
    record= Product.objects.get(id=id)
    record.delete()
    return Response('todo deleted successfully')

@api_view(['GET'])
def tododetail(request, id):
    record= Product.objects.get(id=id)
    info= ProductSerializer(record, many=False)
    return Response(info.data)

@api_view(['PUT'])
def todoedit(request, id):
    record= Product.objects.get(id=id)
    info = ProductSerializer(data=request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('Updated Successfully')
    
    
    
    
def index(request):
    url = request.get('http://localhost:8000/api/v1/alltodo')
    data = url.json()
    context= {'data': data}
    return render(request, 'api/index.html', context)

    

    
