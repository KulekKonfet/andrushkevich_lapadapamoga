from django.contrib import admin
from django.urls import path, include
from volunteers.views import telegram_auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from volunteers import views as volunteer_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Если нужен только один из двух:
    # path('auth/telegram/', telegram_auth, name='telegram_auth'),
    path('telegram-login/', volunteer_views.telegram_login, name='telegram_login'),

    path('', include('volunteers.urls')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),

    # Авторизация / Регистрация
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', volunteer_views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
