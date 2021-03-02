from django.urls import path
from api import views

urlpatterns = [
    path('list/<int:id>/', views.ListByID.as_view(), name='list_id'),
    # path('list/<str:name>/', views.ListByName.as_view(), name='list_name'),
    path('list/<str:type>/', views.ListByType.as_view(), name='list_type'),
    path('list/<str:size>/', views.ListBySize.as_view(), name='list_size'),
    path('create/pizza/', views.CreatePizza.as_view(), name='create_pizza'),
    path('create/topping/', views.CreateTopping.as_view(), name='create_topping'),
    path('modify/<int:pk>/', views.Modify.as_view(), name='modify'),
]