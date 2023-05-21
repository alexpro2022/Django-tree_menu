from django.urls import path

from .views import draw_menu, index

urlpatterns = [
    path('', index),
    path('<path:path>/', draw_menu),
]
