import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
print("🧪 TOKEN =", repr(TOKEN))

print("✅ 最新 bot.py 成功部署")
print("TOKEN:", repr(os.environ.get("TELEGRAM_TOKEN")))
print("GROUP_ID:", repr(os.environ.get("TELEGRAM_GROUP_ID")))
from keep_alive import keep_alive
import telebot
import os
import datetime

# ✅ Telegram Bot 设置
TOKEN = os.environ.get("TELEGRAM_TOKEN")
GROUP_ID = os.environ.get("TELEGRAM_GROUP_ID")

bot = telebot.TeleBot(TOKEN)

# ✅ 每日推送信息内容
def get_daily_message():
    today = datetime.date.today().strftime('%Y年%m月%d日（%A）')
    return f"""
📌 每日任务推送结构如下：

📅 日期：{today}
📋 今日任务清单（未完成）：

✅ Miracore 系统任务：
• 自动发送 Telegram 每日提醒
• 显化进度追踪 + 回流提醒

😽 美容院模块任务：
• 预约顾客确认 + 准备今日疗程
• 整理昨日顾客反馈记录

🔮 命理顾客任务：
• 整理 511 命理顾客咨询数据
• 生成报告并准备发送

🧩 系统开发任务：
🔷 检查 AI 系统进度
📄 可参考：《AI智能王国系统_总进度检查表》

💡 鼓励语：
「再小的坚持，也会创造奇迹。」
"""

# ✅ 回应 start 指令
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ferrari AI 任务提醒系统已启动 ✅")

# ✅ 回复你好
@bot.message_handler(func=lambda message: '你好' in message.text)
def reply_hello(message):
    bot.reply_to(message, "你好 Ferrari👑，AI 总管家在这里，有什么吩咐？")

# ✅ 每次启动就自动推送到群组
def push_daily_message():
    if GROUP_ID:
        bot.send_message(GROUP_ID, get_daily_message())
    else:
        print("⚠️ 没有设置 TELEGRAM_GROUP_ID")

# ✅ 保持运行 + 启动轮询
keep_alive()
push_daily_message()
bot.polling()
