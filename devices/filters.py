import django_filters
from .models import *


class ThinClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = ThinDevicesUnits
        fields = ['status', 'name']
