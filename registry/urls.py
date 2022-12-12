from django.urls import path

from registry.views import RegistryViews

registry_set = RegistryViews.as_view({"get": "list"})

urlpatterns = [
    path("registry/", registry_set),
]