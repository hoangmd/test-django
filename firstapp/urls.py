from django.urls import path

from .views import index

urlpatterns = [
    path('<int:run>', index, name='index')
]
