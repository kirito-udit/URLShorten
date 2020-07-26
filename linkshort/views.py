from django.shortcuts import render
import pyshorteners
# Create your views here.
def short(request):
    return render(request, 'home.html', )

def shorten(request):
 a = request.GET["link"]
 s=pyshorteners.Shortener()
 x=s.tinyurl.short(a)
 return render(request, 'result.html', {'result':x})