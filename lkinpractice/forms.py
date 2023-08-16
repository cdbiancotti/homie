from django.forms import ModelForm
from lkinpractice.models import Lkin

class LkinForm(ModelForm):
    class Meta:
        model = Lkin
        fields = '__all__'