from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fn1(request):
    return render(request,'test.html')
def fn2(request):
    return render(request,'index.html')
def fn3(request):
    return render(request,'index2.html')    
def assignment1(request):
    return render(request,'assignment1.html')
def assignment2(request):
    return render(request,'assignment2.html')    
def assignment3(request):
    return render(request,'assignment3.html')    
def assignment4(request):
     return render(request,'assignment4.html')  
def assignment5(request):
    return render(request,'assignment5.html')
def assignment6(request):
    return render(request,'assignment6.html')
def fb(request):
    return render(request,'fb.html')
def bulb(request):
    return render(request,'bulb.html') 
def calculator(request):
    return render(request,'calc.html')       