from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import re

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def bold(data):
    #print("inside bold: "+data)
    return re.sub(r'\*\*((.|\n)*)\*\*',r'<b>\1</b>',data) #([\*\w\n\s.<>]*)

def italics(data):
    #print("inside italics"+data)
    return re.sub(r'//([<a-z>]*)([^http:](.|\n)*)([/<a-z>]*)//',r'<i>\1\2\3</i>',data)

def underline(data):
    #print("inside underline"+data)
    return re.sub(r'__([<a-z>]*)((.|\n)*)([/<a-z>]*)__',r'<u>\1\2\3</u>',data)

def strike(data):
    #print("inside underline"+data)
    return re.sub(r'\$\$([<a-z>]*)((.|\n)*)\$\$',r'<strike>\1\2\3</strike>',data)

def newline(data):
    return re.sub(r'(.*)\n',r'\1<br>\n',data)

def bullets(data):
    data = re.sub(r'(^(\ {0}\*{1}\s{1}(.)*\n)+(\ {0,}\*\ {1}(.)*\n)*)',r'<ul>\n\1</ul>\n',data, flags = re.M)
    for i in range(1,5):
        data = re.sub(r'(^(\ {'+str(i)+'}\*{1}\s{1}(.)*\n)+(\ {'+str(i)+',}\*\ {1}(.)*\n)*)',r'<ul>\n\1</ul></li>\n',data, flags = re.M)   
    print("outer ul:\n"+data)
    b = re.sub(r'^[\s]*\*{1}\s{1}((.|)*)(<[a-z>]*>)(\n<[a-z]*>)',r'<li>\1\n<ul>',data, flags = re.M)
    b = re.sub(r'^[\s]*\*{1}\s{1}((.|)*)(<[a-z>]*>)',r'<li>\1</li>',b, flags = re.M)
    return b


def numbers(data):
    data = re.sub(r'(^(\ {0}[0-9]+.{1}\ {1}(.)*\n)+(\ {0,}[0-9]+.{1}\ {1}(.)*\n)*)',r'<ol>\n\1</ol>\n',data, flags = re.M)
    for j in range(1,5):
        data = re.sub(r'(^(\ {'+str(j)+'}[0-9]+.{1}\s{1}(.)*\n)+(\ {'+str(j)+',}[0-9]+.{1}\ {1}(.)*\n)*)',r'<ol>\n\1</ol></li>\n',data, flags = re.M)
    print("after loop:\n"+ data)
    n = re.sub(r'^[\s]*[0-9]+.{1}\s{1}((.|)*)(<[a-z>]*>)(\n<[a-z]*>)',r'<li>\1\n<ol>',data, flags = re.M)
    n = re.sub(r'^[\s]*[0-9]+.{1}\s{1}((.|)*)(<[a-z>]*>)',r'<li>\1</li>',n, flags = re.M)
    return n
    
    
def link(data):
    return re.sub(r'\[(\w+)\]\(([\w:/.]+)\)',r'<a href= "\2">\1</a>',data)

def h1_header(data):
    return re.sub(r'^#{1}\s(.*)\n',r'<h1>\1</h1>',data, flags = re.M)

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
        result = h1_header(result)
        #result = h2_header(result)
        #result = h3_header(result)
        result = space(result)
        result = link(result)
        #print(result)
        return HttpResponse(result)
