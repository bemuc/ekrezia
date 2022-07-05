import django_filters 
from django_filters import DateFilter, CharFilter

from .models import *

class amasakaFilter(django_filters.FilterSet):


    class Meta:
        model = amsakaramentu
        fields =  ['nomen','natus','domicilium']
        # exclude = ['status']