from django.shortcuts import render

#def login(request):
   # return render(request,'mysite/login.html')

def index(request):
    return render(request,'mysite/index.html')

def about(request):
    return render(request,'mysite/about.html')

def img4(request):
    return render(request,'mysite/img4.html')

