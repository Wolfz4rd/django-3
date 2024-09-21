from django.urls import path
from .views import PostView

# urlpatterns = [
#     path("", post_list, name="post_list"),
# ]

urlpatterns = [
    path("", PostView.as_view(), name = "post")
]