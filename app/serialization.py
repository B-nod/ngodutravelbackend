from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializations(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username'),
            password=validated_data['password']
        )
        return user

# class RegisterSerializations(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password', 'username', 'phone', 'address')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data, *args, **kwargs):
#         # Pop the password from validated_data so it's not part of the user instance fields
#         password = validated_data.pop('password')  
        
#         # Create the user instance with the other fields
#         user = CustomUser(
#             email=validated_data['email'],
#             username=validated_data.get('username'),
#             phone=validated_data.get('phone'),
#             address=validated_data.get('address'),
#         )
        
#         # Hash the password before saving the user
#         user.password = make_password(password)
#         user.save()  # Save the user instance with the hashed password

#         return user

# serializer for team member
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"

# serializer for certificate
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"

# serializer for company info
class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = "__all__"


# serializer for company info
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"


# serializer for company info
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

# serializer for travel package
class TravelPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPackage
        fields = "__all__"

# serializer for mountain expedition
class MountainExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainExpedition
        fields = "__all__"

# serializer for city tour
class CityTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityTour
        fields = "__all__"

# serializer for customization option
class CustomizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizationOption
        fields = "__all__"


# serializer for booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

# serializer for review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

# serializer for FAQ
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"

# serializer for Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['email', 'name', 'phone', 'message']