# This file was created by me and it was not given or not created by default
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):


    return render(request, "home.html")

def about(request):
    return HttpResponse("About this webpage")

def home(request):
    return HttpResponse("Welcome to the home page of the wedsite")

def removepunctuations(request):
    inputtext = request.POST.get('text','default')
    removepunctuations = request.POST.get('removepunctuations', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    # If user wants to remove punctuations from the text
    if removepunctuations == 'on':
        punctuations = '''!@#$%^&*()_+-={}[]|\:";'<>,.?/'''
        analyzed = ""

        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed + char

        user_text = {'Task' : 'Remove Punctuations', 'analyzed_text' : analyzed} 
        inputtext = analyzed

    # If user wants to capetalize the text 
    if(capitalize == 'on'):
        analyzed = ""
        for char in inputtext:
            analyzed = analyzed + char.upper()

        user_text = {'Task' : 'Capitalized Text', 'analyzed_text' : analyzed} 
        inputtext = analyzed  

    # IF user wants to remove spaces from the text
    if(spaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(inputtext):
            if not (inputtext[index] == " " and inputtext[index+1] == " "):
                analyzed = analyzed + char

        user_text = {'Task' : 'Space-removed Text', 'analyzed_text' : analyzed} 
        inputtext = analyzed  

    if(removepunctuations != "on" and capitalize != "on" and spaceremover != "on"):
        return HttpResponse("You have not selected any operations !!!") 

    return render(request, 'analyzed.html', user_text)                    

def spaceremover(request):
    return HttpResponse("spaceremover")

def capitalize(request):
    return HttpResponse("capitalize")                    