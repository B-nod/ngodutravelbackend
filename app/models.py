from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from tour.settings import base

User = base.AUTH_USER_MODEL

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='charging_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='charging_user_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
# model for team member   
class TeamMember(models.Model):
    CATEGORY_CHOICES = [
        ('board', 'Board of Directors'),
        ('executive', 'Executive Officer'),
        ('staff', 'Dedicated Staff'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="upload/team/", height_field=None, width_field=None, max_length=None, blank=True)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='staff')


    def __str__(self):
        return self.name

#model for certificate
class Certificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/certificates/", height_field=None, width_field=None, max_length=None, blank=True)
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='certificates')

    def __str__(self):
        return self.title

# model for company info
class CompanyInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    contact_email = models.EmailField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    website_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#model for destination
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# model for region
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    description = models.TextField(blank=True, help_text="Details about the region", null=True)

    def __str__(self):
        return self.name
    
# base model for every package
class BasePackage(models.Model):
    name = models.CharField(max_length=100,null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    duration = models.IntegerField(help_text='Duration in days', null=True)
    availability_start = models.DateField(null=True)
    availability_end = models.DateField(null=True)
    image = models.ImageField(upload_to="upload/package/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    max_altitude = models.DecimalField(max_digits=7, decimal_places=2, help_text="Maximum altitude in meters", blank=True, null=True)
    trip_grade = models.CharField(max_length=50, help_text="Difficulty level of the trip (e.g., Easy, Moderate, Hard)", blank=True, null=True)
    best_seasons = models.CharField(max_length=100, help_text="Best seasons for this trip (e.g., Spring, Autumn)", blank=True)
    group_size = models.IntegerField(help_text="Maximum group size", blank=True, null=True)
    includes = models.TextField(help_text="What is included in the package", blank=True)
    excludes = models.TextField(help_text="What is excluded from the package", blank=True)
    itinerary = models.TextField(help_text="Day-by-day itinerary for the trip", blank=True)
    notes = models.TextField(help_text="Additional notes about the package", blank=True)

    class Meta:
        abstract = True

#model for travel package
class TravelPackage(BasePackage):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="packages", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.region.name}) - Travel Package"

#model for mountain expedition   
class MountainExpedition(BasePackage):
    mountain_height = models.DecimalField(max_digits=7, decimal_places=2, help_text='Height in meters above sea level')

    def __str__(self):
        return f"{self.name} - Expedition at {self.mountain_height} meters"

#model for city tour
class CityTour(BasePackage):
    city_name = models.CharField(max_length=100)  # Name of the city for the tour
    

    def __str__(self):
        return f"{self.name} - City Tour"

# model for customization option
class CustomizationOption(models.Model):
    TRAVELING_OPTIONS = [
        ('single', 'Single'),
        ('group', 'Group'),
    ]
    
    TRAVEL_DATE_OPTIONS = [
        ('exact', 'Exact Date'),
        ('certain', 'Certain Date'),
        ('decide_later', 'Decide Later'),
    ]

    ACCOMMODATION_OPTIONS = [
        ('basic', 'Basic'),
        ('luxury', 'Luxury'),
        ('tents', 'Tents'),
        ('self_book', 'Self Book'),
    ]

    BUDGET_CHOICES = [
        ('on_budget', 'I\'m on a budget'),
        ('decide_later', 'I\'ll decide later'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    traveling_option = models.CharField(max_length=10, choices=TRAVELING_OPTIONS, blank=True, null=True)
    travel_date_option = models.CharField(max_length=15, choices=TRAVEL_DATE_OPTIONS, blank=True, null=True)
    travel_date = models.DateField(null=True, blank=True)  # For exact date
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True, blank=True)
    accommodation_preference = models.CharField(max_length=10, choices=ACCOMMODATION_OPTIONS, blank=True, null=True)
    budget_choice = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - Customization Request"
    
# model for booking 
class Booking(models.Model):
     # You can choose to have one of these fields, depending on your requirements
    tour_package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE, null=True, blank=True)
    mountain_expedition = models.ForeignKey(MountainExpedition, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    no_of_people = models.PositiveIntegerField(null=True)
    departure_date = models.DateField(null=True)
    arrival_date = models.DateField(null=True)
    message = models.TextField(blank=True)

    def __str__(self):
        if self.tour_package:
            return f"Booking for {self.tour_package.name} by {self.name}"
        elif self.mountain_expedition:
            return f"Booking for {self.mountain_expedition.name} by {self.name}"
        return f"Booking by {self.name}"


# model for review
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    image = models.ImageField(upload_to="uploads/reviews/", blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    review_text = models.TextField(null=True)


    def __str__(self):
        return f"{self.title} by {self.user.username} ({self.rating} stars)"

#model for faq
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)  # To order FAQs

    def __str__(self):
        return self.question
    
#model for contact us
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"