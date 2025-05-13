import os
import django
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')
django.setup()

from volunteers.models import VolunteerProject

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Это бот платформы ЛапаДапамога 🐾")

# Команда /projects
async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    projects = VolunteerProject.objects.all()
    if projects:
        message = "\n\n".join(
            [f"📌 {p.title}\n{p.description}" for p in projects]
        )
    else:
        message = "Нет доступных проектов 😢"

    await update.message.reply_text(message)

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - приветствие\n"
        "/projects - список проектов\n"
        "/help - помощь"
    )

# Главная функция запуска
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения.")

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("projects", projects))
    application.add_handler(CommandHandler("help", help_command))

    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
