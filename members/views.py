from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    # return HttpResponse("Hello Django, this is from Mister Ainan!")
    template = loader.get_template('first.html')
    return HttpResponse(template.render())