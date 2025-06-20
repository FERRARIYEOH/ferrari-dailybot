
import schedule
import time
from datetime import datetime

def run_reminder():
    def job():
        print(f"[提醒] 当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} —— 记得查看你的任务清单 ✅")

    # 每隔 10 秒提醒一次（你可以改成 schedule.every().day.at("08:00") 等）
    schedule.every(10).seconds.do(job)

    print("✅ 任务提醒已启动...")
    while True:
        schedule.run_pending()
        time.sleep(1)
