from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
from registry.models import Links
from registry.serializers import LinksSerializer


class RegistryViews(viewsets.ModelViewSet):
    serializer_class = LinksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["link", "category__name"]
    ordering_fields = ["link", "category__name"]
    filterset_fields = {
        'link': ["in", "exact"],
        'category__name': ["in", "exact"],
    }

    def get_queryset(self):
        queryset = Links.objects.all()
        return queryset
