from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
from .tasks import delete_my_model

class MyModelList(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Выполнить задачу асинхронно
        delete_my_model.delay(instance.pk)

class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def perform_destroy(self, instance):
        # Выполнить задачу асинхронно
        delete_my_model.delay(instance.pk)
