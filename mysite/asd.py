from django.http import HttpResponse
from django.shortcuts import render

def ram(request):
    return render(request,"countwords.html")

def aboutus(request):
    return render(request,"aboutus.html")

def nagendra(request):
    return render(request,"nagendra.html")



def count(request):
    mess=request.GET['message']
    wl=mess.split()

    wlcount={}
    for word in wl:
        if word in wlcount:
            wlcount[word] +=1
        else:
            wlcount[word]=1
    sort1=sorted(wlcount.items(),reverse=True)

    return render(request,"count.html",{"msg":mess,"length":len(wl),"abc":wlcount,'cba':sort1})
