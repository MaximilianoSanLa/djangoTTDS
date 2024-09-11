from django.contrib import admin
from django.urls import path,include
from dock.views import estadisticaView,listar_vuelo,registrar_vuelo
urlpatterns = [
    path('estadisticas/', estadisticaView.as_view(),name="estadistica"),
    path('listar/', listar_vuelo.as_view(),name='list'),
    path('registrar/', registrar_vuelo.as_view(),name='registrar'),
]
