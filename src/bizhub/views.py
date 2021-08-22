from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bizhub.forms import BusinessCreationForm

from bizhub.models import Bizhub


class BussinessListPage(ListView):
    model = Bizhub

class BussinessCreation(LoginRequiredMixin, CreateView):
    form_class = BusinessCreationForm
    template_name = "bizhub/bizhub_forms.html"

    def form_valid(self, form) -> HttpResponse:
        form.instance.owner = self.request.user.profile
        form.save()
        return resolve_url("core:bizhub:bizhub_list")
