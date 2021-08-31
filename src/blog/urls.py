from django.urls import path
from .views import (
    BlogList,
    DashboardListView,
    CreateBlogView,
    UpdateBlogView,
    DeleteBlogView
)


app_name = "blog"

urlpatterns = [
    path('', BlogList.as_view(), name="blog_list"),
    path('dahboard/', DashboardListView.as_view(), name="dashboard_blog_list"),
    path('create/', CreateBlogView.as_view(), name="dashboard_blog_create"),
    path('view/<pk>/', UpdateBlogView.as_view(), name="dashboard_blog_update"),
    path('trash/<pk>/', DeleteBlogView.as_view(), name="dashboard_blog_delete"),
]