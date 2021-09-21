from django.urls import path
from .views import PCListCreateView, PCRetrieveUpdateDeleteView

urlpatterns = [
    path('', PCListCreateView.as_view(), name='computer_list_create'),
    path('/<int:pk>', PCRetrieveUpdateDeleteView.as_view(), name='computer_retrieve_update_delete')
]
