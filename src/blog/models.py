from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from uuid import uuid4


class Blog(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, unique=True)
    caption = RichTextField(help_text="Enter caption text for this blog")
    thumbnail_image = models.ImageField(default="blog.png", upload_to="blog_images/")
    content = RichTextField(help_text="this is the main writeup for this blog")
    timestamp = models.DateField(auto_now_add=timezone)


    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        from django.urls import reverse
        return reverse("core:blog:dashboard_blog_list")

    class Meta:
        ordering = ["-timestamp"]
