from django.urls import path

from meeting.views import MeetingViews, CategoryView

meeting_set = MeetingViews.as_view({"get": "list"})
category = CategoryView.as_view({"get": "list"})

urlpatterns = [
    path("meeting/", meeting_set, name="meeting"),
    path("meeting/category", category, name="category"),
]