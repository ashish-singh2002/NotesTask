from django.shortcuts import render,redirect,get_object_or_404
from .models import Ashish
from .forms import AshishForm

def insert(request):
    if request.method == 'POST':
        form = AshishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read') 
    else:
        form = AshishForm()
    return render(request, 'insert.html', {'form': form})




def read(request):
    all_data=Ashish.objects.all()
    return render(request,"read.html",{'all_data':all_data})




def edit(request,id):
    edit=get_object_or_404(Ashish,pk=id)
    if request.method=='POST':
        form=AshishForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form=AshishForm(instance=edit)
    return render(request,"insert.html",{'form':form})



def delete(request,id):
    delete = get_object_or_404(Ashish,pk=id)
    if request.method=='POST':
            delete.delete()
            return redirect('read')
    else:
        form=AshishForm(instance=delete)
        return render(request,"delete.html",{'form':form})
