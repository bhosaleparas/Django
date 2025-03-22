from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *

def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context={'tasks':tasks,'form':form}
    return render(request,'list.html',context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)  # Pre-fill form with task data

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  # Bind form to task
        if form.is_valid():
            form.save()
            return redirect("/")  # Redirect back to home after update

    context = {"form": form}
    return render(request, "update_task.html", context)



def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")  # Redirect after deletion

    return render(request, "delete_task.html", {"task": task})