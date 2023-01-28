"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import  settings
from .import views,manager_views,teamlead_views,employee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE_FILE,name='base'),

    #login path
    path('',views.LOGIN,name='login'),
    path('dologin/',views.DOLOGIN,name='dologin'),

    #this is manager panel url
    path('manager/home/', manager_views.HOME,name='manager_home'),
    path('manager/employee/add/', manager_views.EMPLOYEE_ADD, name='employee_add'),
    path('manager/employee/view/',manager_views.VIEW_EMPLOYEE, name='view_employee'),
    path('manager/employee/edit/<str:id>',manager_views.EDIT_EMPLOYEE, name='edit_employee'),
    path('manager/employee/update/',manager_views.UPDATE_EMPLOYEE, name='update_employee'),
    path('manager/employee/delete/<str:admin>',manager_views.DELETE_EMPLOYEE, name='delete_employee'),

    path('manager/teamlead/add/',manager_views.ADD_TEAMLEAD, name='add_teamlead'),
    path('manager/teamlead/view/', manager_views.VIEW_TEAMLEAD, name='view_teamlead'),
    path('manager/teamlead/edit/<str:id>',manager_views.EDIT_TEAMLEAD,name='edit_teamlead'),
    path('manager/teamlead/update/>',manager_views.UPDATE_TEAMLEAD,name='update_teamlead'),


    path('manager/desingation/add/', manager_views.ADD_DESIGNATION, name='add_designation'),
    path('manager/desingation/view/', manager_views.VIEW_DESIGNATION, name='view_designation'),
    path('manager/desingation/edit/<str:id>', manager_views.EDIT_DESIGNATION, name='edit_designation'),
    path('manager/desingation/update/', manager_views.UPDATE_DESIGNATION, name='update_designation'),
    path('manager/desingation/delete/<str:id>', manager_views.DELETE_DESIGNATION, name='delete_designation'),

    #profile update
    path('profile/', views.PROFILE, name='profile'),
    path('profile/update/', views.PROFILE_UPDATE, name='profile_update'),

    #logout
    path('logout/',views.LOGOUT,name='logout'),
    

    
]
   
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)