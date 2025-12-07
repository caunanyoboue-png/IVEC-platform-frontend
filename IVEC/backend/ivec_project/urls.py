from django.urls import path, include

urlpatterns = [
    path('api/users/', include('apps.users.urls')),
    path('api/investments/', include('apps.investments.urls')),
]