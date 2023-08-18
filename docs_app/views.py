from django.shortcuts import render
from .models import Category, Document
from django.views.generic import ListView, DetailView
# Create your views here.

class List_Category(ListView):
    model = Category
    template_name = 'doc/category_list.html'




def Document_List(request, id):
    data = Category.objects.get(id=id)
    documents = Document.objects.filter(category = data)
    return render(request, 'doc/category_detail.html', {'category':data , 'documents':documents})


