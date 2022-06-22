from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('add_facility/',views.add_facility, name='add_facility'),
    path('make_trans/', views.make_transaction, name='make_trans'),
    path ('user_account/<int:pk>', views.User_account,name='user_account'),
    path('useracc-Statement',views.useracc_statement,name='account_statement'),
    path('update_acc/<int:id>',views.update_account, name='account_update'),
]