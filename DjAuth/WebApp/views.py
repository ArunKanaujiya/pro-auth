from django.shortcuts import render
from WebApp.models import Book
from WebApp.forms import StdForm
from django.views.generic import ListView
# Create your views here.

def BookView(request):
    form=StdForm(request.POST)
    
    return render(request,'myapp/home.html',{'form':form})
    
