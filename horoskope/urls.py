from . import views
from django.urls import path, include

#Число должно быть сначала потому что обработка сверху вниз идет
urlpatterns = [
    path('<int:sign_zodiac>/', views.all_signs_int),
    path('<str:sign_zodiac>/', views.all_signs),
    path('type/<str:elem>/', views.signs_from_elem),
    path('', views.horoscope_list),
]