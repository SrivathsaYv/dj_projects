"""
URL configuration for P2_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from student import views
urlpatterns = [
    path('student_create/', views.create),
    path('student_pick/', views.pick),
    path('student/edit/name', views.edit_name),
    path('student/db/update/name', views.update_name),
    # path('student/edit/email', views.edit_email),
    # path('student/edit/roll_no', views.edit_roll_no),
    # path('student/edit/dob', views.edit_dob),
]
