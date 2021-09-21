from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import PCModel


class PCListCreateView(APIView):
    def get(self, *args, **kwargs):
        comps = PCModel.objects.all().values()
        return Response(comps, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        comp = PCModel.objects.create(**data)
        return Response(model_to_dict(comp), status.HTTP_201_CREATED)


class PCRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PCModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('PC with this id is not exist', status.HTTP_404_NOT_FOUND)
        comp = PCModel.objects.get(pk=pk)
        return Response(model_to_dict(comp), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PCModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('PC with this id is not exist', status.HTTP_404_NOT_FOUND)
        data = self.request.data.dict()
        PCModel.objects.filter(pk=pk).update(**data)
        return Response('updated', status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PCModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('PC with this id is not exist', status.HTTP_404_NOT_FOUND)
        comp = PCModel.objects.get(pk=pk)
        comp.delete()
        return Response(status.HTTP_204_NO_CONTENT)
