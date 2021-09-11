from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    return HttpResponse('removepuch')

def analyze(request):
    # getting the text value through url with the help of (get request method)
    gettext = request.POST.get('text', 'default')

    # for checkbox
    removepunch = request.POST.get('removepunch', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newline = request.POST.get('newline', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(gettext)
    print(removepunch)

    if removepunch == "on":
        # punctuation marks to remove into the text
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        # to store the removed punctuation
        analyze = ""
    
        # removing punctuation with the help of loop 
        for char in gettext:
            if char not in punctuations:
                analyze = analyze + char

        # creating a params disctionary
        params = {'purpose' : 'Removed Punctuation', 'analyze_text' : analyze}
        gettext = analyze
        # passsing the parameters into html templates through arguments
        # return render(request, 'analyze.html', params)

    # converting characters into capital letter     
    if capitalize == 'on':
        analyze = ""
        for char in gettext:
            analyze = analyze + char.upper()
        params = {'purpose' : 'Capitalize The Characters', 'analyze_text' : analyze}
        gettext = analyze
        # return render(request, 'analyze.html', params)

    # removing new lines from the characters
    if newline == 'on':
        analyze = ""
        for char in gettext:
            if char != '\n' and char != '\r':
                analyze = analyze + char
        params = {'purpose' : 'Remove New Lines', 'analyze_text' : analyze}
        gettext = analyze
        # return render(request, 'analyze.html', params)

    # removing extra spaces from characters 
    if spaceremover == 'on':
        analyze = ""
        for index, char in enumerate(gettext):
            if gettext[index] == " " and gettext[index + 1] == " ":
                pass
            else:
                analyze = analyze + char
        params = {'purpose' : 'Removed Extra spaces', 'analyze_text' : analyze}
        gettext = analyze
        # return render(request, 'analyze.html', params)

    # count the number of characters in a string
    if charcount == 'on':
        analyze = ""
        analyze = len(gettext)
        params = {'purpose' : 'Count the number of characters', 'analyze_text' : analyze}
        gettext = analyze
       
    # if you dont check any box it will show this error
    if charcount != 'on' and spaceremover != 'on' and newline != 'on' and capitalize != 'on' and removepunch != "on":
        return HttpResponse("Please chose options")
     
    return render(request, 'analyze.html', params)
        

