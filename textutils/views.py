# Created by me--Ashish
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def nav(request):
    return HttpResponse('''<h1><center> Navigation Bar </center></h1><br> <a href="www.facebook.com">facebook</a><br><a href="www.google.com">google</a><br><a href="www.github.com">Github</a><br>''')

def index(request):
    now =datetime.datetime.now()
    params={'d':now}
    return render(request,'index.html',params)
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #check the checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    # Check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed extra spaace', 'analyzed_text': analyzed}
        djtext=analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)
        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

