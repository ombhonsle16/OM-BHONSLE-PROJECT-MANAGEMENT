from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,"home/index.html")

def contactUs(request):
    return render(request,"home\contactus.html")

def contactSubmit(request):
    
    email = request.POST.get("email")
    
    if email is None:
        return contactUs(request)
    
    name = request.POST.get("name")
    tel = request.POST.get("phone")
    desc = request.POST.get("desc")
    
    try:
        if len(tel)!=10: raise Exception
        int(tel)
    except:
        messages.add_message(request, messages.ERROR, 'Phone number Invalid.')
        return redirect("/contactus/")
        # return HttpResponse('<script>alert("Please enter a valid mobile number"); history.go(-1);</script>')                
            
    # File =request.POST.FILE("screenshot",'Default')
    newContact  =  contact(email=email ,name=name , desc=desc , phone=tel)
    newContact.save()
    return HttpResponse("Thank you")
        
