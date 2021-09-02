from typing import Any, Dict, Optional
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView, View, TemplateView, UpdateView, CreateView

from core.forms import ProfileCreationForm, UserCreationForm
from core.models import Profile
from blog.models import Blog


class Index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context  = super().get_context_data(**kwargs)
        context["blog_list"] = Blog.objects.all()[1:3]
        context["newest_blog"] = Blog.objects.first()
        return context

    
class Registration(CreateView):
    template_name = "core/register.html"
    form_class = UserCreationForm
    model = User

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, "You've successfully registered, login to continue")
        form.save()
        return redirect('core:login')

class KnowUsView(TemplateView):
    template_name = "core/knowus.html"

class ContactUsView(TemplateView):
    template_name = "core/contactus.html"

class RedirectToProfileUpdate(View):
    def get(self, request, *args, **kwargs):
        return redirect("core:fill_profile", pk=request.user.profile.pk)

# ================================= [ Profile ]==================================
class FillProfile(LoginRequiredMixin, UpdateView):
    form_class = ProfileCreationForm
    template_name = "core/profile_form.html"
    success_url = reverse_lazy("core:dashboard")
    model = Profile

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, "Your profile has been uploaded successfully")
        return super().form_valid(form)

class ViewProfile(LoginRequiredMixin, TemplateView):
    template_name = "core/profile.html"
    

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    form_class = ProfileCreationForm
    template_name = "core/profile_form.html"
    # success_url = reverse_lazy()

    def test_func(self) -> Optional[bool]:
        if self.request.user == self.kwargs.get("pk"):
            return True
        return False

class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "core/profile_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["this_user_pk"] = self.get_object().user.pk

        print(self.kwargs.get("pk"), "new")
        return context


# ================================= [ Dashboard ]==================================
class Dashboard(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "core/dashboard.html"
    ordering = ['-id']

    # def test_func(self) -> Optional[bool]:
    #     if self.request.user
    #     return super().test_func()
 

# ================================= [ Blog ]========================================
