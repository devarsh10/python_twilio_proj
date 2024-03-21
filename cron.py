from apscheduler.schedulers.background import BackgroundScheduler

from twilio_prac import send_whatsapp_text,client,ques
import time
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job=scheduler.add_job(send_whatsapp_text,'cron',[client,ques],hour='19',minute='09')
print(job)

while True:
    time.sleep(1)