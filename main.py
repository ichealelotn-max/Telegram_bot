import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatMemberStatus
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Direct token (agar environment variable use karna ho to os.getenv("BOT_TOKEN"))
TOKEN = "8259299390:AAHpXdqWXbaxJoFhqSp2WSKEG_CPCLQqrr0"

# 🔗 Channel IDs
CH1 = -1003031873990   # channel 1
CH2 = -1002742660499   # channel 2

# 🔗 Links
INSTAGRAM_LINK = "https://www.instagram.com/mods_zyphr3?igsh=MWN2cWRrcXk4cWt3Zg=="
YOUTUBE_LINK = "https://youtube.com/@sahilahmed-d3o?si=c8We3YjPu08e78Zy"
TELEGRAM_LINK1 = "https://t.me/+fyMHYwW3F6FiZTNl"
TELEGRAM_LINK2 = "https://t.me/premiumapkmodsfile"

JOIN_TEXT = (
    "👋 Welcome!\n\n"
    "⚠️ Pehle dono channel join karo:\n"
    f"1️⃣ {TELEGRAM_LINK1}\n"
    f"2️⃣ {TELEGRAM_LINK2}\n\n"
    "👉 Join karne ke baad /start dubara bhejo."
)

async def is_member(app, chat_id, user_id):
    if not chat_id:
        return True
    try:
        m = await app.bot.get_chat_member(chat_id, user_id)
        return m.status in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )
    except Exception:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ok1 = await is_member(context.application, CH1, user_id)
    ok2 = await is_member(context.application, CH2, user_id)

    if ok1 and ok2:
        keyboard = [
            [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
            [InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_LINK)],
            [InlineKeyboardButton("💬 Telegram 1", url=TELEGRAM_LINK1)],
            [InlineKeyboardButton("📂 Telegram 2", url=TELEGRAM_LINK2)]
        ]
        await update.message.reply_text(
            "✅ Access granted! Sab links yaha hai:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await update.message.reply_text(JOIN_TEXT)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
