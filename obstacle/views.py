from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
from obstacle.models import Category, ObstacleArticles
from obstacle.serializers import CategorySerializer, ObstacleArticlesSerializer


class ObstacleViews(viewsets.ModelViewSet):
    serializer_class = ObstacleArticlesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["id","title", "content", "tags__name", "tags__id","created_at", "category__id", "category__category_name"]
    ordering_fields = ["created_at", "tags__name", "category__category_name"]
    filterset_fields = {
        'id': ["in", "exact"],
        'title': ["in", "exact"],
        'tags__name': ["in", "exact"],
        'tags__id': ["in", "exact"],
        'created_at': ["in", "exact"],
        'category__id': ["in", "exact"],
        'category__category_name': ["in", "exact"],
    }

    def get_queryset(self):
        queryset = ObstacleArticles.objects.all()
        return queryset


class CategoryView(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)