from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# 🔑 BOT_TOKEN aur CHANNEL_ID environment me dalna
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# 🔗 Links yaha dalna
INSTAGRAM_LINK = "https://instagram.com/YourUsername"
YOUTUBE_LINK = "https://youtube.com/@YourChannel"
TELEGRAM_GROUP = "https://t.me/YourGroupLink"
PREMIUM_APK = "https://your-apk-link.com"

# ✅ Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user.id)
        if member.status in ["member", "administrator", "creator"]:
            keyboard = [
                [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
                [InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_LINK)],
                [InlineKeyboardButton("💬 Telegram Group", url=TELEGRAM_GROUP)],
                [InlineKeyboardButton("📂 Premium APK", url=PREMIUM_APK)]
            ]
            await update.message.reply_text(
                "🎉 Welcome! Yaha se sab links access karo:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await update.message.reply_text(
                "⚠️ Pehle hamare channel join karo fir /start dabao!",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅ Channel Join Karo", url="https://t.me/YourChannelUsername")]
                ])
            )
    except:
        await update.message.reply_text("❌ Error aaya hai, channel ID ya link check karo.")

# 🚀 Main Function
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
