from urllib import response
from django.shortcuts import render
from .serialization import *
from rest_framework import generics, viewsets, permissions, status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model()

class Register_view(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializations
    permission_classes = [AllowAny]  # Allow any user to access this view

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class Login_view(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "email": email,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#views for team memeber
class team_view(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamSerializer
  
class allTeam(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]

class create_team(generics.CreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamSerializer

class updateDeleteTeam(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamSerializer

#views for certificate
class certificate_view(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class allCertificate(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class create_certificate(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class updateDeleteCertificate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

#views for company info
class info_view(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class allInfo(generics.ListAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class create_info(generics.CreateAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class updateDeleteInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

#views for travel package
class package_view(viewsets.ModelViewSet):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer

class allPackage(generics.ListAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer

class create_package(generics.CreateAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer

class updateDeletePackage(generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer

#views for mountain expedition
class expedition_view(viewsets.ModelViewSet):
    queryset = MountainExpedition.objects.all()
    serializer_class = MountainExpedition

class allExpedition(generics.ListAPIView):
    queryset = MountainExpedition.objects.all()
    serializer_class = MountainExpedition

class create_expedition(generics.CreateAPIView):
    queryset = MountainExpedition.objects.all()
    serializer_class = MountainExpedition

class updateDeleteExpedition(generics.RetrieveUpdateDestroyAPIView):
    queryset = MountainExpedition.objects.all()
    serializer_class = MountainExpedition

#views for city tour
class ctour_view(viewsets.ModelViewSet):
    queryset = CityTour.objects.all()
    serializer_class = CityTourSerializer

class allCtour(generics.ListAPIView):
    queryset = CityTour.objects.all()
    serializer_class = CityTourSerializer

class create_ctour(generics.CreateAPIView):
    queryset = CityTour.objects.all()
    serializer_class = CityTourSerializer

class updateDeleteCtour(generics.RetrieveUpdateDestroyAPIView):
    queryset = CityTour.objects.all()
    serializer_class = CityTourSerializer

#views for customization option
class customize_view(viewsets.ModelViewSet):
    queryset = CustomizationOption.objects.all()
    serializer_class = CustomizationSerializer

class allCustomize(generics.ListAPIView):
    queryset = CustomizationOption.objects.all()
    serializer_class = CustomizationSerializer

class create_customize(generics.CreateAPIView):
    queryset = CustomizationOption.objects.all()
    serializer_class = CustomizationSerializer

class updateDeleteCustomize(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomizationOption.objects.all()
    serializer_class = CustomizationSerializer


#views for booking
class booking_view(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class allBooking(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class create_booking(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class updateDeleteBooking(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

#views for review
class review_view(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class allReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class create_review(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class updateDeleteReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


#views for faq
class faq_view(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class allFAQ(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class create_faq(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class updateDeleteFAQ(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

#views for contact
class contact_view(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer

class allContact(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer

class create_contact(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer

class updateDeleteContact(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer