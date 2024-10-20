from django.urls import path
from .views import *

urlpatterns = [
    # url for use login and registration
    path('register/', Register_view.as_view(), name="register"),
    path('login/', Login_view.as_view(), name="login" ),

    # url for team member 
    path("teammember/", team_view.as_view({'get':'list'}), name="teammember"), 
    path("allTeam/", allTeam.as_view(), name="allTeam" ),
    path("c/", create_team.as_view(), name="createTeam"),
    path("singleTeam/<int:pk>/",updateDeleteTeam.as_view(), name="singleTeam"),
    path("updateDeleteTeam/<int:pk>/",updateDeleteTeam.as_view(), name="updateDeleteTeam"),

    # url for certificate
    path("certificate/", certificate_view.as_view({'get':'list'}), name="certificate"), 
    path("allCertificate/", allCertificate.as_view(), name="allCertificate" ),
    path("createCertificate/", create_certificate.as_view(), name="createCertificate"),
    path("singleCertificate/<int:pk>/",updateDeleteCertificate.as_view(), name="singleCertificate"),
    path("updateDeleteCertificate/<int:pk>/",updateDeleteCertificate.as_view(), name="updateDeleteCertificate"),


    # url for company_info 
    path("info/", team_view.as_view({'get':'list'}), name="info"), 
    path("allInfo/", allInfo.as_view(), name="allInfo" ),
    path("createInfo/", create_info.as_view(), name="createInfo"),
    path("singleInfo/<int:pk>/",updateDeleteInfo.as_view(), name="singleInfo"),
    path("updateDeleteInfo/<int:pk>/",updateDeleteInfo.as_view(), name="updateDeleteInfo"),

    # url for travel package 
    path("package/", package_view.as_view({'get':'list'}), name="package"), 
    path("allPackage/", allPackage.as_view(), name="allPackage" ),
    path("createPackage/", create_package.as_view(), name="createPackage"),
    path("singlePackage/<int:pk>/",updateDeletePackage.as_view(), name="singlePackage"),
    path("updateDeletePackage/<int:pk>/",updateDeletePackage.as_view(), name="updateDeletePackage"),

      # url for mountain expedition
    path("expedition/", expedition_view.as_view({'get':'list'}), name="expedition"), 
    path("allExpedition/", allExpedition.as_view(), name="allExpedition" ),
    path("createExpedition/", create_expedition.as_view(), name="createExpedition"),
    path("singleExpedition/<int:pk>/",updateDeleteExpedition.as_view(), name="singleExpedition"),
    path("updateDeleteExpedition/<int:pk>/",updateDeleteExpedition.as_view(), name="updateDeleteExpedition"),

      # url for city tour
    path("ctour/", ctour_view.as_view({'get':'list'}), name="ctour"), 
    path("allCtour/", allCtour.as_view(), name="allCtour" ),
    path("createCtour/", create_ctour.as_view(), name="createCtour"),
    path("singleCtour/<int:pk>/",updateDeleteCtour.as_view(), name="singleCtour"),
    path("updateDeleteCtour/<int:pk>/",updateDeleteCtour.as_view(), name="updateDeletePackage"),

    # url for customization option
    path("customize/", customize_view.as_view({'get':'list'}), name="customize"), 
    path("allCustomize/", allCustomize.as_view(), name="allCustomize" ),
    path("createCustomize/", create_customize.as_view(), name="createCustomize"),
    path("singleCustomize/<int:pk>/",updateDeleteCustomize.as_view(), name="singleCustomize"),
    path("updateDeleteCustomize/<int:pk>/",updateDeleteCustomize.as_view(), name="updateDeleteCustomize"),

    # url for booking 
    path("booking/", booking_view.as_view({'get':'list'}), name="booking"), 
    path("allBooking/", allBooking.as_view(), name="allBooking" ),
    path("createBooking/", create_booking.as_view(), name="createBooking"),
    path("singleBooking/<int:pk>/",updateDeleteBooking.as_view(), name="singleBooking"),
    path("updateDeleteBooking/<int:pk>/",updateDeleteBooking.as_view(), name="updateDeleteBooking"),

    # url for review
    path("review/", review_view.as_view({'get':'list'}), name="review"), 
    path("allReview/", allReview.as_view(), name="allReview" ),
    path("createReview/", create_review.as_view(), name="createReview"),
    path("singleReview/<int:pk>/",updateDeleteReview.as_view(), name="singleReview"),
    path("updateDeleteReview/<int:pk>/",updateDeleteReview.as_view(), name="updateDeleteReview"),

     # url for faq
    path("faq/", faq_view.as_view({'get':'list'}), name="faq"), 
    path("allFAQ/", allFAQ.as_view(), name="allFAQ" ),
    path("createFAQ/", create_faq.as_view(), name="createFAQ"),
    path("singleFAQ/<int:pk>/",updateDeleteFAQ.as_view(), name="singleFAQ"),
    path("updateDeleteFAQ/<int:pk>/",updateDeleteFAQ.as_view(), name="updateDeleteFAQ"),

        # url for faq
    path("contact/", contact_view.as_view({'get':'list'}), name="contact"), 
    path("allContact/", allContact.as_view(), name="allContact" ),
    path("createContact/", create_contact.as_view(), name="createContact"),
    path("singleContact/<int:pk>/",updateDeleteContact.as_view(), name="singleContact"),
    path("updateDeleteContact/<int:pk>/",updateDeleteContact.as_view(), name="updateDeleteContact"),
]
