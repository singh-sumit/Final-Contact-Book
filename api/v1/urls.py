from django.urls import path, include

urlpatterns = [
    # contact/
    path('', include('api.v1.contact.urls'))
]