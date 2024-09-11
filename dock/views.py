from django.shortcuts import render
from django.views import View
class estadisticaView(View):
    template_name='templates/estadistca_vuelos.html'
    def get(self,request):
        return render(request,self.template_name)
class listar_vuelo(View):
    template_name='templates/listar_vuelos.html'
    def get(self,request):
        return render(request,self.template_name)
class registrar_vuelo(View):
    template_name='templates/registrar_vuelos.html'
    def get(self,request):
        return render(request,self.template_name)