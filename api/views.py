from asyncio.log import logger
import logging
from ast import Return
from copy import error
from urllib import request
from api import serializers
from api.models import CheckBox
from api.serializers import CheckBoxSerializer, DataSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets, status, authentication, permissions, generics, mixins
from api.utils import Sum

logger = logging.getLogger('django')

class CheckBoxViewSet(viewsets.ModelViewSet):
    queryset = CheckBox.objects.all()
    serializer_class = CheckBoxSerializer
    @action(detail=False, methods=['get'])
    def limit(self, req, pk=None):
        try:
            params = req.query_params
        except Exception as error:
            logger.warning('params: %s', params)
        return Response({"result": params})

class CheckBoxList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = CheckBox.objects.all()
    serializer_class = CheckBoxSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
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

class DataView(APIView):
    @staticmethod
    def get(req):
        serializer = DataSerializer(data=req.query_params)
        serializer.is_valid(raise_exception=True)
        result = Sum(serializer.validated_data).call()
        return Response(result, status=200)



