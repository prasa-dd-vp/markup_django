from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import re

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def bold(data):
    #print("inside bold: "+data)
    return re.sub(r'\*\*([\*\w\n\s.<>]*)\*\*',r'<b>\1</b>',data) #([\*\w\n\s.<>]*)

def italics(data):
    #print("inside italics"+data)
    return re.sub(r'//([<a-z>]*)([^http:][<>/\w\n]*)([/<a-z>]*)//',r'<i>\1\2\3</i>',data)

def underline(data):
    #print("inside underline"+data)
    return re.sub(r'__([<a-z>]*)(.*[\w\n]*)([/<a-z>]*)__',r'<u>\1\2\3</u>',data)

def strike(data):
    #print("inside underline"+data)
    return re.sub(r'\$\$([<a-z>]*)(.*[\w\n]*)([/<a-z>]*)\$\$',r'<strike>\1\2\3</strike>',data)

def newline(data):
    return re.sub(r'([^>{1}])\n',r'\1<br>\n',data)

def bullets(data):
    b = re.sub(r'^[^a-zA-Z0-9]*((\*\s.*[\w<>]+\n)+)',r'<ul>\n\1</ul>\n',data, flags = re.M)
    b = re.sub(r'^\*\s((.*[\w<>]+\n))',r'<li>\1</li>',b, flags = re.M)
    return b

def numbers(data):
    n = re.sub(r'^[^a-zA-Z0-9]*(([0-9]+.{1}\s{1}.*[\w<>]+\n)+)',r'<ol>\n\1</ol>\n',data, flags = re.M)   
    n = re.sub(r'^[0-9]+.\s{1}((.*[\w<>]+\n))',r'<li>\1</li>',n, flags = re.M)
    return n

def link(data):
    return re.sub(r'\[(\w+)\]\(([\w:/.]+)\)',r'<a href= "\2">\1</a>',data)

def h1_header(data):
    return re.sub(r'[^#](#{1})\s(.*)\n',r'<h1>\2</h1>',data)

def h2_header(data):
    return re.sub(r'(#{2})\s(.*)\n',r'<h2>\2</h2>',data)

def h3_header(data):
    return re.sub(r'(#{3})\s(.*)\n',r'<h3>\2</h3>',data)

def space(data):
    return data.replace(" ", "&nbsp;")


def process(request):
    if request.method == "POST":
        words = request.POST.get('words')
        result = words
        result = bold(result)
        #print("after bold " +result)
        result = italics(result)
        #print("after italics"+result)
        result = underline(result)
        #print("after underline"+result)
        result = strike(result)
        #print("after strike"+result)
        result = newline(result)
        result = bullets(result)
        result = numbers(result)   
        #result = h1_header(result)
        #result = h2_header(result)
        #result = h3_header(result)
        result = space(result)
        result = link(result)
        print(result)
        return HttpResponse(result)
