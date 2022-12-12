from django.urls import path

from free_zone.views import FreeZoneViews, CategoryView

free_zone_set = FreeZoneViews.as_view({"get": "list"})
category = CategoryView.as_view({"get": "list"})

urlpatterns = [
    path("free_zone/", free_zone_set, name="free_zone"),
    path("free_zone/category", category, name="category"),
]