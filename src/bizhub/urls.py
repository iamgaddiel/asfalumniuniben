from django.urls import path

from bizhub.forms import BusinessCreationForm
from .views import (
    BussinessListPage,
    BussinessCreation,
    SearchBusiness
)


app_name = "bizhub"


urlpatterns = [
    path('', BussinessListPage.as_view(), name="bizhub_list"),
    path('create/', BussinessCreation.as_view(), name="bizhub_form"),
    path('biz/search/', SearchBusiness.as_view(), name="bizhub_search")
]