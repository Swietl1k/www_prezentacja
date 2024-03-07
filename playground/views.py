from django.shortcuts import render
from django.http import HttpResponse

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
