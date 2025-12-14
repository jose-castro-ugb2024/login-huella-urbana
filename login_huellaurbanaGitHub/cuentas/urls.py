from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='inicio'),  # Raíz va al login
    path('login/', views.login_usuario, name='login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('pagina/<int:pk>/', views.pagina_detalle, name='pagina_detalle')
]
