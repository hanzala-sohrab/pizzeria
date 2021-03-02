from django.urls import path
from api import views

urlpatterns = [
    path('list/id/<int:id>/', views.ListByID.as_view(), name='list_id'),
    path('list/type/<str:type>/', views.ListByType.as_view(), name='list_type'),
    path('list/size/<str:size>/', views.ListBySize.as_view(), name='list_size'),
    path('list/all/', views.ListAll.as_view(), name='list_all'),
    path('list/all/toppings/', views.ListAllTopping.as_view(), name='list_all_topping'),
    path('list/all/size/', views.ListAllSize.as_view(), name='list_all_size'),
    path('create/pizza/', views.CreatePizza.as_view(), name='create_pizza'),
    path('create/topping/', views.CreateTopping.as_view(), name='create_topping'),
    path('create/size/', views.CreateSize.as_view(), name='create_size'),
    path('modify/<int:pk>/', views.Modify.as_view(), name='modify'),
]
