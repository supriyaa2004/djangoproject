from django.shortcuts import render

def child1_view(request):
    return render(request, 'child1.html')

def child2_view(request):
    return render(request, 'child2.html')
