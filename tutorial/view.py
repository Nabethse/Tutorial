from django.http import HttpResponse
from django.views.generic import TemplateView
from .models.carrera import Carrera
from .vistas import formCarrera
from django.shortcuts import redirect 

def index(request):
    return HttpResponse("Hello word!")

class HomePageView(TemplateView):
    template_name= 'home.html' 
    models = Carrera
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["saludo"]= "hola de nuevo"
        context['arreglo']= self.models.objects.all()
        return context
    
class AboutPageView(TemplateView):
    template_name='about.html'


class CarreraCreateViewPage (TemplateView):
    template_name = "carrera_form.html"
    def get(Self,request, *args, **kwargs):
        form = formCarrera
        context = {'form':form}
        return Self.render_to_response(context)
    
def post(self, request, *arqs, **kwargs):
    form = formCarrera(request.POST)
    if form.is_valid():
        form.save()
        return redirect("lista_carrera")
    else:
        return self.render_to_response({'form':form})