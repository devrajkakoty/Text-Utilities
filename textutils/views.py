#Created
from typing import final
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def analyze(request):
    djtext = request.POST.get('text','default')
    rempunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capital','off')
    newlines = request.POST.get('newline','off')
    spaces = request.POST.get('space','off')
    params = {'purpose':[], "analyzed_text":''}
    if rempunc=="on":
        final_text=""
        for j in djtext:
            if j!=',' and j!='.':
                final_text+=j
        djtext=final_text
        params['purpose'].append("removed puncs")
    if capitalize=="on":
        final_text=djtext.upper()
        djtext=final_text
        params['purpose'].append("capitalized")
    if newlines=="on":
        final_text=""
        for j in djtext:
            if j!='\n' and j!='\r':
                final_text+=j
        djtext=final_text
        params['purpose'].append("newline removed")
    if spaces=="on":
        final_text=""
        prev=' '
        for j in djtext:
            if j!=' ' or (j==' ' and prev!=' '):
                final_text+=j
            prev=j
        djtext=final_text
        params['purpose'].append("spaces removed")

    if len(params['purpose'])>0:
        params['analyzed_text']=djtext
        params['purpose']=" and ".join(params['purpose'])
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("ERROR")
