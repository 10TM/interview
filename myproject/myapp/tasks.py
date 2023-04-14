from celery import shared_task
from .models import MyModel

@shared_task
def delete_my_model(pk):
    MyModel.objects.get(pk=pk).delete()