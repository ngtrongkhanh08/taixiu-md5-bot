
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import hashlib

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gửi /md5 <chuỗi MD5> để phân tích tài xỉu!")

async def md5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Vui lòng gửi đúng cú pháp: /md5 <chuỗi_md5>")
        return
    md5_string = context.args[0]
    digits = ''.join(filter(str.isdigit, md5_string))[:6]
    if len(digits) < 6:
        await update.message.reply_text("Chuỗi không hợp lệ để phân tích.")
        return
    dice = [int(d) % 6 + 1 for d in digits[:3]]
    total = sum(dice)
    result = "Tài" if total >= 11 else "Xỉu"
    await update.message.reply_text(f"🎲 Kết quả: {dice} → Tổng: {total} → {result}")

if __name__ == "__main__":
    import os
    TOKEN = os.environ.get("YOUR_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("md5", md5))
    app.run_polling()
