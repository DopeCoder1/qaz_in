from django.urls import path

from onpf.views import OnpfViews, CategoryView

onpf_set = OnpfViews.as_view({"get": "list"})
category_set = CategoryView.as_view({"get": "list"})

urlpatterns = [
    path("onpf/", onpf_set, name="onpf"),
    path("onpf/category/", category_set),
]