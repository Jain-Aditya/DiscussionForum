
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.detail, name='detail'),
    path('<int:category_id>/insert/', views.InsertDiscussion, name='InsertDiscussion'),
    path('discussion/<int:discussion_id>/', views.comment, name='comment'),
    path('discussion/insert/<int:discussion_id>/', views.InsertComment, name='InsertComment')

            
]
