from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index),
    path('about/',about),
    path('contact/',contact),
    path('services/', services),
    path('properties/', properties),
    path('categories/',category_detail),
    path('property_details/<str:category>/',property_detail,name="property_detail"),
    path('card_details/<int:id>', detail_card),

    path('success/',success),
    path('sellproperty/',sellproperty)

]