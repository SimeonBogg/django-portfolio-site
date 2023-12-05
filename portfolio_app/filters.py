import django_filters
from django_filters import CharFilter

from django import forms

from .models import *

class PostFilter(django_filters.FilterSet):
    heading = CharFilter(field_name='heading', lookup_expr="icontains", label='Search by Heading:')
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Search by Tags:'
    )

    class Meta:
        model = Post
        fields = ['heading', 'tags']