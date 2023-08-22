from django.urls import path
from .views import (Document_List, Dashboard_List_Document,List_Category, Dashboard_List_Category, Document_Detail,
                    Create_Category, Create_Document, Update_Category,
                    Update_Document,Delete_Category, Delete_Document)
                    
urlpatterns = [
    path('', List_Category.as_view(), name='list_category'),
    path('dashboard/', Dashboard_List_Category.as_view(), name='dashboard'),
    path('dashboard/<int:id>', Dashboard_List_Document, name='dashboard_docs'),
    path('category/<int:id>', Document_List, name='document_list'),
    path('category/<int:id>/document/<int:pk>', Document_Detail.as_view(), name='document_detail'),
    path('create_category', Create_Category, name='create_category'),
    path('create_document/<int:id>', Create_Document, name='create_document'),
    path('update_category/<int:pk>', Update_Category.as_view(), name='update_category'),
    path('update_document/<int:id>', Update_Document, name='update_document'),
    path('delete_category/<int:pk>', Delete_Category.as_view(), name='delete_category'),
    path('delete_document/<int:pk>', Delete_Document.as_view(), name='delete_document'),
]
