from django.urls import path, include

urlpatterns = [
    # api/v1
    path('v1/', include('api.v1.urls')),
]