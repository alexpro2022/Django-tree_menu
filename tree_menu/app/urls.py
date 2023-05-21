from django.urls import path

from .views import index, draw_menu

urlpatterns = [
    path('', index),
    path('<path:path>/', draw_menu),
]
