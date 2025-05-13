import os
import logging

from django.core.management.base import BaseCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

from volunteers.models import VolunteerProject


# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Команды бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Это бот платформы ЛапаДапамога 🐾")

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    projects = VolunteerProject.objects.all()
    if projects:
        message = "\n\n".join(
            [f"📌 {p.title}\n{p.description}" for p in projects]
        )
    else:
        message = "Нет доступных проектов 😢"
    await update.message.reply_text(message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - приветствие\n"
        "/projects - список проектов\n"
        "/help - помощь"
    )


# Основная команда Django
class Command(BaseCommand):
    help = "Запускает Telegram-бота"

    def handle(self, *args, **kwargs):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            self.stderr.write("❌ TELEGRAM_BOT_TOKEN не найден в переменных окружения.")
            return

        application = ApplicationBuilder().token(token).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("projects", projects))
        application.add_handler(CommandHandler("help", help_command))

        self.stdout.write("✅ Бот запущен. Ожидаю команды в Telegram...")
        application.run_polling()
