"""
URL configuration for LITRevu project.

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
import tickets.views
import authentication.views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('home/', tickets.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket/add/', tickets.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/edit/',
         tickets.views.edit_ticket,
         name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete/',
         tickets.views.delete_ticket,
         name='delete_ticket'),
    path('review/create/',
         tickets.views.create_ticket_review,
         name='create_ticket_review'),
    path('review/<int:review_id>/edit/',
         tickets.views.edit_review,
         name='edit_review'),
    path('review/<int:review_id>/delete/',
         tickets.views.delete_review,
         name='delete_review'),
    path('ticket/<int:ticket_id>/review/',
         tickets.views.create_review_for_ticket,
         name='create_review_for_ticket'),
    path("follows/", tickets.views.follow_user, name="follows"),
    path("unfollow/<int:followed_id>/", tickets.views.unfollow_view, name="unfollow"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)