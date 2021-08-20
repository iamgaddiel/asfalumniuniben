from django.db import models

from core.models import Profile


class Bizhub(models.Model):
    INDUSTRY = [
        ("Law", "Law"),
        ("Software Development", "Software Development"),
        ("Health Care", "Health Care"),
        ("Accounting", "Accounting"),
        ("Engineering", "Engineering"),
        ("Ecommerce", "Ecommerce"),
        ("Design", "Design"),
        ("ICT", "ICT"),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=300, unique=True)
    business_sector = models.CharField(max_length=200, choices=INDUSTRY)
    description = models.TextField(help_text="Give a little description of your business", blank=True)
    location = models.TextField(blank=True)
    contact = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.business_name} owned by {self.owner.full_name}"

