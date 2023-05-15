import os
import sys
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory path containing the app module
app_directory = os.path.dirname(os.path.dirname(current_file_path))

# Add the app directory to sys.path
sys.path.append(app_directory)

# Import the necessary modules from the app package
from app.events.qteam.send_results import send_results_qteam
from app.events.suzuki.send_results import send_results_suzuki


def create_workers(app):
    # Email schedule
    scheduler = BackgroundScheduler()
    
    # Define the time at which the job should run
    tz = timezone('Europe/Brussels')  # change timezone to GMT+2

    # Schedule the send_email job, passing the app object,
    existing_jobs = scheduler.get_jobs()
    job_names = [job.name for job in existing_jobs]

    # Check if the qteam job already exists
    if 'send_results_qteam' not in job_names:
        scheduler.add_job(send_results_qteam, 'cron', args=[app], hour=8, minute=0, timezone=tz)
        print("Qteam worker created")

    # Check if the suzuki job already exists
    if 'send_results_suzuki' not in job_names:
        scheduler.add_job(send_results_suzuki, 'cron', args=[app], hour=8, minute=0, timezone=tz)
        print("Suzuki worker created")
        
    scheduler.start()


app = Flask(__name__)
app.app_context().push()
create_workers(app)