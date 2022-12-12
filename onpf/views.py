from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
from rest_framework.response import Response

from onpf.models import SubCategory, SubCategory2, OnpfArticles, Category
from onpf.serializers import SubCategorySerializer, SubCategorySerializer2, OnpfArticlesSerializer


class OnpfViews(viewsets.ModelViewSet):
    serializer_class = OnpfArticlesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["id", "title", "content", "tags__name", "subcategory3__subcategory_name2"]
    ordering_fields = ["id", "created_at", "content", "title"]
    filterset_fields = {
        'id': ["in", "exact"],
        'title': ["in", "exact"],
        'content': ["in", "exact"],
        'created_at': ["in", "exact"],
        'tags__name': ["in", "exact"],
        'subcategory3__subcategory_name2': ["in", "exact"],
    }

    def get_queryset(self):
        queryset = OnpfArticles.objects.all()
        return queryset


class CategoryView(viewsets.ViewSet):
    def list(self, request):
        queryset = SubCategory2.objects.all()
        serializer = SubCategorySerializer2(queryset, many=True)
        return Response(serializer.data)
