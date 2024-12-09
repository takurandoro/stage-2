from django_filters import rest_framework as filters
from .models import *


class StudentFilter(filters.FilterSet):

    class Meta:
        model = Student
        fields = {
            "first_name": ["icontains", "istartswith", "iendswith"],
            "level": ["iexact"],
        }


class ResidentFilter(filters.FilterSet):

    class Meta:
        model = Resident
        fields = {
            "name": ["icontains", "istartswith", "iendswith"],
            "size": ["iexact", "gte"],
        }


class RoomFilter(filters.FilterSet):

    class Meta:
        model = Room
        fields = {
            "name": ["icontains", "istartswith", "iendswith"],
            "room_type": ["iexact"],
        }
