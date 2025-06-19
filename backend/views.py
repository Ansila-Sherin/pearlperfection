from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
def message(request):
    return HttpResponse("first django project")

from backend.forms import *
def product(request):
    frm=ProductForm()
    return render(request,"productform.html",{'frm':frm})


# def save_form (request):
#    if request.POST:
#     frm=productform(request.post,request.FILES)
#     if frm.is_valid():
#        frm.save()
#     else:
#        frm=productform()    


def save_form (request):
    if request.POST:
        frm=ProductForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect (product)
        else:
            frm=ProductForm()
        return redirect(product,{'frm':frm})
    
def table(request):
    data=productTable.objects.all()
    return render(request,"producttable.html",{'data':data})   
def delete(request,dataid):
    data=productTable.objects.filter(id=dataid)
    data.delete()
    return redirect(table) 

def edit(request, dataid):
    edited = productTable.objects.get(id=dataid)
    if request.method == 'POST':
        frm = ProductForm(request.POST, request.FILES, instance=edited)
        if frm.is_valid():
            frm.save()
            return redirect('table')  # replace with your actual redirect target
    else:
        frm = ProductForm(instance=edited)
    return render(request, "productedit.html", {"frm": frm})


