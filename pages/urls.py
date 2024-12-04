from django.urls import path

from .views import AboutUsView, HomePageView, UpdateServerView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('update-server/', UpdateServerView, name='update-server'),
]