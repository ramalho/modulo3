# coding: utf-8

from django.forms import ModelForm

from .models import Cliente

class ClienteModelForm(ModelForm):
    class Meta:
        model = Cliente

