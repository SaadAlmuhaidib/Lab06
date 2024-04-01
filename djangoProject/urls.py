# project_name/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saad_app/', include('Saad_app.urls')),  # Include the Saad_app URLs here
]
