from django.shortcuts import render
from .models import Member 

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'my_members': my_members,
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('myfirst.html')
  context = {
     'fruits': ['banana', 'abacate', 'maçã']
  }
  return HttpResponse(template.render(context, request))