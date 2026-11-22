from django.urls import path
from student import views

urlpatterns = [
    path('student_create/', views.create),
    path('student_pick/', views.pick),

    path('student/edit/name', views.edit_name),
    path('student/db/update/name', views.update_name),

    # Add these two URLs for Email Update
    path('student/edit/email', views.edit_email),
    path('student/db/update/email', views.update_email),

    path('student/edit/dob', views.edit_dob),
    path('student/db/update/dob', views.update_dob),

    path('student/edit/roll_no', views.edit_roll_no),
    path('student/db/update/roll_no', views.update_roll_no),

    path('student/delete/', views.delete_student),
]