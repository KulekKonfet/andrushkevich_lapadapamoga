from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from volunteers import views as volunteer_views
from django.contrib.auth.views import LogoutView

class LogoutRedirectView(LogoutView):
    next_page = '/logout-success/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('telegram-login/', volunteer_views.telegram_login, name='telegram_login'),
    path('', include('volunteers.urls')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),

    # Авторизация / Регистрация
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('signup/', volunteer_views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 # Обработчики ошибок   
handler404 = 'core.views.custom_404_view'
handler500 = 'core.views.custom_500_view'
