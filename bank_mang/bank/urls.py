from django.urls import path
from . import views

urlpatterns=[
   path('',views.index),
   path('about/',views.about,name='about'),
   path('account_list/',views.users_list,name='account_list'),
   path('account_detail/<int:pk>/',views.users_detail,name='account_detail'),
   path('account_form/',views.users_create,name='account_form'),
   path('account_update/<int:pk>/',views.users_update,name='account_update'),
   path('account_delete/<int:pk>/',views.users_delete,name='account_delete'),
   path('deposit/<int:pk>/',views.deposit,name='deposit'),
   path('withdraw/<int:pk>/',views.withdraw,name='withdraw'),
]
