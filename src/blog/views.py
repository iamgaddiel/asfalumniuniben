from typing import Any, Dict, List, Optional
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.urls import reverse

from blog.forms import BlogForm
from .models import Blog


class BlogList(ListView):
    model = Blog

# =============================== [ Admin ]=================================

class DashboardListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Blog
    template_name = "blog/blog_dashboard_list.html"

    def test_func(self) -> Optional[bool]:
        if self.request.user.is_superuser:
            return True
        return False

class CreateBlogView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "blog/blog_forms.html"
    form_class = BlogForm

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Blog created updated")
        return super().form_valid(form)

    def test_func(self) -> Optional[bool]:
        if self.request.user.is_superuser:
            return True
        return False

class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog/blog_forms.html"
    form_class = BlogForm

    def form_valid(self, form) -> HttpResponse:
        form.save()
        messages.success(self.request, "Blog successfull updated")
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_title"] = "View/Update Blog"
        return context
 
    def test_func(self) -> Optional[bool]:
        if self.request.user.is_superuser:
            return True
        return False

class DeleteBlogView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        blog = Blog.objects.get(pk=kwargs.get("pk"))
        messages.warning(self.request, f"{blog.title} has been deleted")
        blog.delete()
        return redirect("core:blog:dashboard_blog_list")

