from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
         username = request.POST.get('name')
         my_user = User.objects.create_user(username)
         print(username)
         my_user.save()
         return render(request,'nextpage.html', {'user': username})
    return render(request, 'index.html')
def nextpage(request):
    return render(request, 'nextpage.html')