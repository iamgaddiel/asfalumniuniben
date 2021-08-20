from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include
from .views import (
    Blogs,
    Index,
    Dashboard,
    FillProfile,
    Registration,
    UpdateView,
    ProfileDetail,
    RedirectToProfileUpdate
)

app_name = "core"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('dispatcher/', RedirectToProfileUpdate.as_view(), name="dispatcher"), 
    path('login/', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', Registration.as_view(), name="register"),
    path('blogs/', Blogs.as_view(), name="blogs"),
    path('profile/view/<pk>/', ProfileDetail.as_view(), name="profile_detail"),
    path('profile/form/<pk>/', FillProfile.as_view(), name="fill_profile"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('bizhub/', include("bizhub.urls")),
]

