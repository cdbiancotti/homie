from django.shortcuts import redirect,render
from lkinpractice.forms import LkinForm
from lkinpractice.models import Lkin, GenericProfile
from django.views.generic import View, TemplateView
from django.db.models import Q



class LkinView(View):
    
    def get(self, request):
        lkins = Lkin.objects.only('text_val')
        form = LkinForm()
        return render(request, 'lkinpractice/lkin_practice.html', {'form': form, 'lkins': lkins})
    
    def post(self, request):
        form = LkinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lkin:lkin')
        lkins = Lkin.objects.all()
        return render(request, 'lkinpractice/lkin_practice.html', {'form': form, 'lkins': lkins})
        
        
class LkinProfile(TemplateView):
    template_name = "lkinpractice/lkin_profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = GenericProfile.objects.filter(Q(lkin__user=self.request.user) | Q(lkinbusiness__user=self.request.user)
            )[0]
        return context
    
    
