from django.urls import path

from tariff.views import TariffViews, CategoryView

tariff_set = TariffViews.as_view({"get": "list"})
category = CategoryView.as_view({"get": "list"})

urlpatterns = [
    path("tariff/", tariff_set),
    path("tariff/category", category),
]