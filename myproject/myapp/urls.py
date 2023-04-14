from django.urls import path
from .views import MyModelList, MyModelDetail

urlpatterns = [
    path('mymodels/', MyModelList.as_view(), name='mymodel-list'),
    path('mymodels/<int:pk>/', MyModelDetail.as_view(), name='mymodel-detail'),
]
