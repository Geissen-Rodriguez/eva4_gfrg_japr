from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def redireccion_login(request):
    return redirect('login')

class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'
