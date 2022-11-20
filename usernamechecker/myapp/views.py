from django.shortcuts import render
from django.http import JsonResponse
from .models import Userdata

# Create your views here.
def home(request):
    return render(request,'myapp/index.html')

def check(request):
    if (request.method == "POST"):
        uname = request.POST.get('uname')
        avluname = Userdata.objects.filter(username=uname).exists()
        if avluname:
            status=0
        else:
            status=1
    return JsonResponse({'status':status})
