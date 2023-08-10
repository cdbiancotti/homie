from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Publicacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

@login_required
def pages(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/pages.html', {'publicaciones': publicaciones})

class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = "blog/page.html"

class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "blog/delete_page.html"
    success_url = "/pages"

class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = "blog/update_page.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user.username
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return f'/pages/{self.object.id}'

class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = "blog/update_page.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    
    def get_success_url(self) -> str:
        return f'/pages/{self.object.id}'
