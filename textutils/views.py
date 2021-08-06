# I have created this files -sabin
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = (request.POST.get('text', 'default'))

    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    charcount = (request.POST.get('charcount', 'off'))

    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
# aaaa
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
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

    elif (charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'Counting Character ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

