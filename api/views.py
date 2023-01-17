from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from base.models import Item
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleData(request, pk):
    item = Item.objects.get(id = pk)
    serializer = ItemSerializer(item,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateItem(request, pk):
    item = Item.objects.get(id = pk)
    serializer = ItemSerializer(instance= item,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request, pk):
    item = Item.objects.get(id = pk)
    item.delete()
    return Response('item succesfully deleted')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AboutData(request):
    data = About.objects.all()
    serializer = AboutSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ServiceData(request):
    data = Service.objects.all()
    serializer = ServiceSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TestimonialData(request):
    data = Testimonial.objects.all()
    serializer = TestimonialSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskData(request):
    data = Task.objects.all()
    serializer = TaskSerializer(data, many=True)
    return Response(serializer.data)