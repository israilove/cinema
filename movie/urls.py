from django.urls import include, path

urlpatterns = [
    # ... другие URL-адреса вашего проекта ...
    path('cinema/', include('cinema.urls')),
]
