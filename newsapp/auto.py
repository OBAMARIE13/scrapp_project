from apscheduler.schedulers.background import BackgroundScheduler
from manager.onu import scrap_onu_features


scheduler = BackgroundScheduler()

def the_runner():
    scrap_onu_features()


def run():
    
    scheduler.add_job(the_runner, 'interval', minutes=1)
    scheduler.start()
