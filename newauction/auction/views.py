from django.shortcuts import redirect, render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Items
from django.urls import reverse
from datetime import datetime
from django.template import loader
import win32api

def index(request):
    return render(request,'index.html')
def addrecord(request):
    x = request.POST['uname']
    y = request.POST['psw']
    if x=="admin" and y=="admin":
        return render(request,'admin.html')
    else:
        username = request.POST['uname']
        mymembers = Items.objects.all().values()
        l=[]
        for x in mymembers:
            id=x['id']
            member = Items.objects.get(id=id)
            if member.status=="Active":
                l.append(member)

                
                
                
                
        template = loader.get_template('userpage.html')
        context = {
                'mymembers': l,
                'username':username,
        
        
                }
            


        
        
            
            

            


        
        return HttpResponse(template.render(context, request))

        #return render(request,'userpage.html')
        
def addingitem(request):
    return render(request,'addingitem.html')
def view(request):
    
    mymembers = Items.objects.all().values()
    for x in mymembers:
        id=x['id']
        member = Items.objects.get(id=id)
        current_time1=x['endtime']
        nn1=current_time1[0:2]
        nn=int(nn1)
        hh1=current_time1[3:5]
        hh=int(hh1)
        now = datetime.now()

        current_time = now.strftime("%H:%M")

        aa1=current_time[0:2]
        aa=int(aa1)
        bb1=current_time[3:5]
        bb=int(bb1)
        
        if nn-aa<0:
            status="Completed"
        elif nn==aa:
    
            if hh-bb<0:
                status="Completed"
            else:
                status="Active"
        else:
            status="Active"
        member.status=status
        member.save()
        
        
        



    
    mymembers = Items.objects.all().values()
    template = loader.get_template('view.html')
    context = {
        'mymembers': mymembers,
        
        
    }
    return HttpResponse(template.render(context, request))
def added(request):
       
    x = request.POST['itemname']
    y = request.POST['startprice']
    
    z = datetime.now().strftime('%H:%M')
    q=request.POST['etime']
    p = request.POST['status']
    
    uid=""
    member = Items(itemname=x,startprice=y,starttime=z,endtime=q,status=p,highprice=y,userid=uid)
    member.save()
    return HttpResponseRedirect(reverse('addingitem'))
def delete(request, id):
    member = Items.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('view'))
def update(request, id):
    mymember = Items.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
def updaterecord(request, id):
    x = request.POST['itemname']
    y = request.POST['startprice']
    
    z = request.POST['stime']
    current_time=request.POST['etime']
    p = request.POST['status']
    h=y
    uid=""
    
    

    
    











    member = Items.objects.get(id=id)
    member.itemname = x
    member.startprice = y
    member.starttime=z
    member.endtime=current_time

    member.status=p
    member.highprice=h
    member.save()
    return HttpResponseRedirect(reverse('view'))

def userpage(request):

            
    pass
def bid(request,id,username):
    mymembers = Items.objects.all().values()

    mymember = Items.objects.get(id=id)
    template = loader.get_template('bid.html')
    context = {
        'mymember': mymember,
        'username':username,
    }
    return HttpResponse(template.render(context, request))

def placebid(request,id,itemname,highprice,username):
    amt=request.POST['bid']
    amt=int(amt)
    if amt<=highprice:
        win32api.MessageBox(0, 'Amount must be high', 'title', 0x00001000)
    else:
         mymembers = Items.objects.all().values()
         member = Items.objects.get(itemname=itemname)
         member.highprice=amt
         member.userid=username
         member.save()
         mymembers = Items.objects.all().values()

         mymember = Items.objects.get(id=id)
         template = loader.get_template('bid.html')
         context = {
         'mymember': mymember,
         'username':username,
         }
         return HttpResponse(template.render(context, request))
         
    
         


