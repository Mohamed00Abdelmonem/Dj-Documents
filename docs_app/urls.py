from django.urls import path
from .views import (Document_List,List_Category, Document_Detail,
                    Create_Category, Create_Document, Update_Category,
                    Update_Document,Delete_Category, Delete_Document)
                    
urlpatterns = [
    path('', List_Category.as_view(), name='list_category'),
    path('category/<int:id>', Document_List, name='document_list'),
    path('category/<int:id>/document/<int:pk>', Document_Detail.as_view(), name='document_detail'),
    path('create_category', Create_Category.as_view(), name='create_category'),
    path('create_document', Create_Document.as_view(), name='create_document'),
    path('update_category/<int:pk>', Update_Category.as_view(), name='update_category'),
    path('update_document/<int:pk>', Update_Document.as_view(), name='update_document'),
    path('delete_category/<int:pk>', Delete_Category.as_view(), name='delete_category'),
    path('delete_document/<int:pk>', Delete_Document.as_view(), name='delete_document'),
]
