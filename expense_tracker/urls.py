"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),                                     # showing home page
    path('register/', views.registerform),                      # showing registration page
    path('adduser/',views.adduser),                           # adding user 
    path('login/', views.login),                                  # login page
    path('dashboard/', views.dashboard),                        # dashboard page
    path('newexp/',views.newexpense),                              # add_expense page
    path('addexp/',views.addexpense),                             # for adding form submit
   path('modify/',views.modify),                                    # for modify page
   path('edit_expense/',views.edit_expense),                        # modify form edit_expense
   path('modifystatus/',views.modifystatus),                        # modify status
    path('delete/',views.delete),                                   # deleteExpense page
    path('deleteexpense/', views.deleteexpense),                  # after detele expense page
    path('report/',views.showreport),                             # report page
    path('search/',views.search),                                      # search page
    path('searchexpenses/',views.searchexp),                          # after serach page
    path('change/',views.change),                                   # change_password page
    path('changepass/',views.changepass),                              # after change_password page
    path('profile/',views.profile),                                # profile page
    path('logout/', views.logout),                                    # logout page     
]
