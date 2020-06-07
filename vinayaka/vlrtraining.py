from django.http import HttpResponse
from django.shortcuts import render
import operator

def ram(request):
     return render(request,"countwords.html");

def count(request):
  mess=request.GET['message'];
  wl=mess.split();

  wlcount={};
  for word in wl:
      if word in wlcount:
               wlcount[word] +=1;
      else:
          wlcount[word]=1
  sort1=sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True);

  return render(request,"count.html",{"msg":mess,"length":len(wl),"abc":wlcount,"cba":sort1});

def aboutus(request):
    return render(request,"aboutus.html")
#def ram1(request):
   #return render(request,"ram.html",{"gopi":"03434343444"});


#def wel(request):
    #return HttpResponse("<h1>Hello Computer World</h1>");

#def kit(request):
   # return HttpResponse("<h1>Hello World</h1>");

#def ram2(request):
    #return render(request,"countwords.html");