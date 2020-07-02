#!/usr/bin/python3
import os
import schedule
import logging
from logging.handlers import RotatingFileHandler
from time import sleep
from instapy import InstaPy

igun = os.environ['IGUN']
igpw = os.environ['IGPW']
sigOther = os.environ['IGSigOther']
# sigOther = 'your_significant_others_insta_name'
minutes = 5
numOfPosts = 3
log_file = 'instalikes.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger()

handler = RotatingFileHandler(log_file, maxBytes=500000, backupCount=1)
log.addHandler(handler)

def job():
    logging.info('Running InstaPy Job.')
    session = InstaPy(username=igun, password=igpw, headless_browser=True)
    session.login()
    session.set_do_like(True, percentage=100)
    session.interact_by_users([sigOther], amount=numOfPosts)
    session.end()

print('creating scheduled job')
log.info('creating scheduled job')
schedule.every(minutes).minutes.do(job)
print('created scheduled job')
log.info('created scheduled job')

count = 0
log.info(f'initializing while loop for running the job every {minutes} minutes.')
while True:
    sleep(1)
    count = count + 1
    if count == 1:
        print('waiting for scheduled job timer....')
    if count == 30:
        count = 1
    try:
        schedule.run_pending()
    except:
        log.warning('Exception occurred, rescheduling job.')
        schedule.every(minutes).minutes.do(job)
        continue
