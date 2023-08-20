from django.shortcuts import render, redirect
from .models import Category, Document
from .forms import Document_Form, Category_Form
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class List_Category(ListView):
    model = Category
    template_name = 'doc/category_list.html'


class Dashboard_List_Category(ListView):
    model = Category
    template_name = 'doc/dashboard.html'




def Document_List(request, id):
    data = Category.objects.get(id=id)
    documents = Document.objects.filter(category = data)
    return render(request, 'doc/category_detail.html', {'category':data , 'documents':documents})


class Document_Detail(DetailView):
    model = Document
    template_name = 'doc/document_detail.html'
   




def Create_Category(request):
    if request.method == 'POST':
        form = Category_Form(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/')
    else:
        form = Category_Form()

    return render (request,'doc/create_document.html', {'form': form} )

# class Create_Category(CreateView):
#     model = Category
#     template_name = 'doc/create_category.html'
#     fields = '__all__'
#     success_url = '/'



def Create_Document(request, id):
    data = Category.objects.get(id=id)
    if request.method == 'POST':
        form = Document_Form(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.category = data  # Assign the section to the subject
            myform.save()
            return redirect('/')
    else:
        form = Document_Form()

    return render (request,'doc/create_document.html', {'form': form} )




class Update_Category(UpdateView):
    model = Category
    fields = '__all__'    
    template_name = 'doc/update_form.html'
    success_url = '/'    


class Update_Document(UpdateView):
    model = Document
    fields = '__all__'    
    template_name = 'doc/update_form.html'
    success_url = '/'    


class Delete_Category(DeleteView):
    model = Category
    success_url = '/'    
    template_name = 'delete_category.html'



class Delete_Document(DeleteView):
    model = Document
    success_url = '/'    
    template_name = 'delete_document.html'


def dashboard(request):
    return render(request, 'doc/dashboard.html')    