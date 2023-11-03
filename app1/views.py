from django.shortcuts import render,redirect,get_object_or_404
from . import models
# Create your views here.
def home(request):

    if request.POST:
        note=request.POST.get("content")
        notes=models.Notes(note=note)
        notes.save()
    
    notes=models.Notes.objects.all()

    return render(request,"index.html",{"notes":notes})

def delete_note(request,id):
    instance=get_object_or_404(models.Notes,pk=id)
    instance.delete()

    return redirect('home')