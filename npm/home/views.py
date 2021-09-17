from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
# Create your views here.
def home(request):

    return render(request,"home/index.html")

def contactUs(request):
    return render(request,"home\contactus.html")

def contactSubmit(request):
    email = request.POST.get("email")
    name = request.POST.get("name")
    tel = request.POST.get("phone")
    desc = request.POST.get("desc")
    # File =request.POST.FILE("screenshot",'Default')
    newContact  =  contact(email=email ,name=name , desc=desc , phone=tel)
    newContact.save()
    return HttpResponse("Thank you")

    if(not(len(tel)==tel)):
            messages.add_message(request, messages.ERROR, 'Phone number Invalid.')
            return redirect("/contactus/")
        
