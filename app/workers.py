from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone

def create_workers(app):
    from app.events.qteam.send_results import send_results_qteam
    from app.events.suzuki.send_results import send_results_suzuki
    # Email schedule
    scheduler = BackgroundScheduler()
    
    # define the time at which the job should run
    tz = timezone('Europe/Brussels') # change timezone to GMT+2

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