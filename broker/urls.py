from django.urls import path,re_path
from django.conf.urls import url
from . import views, api


urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student_home, name='student_home'),
    path('apply/<int:id>/', views.application, name='apply_form'),
    path('apply/success/', views.application_success, name='application_success'),
    path('apply/failed/', views.application_failed, name='application_failed'),
    path('instructor/', views.instructor_home, name='instructor_home'),
    path('instructor/form/new/', views.instructor_create_form, name='create_form'),

    path('instructor/form/<int:id>/', views.instructor_form_detail, name='instructor_form_detail'),
    path('instructor/form/<int:id>/delete/', views.instructor_form_delete, name='instructor_form_delete'),
    path('student/response/<int:id>/delete/', views.student_response_delete, name='student_response_delete'),


    path('instructor/res/<int:id>/', views.instructor_response_detail, name='instructor_response_detail'),
    path('api/change_response_state', api.change_response_state, name='change_response_state'),

    path('student/view_profile/', views.view_student_profile, name='view_student_profile'),
    path('student/update_profile/', views.update_student_profile.as_view(), name='update_student_profile'),

    path('instructor/view_profile/', views.view_profile, name="view_instructor_profile"),
    path('instructor/update_profile/', views.update_instructor_profile.as_view(), name="update_instructor_profile"),


    path('instructor/view_student/<int:pk>', views.view_student, name='view_student'),
    path('instructor/view_student/<int:pk>', views.view_instructor, name='view_instructor'),

]
