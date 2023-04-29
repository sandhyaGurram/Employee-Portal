from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('login/',views.login_user,name='login'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('view_emp/<str:pk>',views.view_emp,name='view_emp'),
    path('update/<str:pk>', views.update_emp ,name='update'),
    path('delete/<str:pk>', views.delete_emp ,name='delete'),
]