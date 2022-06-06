from django.shortcuts import render,redirect
from app1.forms import LaptopForm
from app1.models import Laptop
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def LaptopView(request):
    form=LaptopForm()
    template_name="app1/Laptop_form.html"
    context={'form':form}
    
    if request.method=='POST':
        form=LaptopForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('showlaptop_url')
    return render(request,template_name,context)
    
@login_required
def ShowLaptopView(request):
    obj=Laptop.objects.all()
    template_name='app1/show_laptop.html'
    context={'data':obj}
    return render(request,template_name,context)

def UpdateLaptopView(request,id):
    obj=Laptop.objects.get(id=id)
    form=LaptopForm(instance=obj)
    template_name="app1/Laptop_form.html"
    if request.method=='POST':
        form=LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showlaptop_url')
    context={'form':form}
    return render(request,template_name,context)

def deleteLaptopView(request,id):
    obj=Laptop.objects.get(id=id)
    template_name="app1/conformation.html"
    context={'data':obj}
    if request.method=='POST':
        obj.delete()
        return redirect('showlaptop_url')
    return render(request,template_name,context)
    


