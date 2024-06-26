from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

def job():
    # Run daily-news-sql.py
    subprocess.run(["python", "/work/MLops/daily-news-sql.py"])
    # Run llm.py
    subprocess.run(["python", "/work/MLops/llm.py"])

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the job to run every 24 hours at midnight
scheduler.add_job(job, 'cron', hour=0)

try:
    # Start the scheduler
    scheduler.start()
except KeyboardInterrupt:
    # Stop the scheduler if interrupted
    scheduler.shutdown()