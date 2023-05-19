from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('',getData),
    path('add/',addItem),
    path('details/<str:pk>/',getSingleData),
    path('update/<str:pk>/',updateItem),
    path('delete/<str:pk>/',deleteItem),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('about/',AboutData),
    path('services/',ServiceData),
    path('testimonial/',TestimonialData),
    path('task/',TaskData)
]
