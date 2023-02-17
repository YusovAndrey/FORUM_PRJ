#from django.shortcuts import render
from copy import error
from rest_framework import viewsets
from api.models import CheckBox
from api.serializers import CheckBoxSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


#class CheckBoxViewSet(viewsets.ModelViewSet):
#    queryset = CheckBox.objects.all()
#    serializer_class = CheckBoxSerializer

@api_view(['GET'])
def CheckBox_list(req):
    checkboxes = CheckBox.objects.all()
    serializer = CheckBoxSerializer(checkboxes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CheckBox_detail(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)
        serializer = CheckBoxSerializer(checkbox)
    except CheckBox.DoesNotExist:
        return Response({"error": f'CheckBox with id={pk} is not found'}, status=404)
    return Response(serializer.data)

@api_view(['POST'])
def CheckBox_create(req):
    serializer = CheckBoxSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=201)

@api_view(['PUT'])
def CheckBox_update(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)
        serializer = CheckBoxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except CheckBox.DoesNotExist:
        return Response({"error": f'CheckBox with id={pk} is not found'}, status=404)
    return Response(serializer.data)
    
@api_view(['DELETE'])
def CheckBox_delete(req, pk):
    checkbox = CheckBox.objects.get(id=pk)
    checkbox.delete()
    return Response(status=204)


