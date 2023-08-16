from django.shortcuts import redirect,render
from lkinpractice.forms import LkinForm
from lkinpractice.models import Lkin

# Create your views here.

from django.views.generic import TemplateView


class LkinView(TemplateView):
    template_name = "lkinpractice/lkin_practice.html"
    
    def get(self, request):
        lkins = Lkin.objects.all()
        form = LkinForm()
        return render(request, 'lkinpractice/lkin_practice.html', {'form': form, 'lkins': lkins})
    
    def post(self, request):
        form = LkinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lkin:lkin')
        lkins = Lkin.objects.all()
        return render(request, 'lkinpractice/lkin_practice.html', {'form': form, 'lkins': lkins})
        
        
    
