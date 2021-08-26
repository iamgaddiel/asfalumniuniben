from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
import uuid


class Profile(models.Model):
    TITLE = [
        ('Professor', 'Professor'),
        ('Doctor', 'Doctor'),
        ('Pharm Doctor', 'Pharm Doctor'),
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Rev', 'Rev'),
    ]
    DAYS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    ]

    MONTHS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]

    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default="user.svg", upload_to="%y%m%d")
    full_name = models.CharField(max_length=300)
    title = models.CharField(max_length=12, choices=TITLE, blank=True)
    year_of_graduation = models.CharField(max_length=6, blank=True)
    phone_number = models.CharField(max_length=15, default="")
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=10, help_text="If Nigeria is chosen", blank=True)
    day_of_birth = models.CharField(max_length=2, blank=True, choices=DAYS)
    month_of_birth = models.CharField(max_length=2, blank=True, choices=MONTHS)
    profession = models.CharField(max_length=20, blank=True)
    ministry_group = models.CharField(max_length=30, help_text="enter ministry group joined, if you joined any", blank=True)
    updated = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username} profile"

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="blog_images %Y%M%d", default="blog_image.png")
    content = models.TextField()
    date = models.DateField(auto_now=timezone.now)

    def __str__(self) -> str:
        return self.title

