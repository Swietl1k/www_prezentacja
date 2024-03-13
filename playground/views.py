from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Siteuser

def say_hello(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        return HttpResponse(f'Hello {user_input}, this is an exemplary site')
    else:
        return render(request, 'hello.html')



def say_hello2(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        return HttpResponse(f'Hello {user_input}, you reached the seccond site')
    else:
        return render(request, 'hello2.html')
    
def view_users(request):
    myusers = Siteuser.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))


def view_details(request, id):
    myuser = Siteuser.objects.get(id=id)
    template = loader.get_template('users_details.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse(template.render(context, request))


def view_testing(request):
    mydata = Siteuser.objects.all()
    mydata_alphabet = Siteuser.objects.all().order_by('firstname').values()
    template = loader.get_template('testing.html')
    context = {
        'myusers': mydata_alphabet,
    }
    return HttpResponse(template.render(context, request))