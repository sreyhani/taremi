from django.urls import path

from . import views

urlpatterns = [
    path('account/signup/', views.signup_user, name='signup'),
    path('account/login/', views.login_user, name='login'),
    path('laccount/ogout/', views.logout_user, name='logout'),
    path('account/activate/<int:uid>/<str:token>', views.activate, name='activate')
]
