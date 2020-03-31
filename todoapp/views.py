from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import  todoitem
# Create your views here.
def todo(request):
    all_items=todoitem.objects.all()

    return render(request,'todo.html',{'all_items':all_items})

def add_to_do(request):
    a=todoitem(content=request.POST['content'])
    a.save()
    return HttpResponseRedirect("/todo/")

def delete_to_do(request,oid):
    a=todoitem.objects.get(id=oid)
    a.delete()

    return HttpResponseRedirect("/todo/")
