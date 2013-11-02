# -*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    docfile = forms.FileField(
        label='Selecione Arquivo',
	help_text='max. 42 megabytes'
    )
