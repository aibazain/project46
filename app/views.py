from django.shortcuts import render

# Create your views here.
def userfilter(request):

    d={'data':'HAI how Are YOU'}

    return render(request,'userfilter.html',d)