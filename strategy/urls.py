from django.urls import path

from strategy.views import StrategyViews, CategoryView

strategy_set = StrategyViews.as_view({"get": "list"})
category_set = CategoryView.as_view({"get": "list"})

urlpatterns = [
    path("strategy/", strategy_set, name="strategy"),
    path("strategy/category/", category_set),

]