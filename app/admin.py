from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'email',
        'username',
        'is_admin',
        'is_user' 
    )
    
    # Fields to search in the search box
    search_fields = ['email', 'username']
    list_per_page = 20

class TeamAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'name',
        'position',
        'bio',
        'image_display',
        'facebook_url',
        'instagram_url',
        'linkedin_url',
        'twitter_url',
        'category'
        
    )
    
    # Fields to search in the search box
    search_fields = ['name', 'position']
    list_per_page = 20

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 90px; height:120px; object-fit:cover;" />', obj.image.url)
        return "No Image"

    image_display.short_description = "Image"  # Display name in the admin
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TeamMember, TeamAdmin)
admin.site.register(Certificate)
admin.site.register(CompanyInfo)
admin.site.register(Destination)
admin.site.register(Region)
admin.site.register(TravelPackage)
admin.site.register(MountainExpedition)
admin.site.register(CityTour)
admin.site.register(CustomizationOption)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(FAQ)
admin.site.register(ContactUs)

