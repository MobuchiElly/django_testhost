from django.http import HttpResponse
from django.template import loader
from .models import User, Member
from django.db.models import Q

def home(request):
    users = User.objects.all().values()
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def members(request):
    members = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': members 
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  print(context)
  return HttpResponse(template.render(context, request))


