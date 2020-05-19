from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request , 'home.html')

def countpage(request):
    text  = request.GET['fulltext']
    wordlist =  text.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    sortedwords = sorted(worddic.items(), key=operator.itemgetter(1),reverse = True)
    return render(request , 'count.html', {'yourtext':text , 'count':len(wordlist) , 'sortedwords': sortedwords})

def about(request):
    return render(request , 'about.html')
