from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import MasterSerializers, ServicesSerializers, RequestSerializer
from .models import Master, Request, Services
from rest_framework.response import Response

# Create your views here.


class MasterAPIView(generics.ListCreateAPIView):
    serializer_class = MasterSerializers
    queryset = Master.objects.all()

    def post(self, request):
        request_body = request.data
        srz = MasterSerializers(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)


class MasterRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Master.objects.get(id=pk)
        except Master.DoesNotExist:
            return Response({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = MasterSerializers(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Master.objects.get(id=pk)
        except Master.DoesNotExist:
            return JsonResponse({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ServiceAPIView(generics.ListAPIView):
    serializer_class = ServicesSerializers
    queryset = Services.objects.all()

    def post(self, request):
        request_body = request.data
        srz = ServicesSerializers(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = Services.objects.get(id=pk)
        except Services.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = ServiceSerializers(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Services.objects.get(id=pk)
        except Services.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RequestAPIView(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def post(self, request):
        request_body = request.data
        srz = RequestSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = Request.objects.get(id=pk)
        except Request.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = RequestSerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Request.objects.get(id=pk)
        except Request.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)