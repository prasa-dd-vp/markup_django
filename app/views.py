from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import re
# Create your views here.



def home(request):
    return render(request, 'app/index.html')

def bold(data):
    print("inside bold"+data)
    return re.sub(r'\*\*([_/a-zA-Z0-9\\__,.\s]+)\*\*',r'<b>\1</b>',data)

def italics(data):
    print("inside italics"+data)
    return re.sub(r'//([<a-z>]*)([a-zA-Z\_,.\s]+)([/<a-z>]*)//',r'<i>\1\2\3</i>',data)

def underline(data):
    print("inside underline"+data)
    return re.sub(r'__([<a-z>]*)([a-zA-Z\\__,.\s]+)([/<a-z>]*)__',r'<u>\1\2\3</u>',data)

def strike(data):
    print("inside underline"+data)
    return re.sub(r'\$\$([<a-z>]*)([a-zA-Z\\__,.\s]+)([/<a-z>]*)\$\$',r'<strike>\1\2\3</strike>',data)

def newline(data):
    print("inside newline"+data)
    return re.sub(r'([<a-z>]*)([a-zA-Z\\__,.\s]+)([/<a-z>]*)',r'\1\2\3<br>',data)



def process(request):
    if request.method == "POST":
        words = request.POST.get('words')
        result = words
        result = bold(result)
        print("after bold " +result)
        result = italics(result)
        print("after italics"+result)
        result = underline(result)
        print("after underline"+result)
        result = strike(result)
        print("after strike"+result)
        #result = newline(result)        
        return HttpResponse(result)
