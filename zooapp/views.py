from django.shortcuts import render
from django.http import HttpResponse
from zooapp.models import Contact

# Create your views here.
def home(request):
    return render(request,'front/home.html')
def contact(request):
    if request.method=='POST':
        name  = request.POST.get('name')
        email = request.POST.get('email')
        sub   = request.POST.get('subject')
        msg   = request.POST.get('message')

        if name !='' and email !='' and sub !='' and msg !='':
            contact_data = Contact(Name=name,Email=email,Subject=sub,Message=msg)
            contact_data.save()
    return render(request,'front/contact.html')
def about(request):
    return render(request,'front/about.html')
def visit(request):
    return render(request,'front/visit.html')
