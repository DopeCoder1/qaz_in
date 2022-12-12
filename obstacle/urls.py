from django.urls import path

from obstacle.views import ObstacleViews, CategoryView

obstacle_set = ObstacleViews.as_view({"get": "list"})
category = CategoryView.as_view({"get": "list"})

urlpatterns = [
    path("obstacle/", obstacle_set),
    path("obstacle/category", category),
]