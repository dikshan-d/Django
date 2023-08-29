from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDO

# Create your views here.
def home(request):
    todo_objects = ToDO.objects.all() #query all object from class todo from models.py
    content={'todo':todo_objects}
    return render(request,'index.html',context=content)
def create(request):
    if request.method == "POST":
        name= request.POST.get('name')
        description=request.POST.get('description')
        status = request.POST.get('status')
        ToDO.objects.create(name= name,description=description,status=status)
        return redirect(to = 'home')
    content = {'method':'create'}
    return render(request,'create.html',context=content)

def edit(request,pk):

    obj = ToDO.objects.get(id=pk) #database query
    if request.method == 'POST':
        name= request.POST.get('name')
        description=request.POST.get('description')
        status = request.POST.get('status')
        obj.name = name
        obj.description = description
        obj.status= status
        obj.save()
        return redirect(to='home')
        # ToDO.object.request.create(name=name,description=description,status=status)
    content = {'method':'edit','object':obj}
    return render(request,'create.html',context=content)
def delete(request,pk):
    obj = ToDO.objects.get(id=pk)
    obj.delete()
    return redirect(to='home')
def deleteall(request):
    objects = ToDO.objects.all()
    objects.delete()
    return redirect(to='home')
    
