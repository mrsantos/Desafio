# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from handleFile import handle_uploaded_file
from forms import UploadFileForm

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'])

            return HttpResponseRedirect('', {'form': form})
    else:
        form = UploadFileForm()

    return render_to_response('index.html', {'form': form})
