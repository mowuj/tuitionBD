from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', registration, name='signup'),
    path('change_password/', change_password, name='change_password'),

    path('reset/password/', PasswordResetView.as_view(template_name='session/reset_pass.html'), name='password_reset'),

    path('reset/password/done/', PasswordResetDoneView.as_view(
        template_name='session/reset_pass_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='session/pass_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='session/pass_reset_complete.html'), name='password_reset_complete'),
]
