from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter

from tower.views import NucList, PersonList, PlaceList, DetectedInformationViewset


router = DefaultRouter()
router.register(r'api', DetectedInformationViewset)


app_name = 'tower'

urlpatterns = [
    path('nucs/', NucList.as_view(), name='nuc_list'),
    path('persons/', PersonList.as_view(), name='person_list'),
    path('places/', PlaceList.as_view(), name='place_list'),
    path('', include(router.urls)),
]