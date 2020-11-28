# I have created this files -sabin
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = (request.GET.get('text', 'default'))

    removepunc = (request.GET.get('removepunc', 'off'))
    fullcaps = (request.GET.get('fullcaps', 'off'))
    newlineremover = (request.GET.get('newlineremover', 'off'))
    extraspaceremover = (request.GET.get('extraspaceremover', 'off'))
    charcount = (request.GET.get('charcount', 'off'))

    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):

                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount == "on"):
        analyzed =len(djtext)
        params = {'purpose': 'Counting Character ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

#
# def capfirst(request):
#     return HttpResponse("capfirst")
#
#
# def newlineremove(request):
#     return HttpResponse("New line remove")
#
#
# def spaceremove(request):
#     return HttpResponse("Space Remove")
#
#
# def charcount(request):
#     return HttpResponse("character Count")
