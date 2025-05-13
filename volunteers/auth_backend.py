from django.conf import settings  # Добавьте эту строку
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError

class TelegramBackend(BaseBackend):
    def authenticate(self, request, telegram_data=None):
        if not telegram_data:
            return None
        
        try:
            verified_data = verify_telegram_authentication(
                bot_token=settings.TELEGRAM_BOT_TOKEN,  # Теперь settings доступен
                request_data=telegram_data
            )
            User = get_user_model()
            user, _ = User.objects.get_or_create(
                username=f"tg_{verified_data['id']}",
                defaults={
                    'first_name': verified_data.get('first_name', ''),
                    'last_name': verified_data.get('last_name', '')
                }
            )
            return user
        except (NotTelegramDataError, TelegramDataIsOutdatedError):
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None