from django.urls import path
from .import views
urlpatterns = [
    path('addemployee', views.addemployee, name='addemployee'),
    path('empdetails',views.empdetails, name='empdetails'),
    path('addempdata', views.addempdata,name='addempdata'),
    path('edit/<int:eid>',views.edit, name='edit'),
    path('update/<int:eid>',views.update, name='update'),
    path('delete/<int:eid>',views.delete, name='delete'),


]
