from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    # return HttpResponse("Hello Django, this is from Mister Ainan!")
    # template = loader.get_template('first.html')
    # return HttpResponse(template.render())
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))