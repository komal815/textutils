#i have created this file komal
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse('hello')



def template(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    remove1=request.POST.get('removeanalyze','off')
    capital=request.POST.get('fullcapitalize','off')
    removespace=request.POST.get('removespace','off')
    countchar=request.POST.get('countchar','off')
    
    print(remove1)
    print(djtext)
    #analyzed=djtext
    analyzed=""
    final=""
    punc='''"+?><-*/':'''
    
    
    if remove1=='on':
        for i in djtext:
            if i not in punc:
                analyzed=analyzed+i
                
        params={'purpose':'removed punctuations','analyze_text':analyzed}
        
        djtext=analyzed
    if capital=='on':
        analyzed=djtext.upper()
        params={'purpose':'caps','analyze_text':analyzed}
        djtext=analyzed
    if removespace=='on':
        for index,i in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+i
            
        params={'purpose':'removespace','analyze_text':analyzed}   
    if (removespace!='on' and capital!='on' and remove1!='on'):
          return HttpResponse('error')
     
    return render(request,'analyze.html',params)        
        
    
    #return HttpResponse('removed')
    
    
def links(request):
    return render(request,'links.html')