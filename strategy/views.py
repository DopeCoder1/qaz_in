from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
from rest_framework.response import Response

from strategy.models import SubCategory, SubCategory2, StrategyArticles, Category
from strategy.serializers import SubCategorySerializer, SubCategorySerializer2, StrategyArticlesSerializer


class StrategyViews(viewsets.ModelViewSet):
    serializer_class = StrategyArticlesSerializer
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
        queryset = StrategyArticles.objects.all()
        return queryset


class CategoryView(viewsets.ViewSet):
    def list(self, request):
        queryset = SubCategory2.objects.all()
        serializer = SubCategorySerializer2(queryset, many=True)
        return Response(serializer.data)
