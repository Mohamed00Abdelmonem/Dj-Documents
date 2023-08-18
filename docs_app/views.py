from django.shortcuts import render
from .models import Category, Document
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class List_Category(ListView):
    model = Category
    template_name = 'doc/category_list.html'




def Document_List(request, id):
    data = Category.objects.get(id=id)
    documents = Document.objects.filter(category = data)
    return render(request, 'doc/category_detail.html', {'category':data , 'documents':documents})


class Document_Detail(DetailView):
    model = Document
    template_name = 'doc/document_detail.html'
   





class Create_Category(CreateView):
    model = Category
    template_name = 'doc/create_category.html'
    fields = '__all__'
    success_url = '/'


class Create_Document(CreateView):
    model = Document
    template_name = 'doc/create_document.html'
    fields = '__all__'
    success_url = '/'    


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