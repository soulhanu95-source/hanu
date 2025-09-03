from django.shortcuts import render

# Create your views here.
def base1(request):
    return render(request,'base.html',)
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def extra(request):
    return render(request,'extra.html')
def project(request):
    return render(request,'projects.html')