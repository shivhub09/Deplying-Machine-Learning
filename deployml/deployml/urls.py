from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('basicConcepts.urls')),
    path('', include('irisapp.urls')),
    path('admin/', admin.site.urls),
]
