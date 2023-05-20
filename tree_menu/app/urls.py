from django.urls import path

from .views import index  # , fill_data


urlpatterns = [
    # path('fill/', fill_data),
    path('<path:path>/', index),
]
