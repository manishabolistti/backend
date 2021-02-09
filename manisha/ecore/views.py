from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ecore.models import Marchent, Lenin, RFID
from ecore.serializers import MarchentSerializer, LeninSerializer, RFIDSerializer


class MarchentClass(generics.ListCreateAPIView):
    def get_queryset(self):
        return Marchent.objects.all()

    serializer_class = MarchentSerializer

class LeninClass(generics.ListCreateAPIView):
    def get_queryset(self):
        return Lenin.objects.all()

    serializer_class = LeninSerializer
class RFIDClass(generics.ListCreateAPIView):
    def get_queryset(self):
        return RFID.objects.all()

    serializer_class = RFIDSerializer

# update Data

class MarchentClass1(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        blogs=Marchent.objects.all()
        return blogs

    serializer_class = MarchentSerializer



@api_view(['GET', 'POST'])  #Marchent
def marchent_view(request):
    if request.method == 'GET':
        blogs = Marchent.objects.all()
        serializer = MarchentSerializer(blogs, many=True)
        return Response({
                'status': True,
                'message': 'Get request fulfilled!! ',
                'data': serializer.data
            })

    if request.method == 'POST':

        serializer = MarchentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Post request fulfilled!!',
                'data': serializer.data
            })
        else:
            return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    return Response({
            'status': False,
            'message': 'Invalid request',
            'data': ''
        })

@api_view(['GET', 'DELETE', 'PUT']) #MarchentUpdation
def marchentEdit(request, id):
    try:
        todo = Marchent.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MarchentSerializer(todo)
        return Response({
                'status': True,
                'message': 'Edit request fulfilled!!',
                'data': serializer.data
            })

    elif request.method == 'PUT':  # Update
        serializer = MarchentSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response({
                'staus': True,
                'message': 'Update request fulfilled!!',
                'data': serializer.data
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad request


    else:  # Delete
        todo.delete()
        return Response({
                'status': True,
                'message': 'Edit request fulfilled!!',
                'data': 'succesfully deleted'
            })




@api_view(['GET', 'POST'])  #Lenin
def lenin_view(request):
    if request.method == 'GET':
        blogs = Lenin.objects.all()
        serializer = LeninSerializer(blogs, many=True)
        return Response({
                'status': True,
                'message': 'Get request fulfilled!! ',
                'data': serializer.data
            })

    if request.method == 'POST':

        serializer = LeninSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Post request fulfilled!!',
                'data': serializer.data
            })
        else:
            return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    return Response({
            'status': False,
            'message': 'Invalid request',
            'data': ''
        })


@api_view(['GET', 'DELETE', 'PUT']) #LeninUpdation
def LeninEdit(request, id):
    try:
        todo = Lenin.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeninSerializer(todo)
        return Response({
                'status': True,
                'message': 'Edit request fulfilled!!',
                'data': serializer.data
            })

    elif request.method == 'PUT':  # Update
        serializer = LeninSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response({
                'staus': True,
                'message': 'Update request fulfilled!!',
                'data': serializer.data
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad request


    else:  # Delete
        todo.delete()
        return Response({
                'status': True,
                'message': 'Edit request fulfilled!!',
                'data': 'succesfully deleted'
            })




@api_view(['GET', 'POST'])
def Rfid_view(request):
    if request.method == 'GET':
        blogs = RFID.objects.all()
        serializer = RFIDSerializer(blogs, many=True)
        return Response({
                'status': True,
                'message': 'Get request fulfilled!! ',
                'data': serializer.data
            })

    if request.method == 'POST':

        serializer = RFIDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Post request fulfilled!!',
                'data': serializer.data
            })
        else:
            return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    return Response({
            'status': False,
            'message': 'Invalid request',
            'data': ''
        })


@api_view(['GET', 'DELETE', 'PUT']) #RFIDUpdation
def RfidEdit(request, id):
    try:
        todo = RFID.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RFIDSerializer(todo)
        return Response({
                'status': True,
                'message': 'Edit request fulfilled!!',
                'data': serializer.data
            })

    elif request.method == 'PUT':  # Update
        serializer = RFIDSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response({
                'staus': True,
                'message': 'Update request fulfilled!!',
                'data': serializer.data
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad request


    else:  # Delete
        todo.delete()
        return Response({
                'status': True,
                'message': 'Edit request fulfilled!!',
                'data': 'succesfully deleted'
            })

