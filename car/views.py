from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import CarModel


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all().values()
        return Response(cars, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        car = CarModel.objects.create(**data)
        return Response(model_to_dict(car), status.HTTP_201_CREATED)


class CarRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exist', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        return Response(model_to_dict(car), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exist', status.HTTP_404_NOT_FOUND)
        data = self.request.data.dict()
        CarModel.objects.filter(pk=pk).update(**data)
        return Response('updated', status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exist', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status.HTTP_204_NO_CONTENT)
