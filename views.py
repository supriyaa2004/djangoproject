from django.shortcuts import render
from .forms import MyForm

def form(request):
    form= Myform()
    return render(request,"form.html",{'form':form})

# Create your views here.
