from django.urls import path
from aplicativo import views

app_name = 'aplicativo'

urlpatterns = [
    path('', views.home, name='home'),
    path('calcular/', views.calcular, name='calcular'),
]

