from django.conf.urls import url
from rest_framework import routers as merouters
from .views import HistorialViewSet
merouters = merouters.DefaultRouter()
merouters.register(r'mongo', HistorialViewSet)
urlpatterns=[
]
urlpatterns+=merouters.urls