from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style='color: green;'>✅ Ferrari DailyBot 已上线！</h1>
    <p>欢迎来到 Ferrari AI 智能任务提醒系统。</p>
    <p>系统运行正常，请放心使用。</p>
    """

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
