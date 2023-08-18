from django.urls import path
from .views import List_Category, Document_List
urlpatterns = [
    path('', List_Category.as_view(), name='list_category'),
    path('category/<int:id>', Document_List, name='document_list'),
]
