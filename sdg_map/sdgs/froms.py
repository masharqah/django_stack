from django.forms import ModelForm
from .models import Point


class PartnerForm(ModelForm):
    class Meta:
        model = Point
        fields='__all__'
        