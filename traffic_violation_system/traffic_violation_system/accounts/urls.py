from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    account_settings,
    signup,
    staff_portal,
    update_email,
    update_mobile,
)


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('settings/', account_settings, name='account_settings'),
    path('update-email/', update_email, name='update_email'),
    path('update-mobile/', update_mobile, name='update_mobile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url='/accounts/settings/'
    ), name='change_password'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path(
        'staff-login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            extra_context={
                'login_header': 'Staff Login',
                'login_title': 'Staff Login Required',
                'login_message': 'Use your staff account to monitor system activity and manage payments.',
                'staff_login': True,
            },
        ),
        name='staff_login',
    ),
    path('staff-portal/', staff_portal, name='staff_portal'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
