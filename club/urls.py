from django.urls import path
from .views import *
urlpatterns = [
    path('', ClubChartView.as_view(), name="club_view")
]