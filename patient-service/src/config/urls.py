from django.urls import path, include

urlpatterns = [
    path('', include('patients.urls')),
]
