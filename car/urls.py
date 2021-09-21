from django.urls import path
from .views import CarListCreateView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDeleteView.as_view(), name='car_retrieve_update_delete')
]
