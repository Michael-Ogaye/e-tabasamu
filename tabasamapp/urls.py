from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('add_facility',views.add_facility, name='add_facility'),
    path('make_trans', views.make_transaction, name='make_trans'),
]