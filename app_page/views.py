from django.shortcuts import render

# Create your views here.


def page1(request): 
    return render(request, 'index3.html')

def page2(request): 
    return render(request, 'index4.html')
