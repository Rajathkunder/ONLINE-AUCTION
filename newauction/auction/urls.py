from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('addrecord/addingitem/',views.addingitem, name='addingitem'),
    path('addrecord/addingitem/added/',views.added, name='added'),
    path('addrecord/view/',views.view, name='view'),
    path('addrecord/view/delete/<int:id>',views.delete, name='delete'),
    path('addrecord/view/update/<int:id>',views.update, name='update'),
    path('addrecord/view/update/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
    path('userpage/',views.userpage,name='userpage'),
    path('addrecord/bid/<int:id>&<str:username>',views.bid,name='bid'),
    path('addrecord/bid/placebid/<int:id>&<str:itemname>&<int:highprice>&<str:username>',views.placebid,name='placebid')
    
]