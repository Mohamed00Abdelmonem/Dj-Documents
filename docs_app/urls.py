from django.urls import path
from .views import List_Category, Document_List, Document_Detail
urlpatterns = [
    path('', List_Category.as_view(), name='list_category'),
    path('category/<int:id>', Document_List, name='document_list'),
    path('category/<int:id>/document/<int:pk>', Document_Detail.as_view(), name='document_detail'),
]
