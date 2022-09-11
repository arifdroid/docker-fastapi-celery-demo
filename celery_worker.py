import os
import time
from celery import Celery
from dotenv import load_dotenv
from chromeScraper import scraping_script
from sampleScraperFile import download_scraping_script_demo

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    return b+c

@celery.task(name="scrape_data")
def scrape_data():
    print("scraping 1")
    data = scraping_script()
    return data

@celery.task(name="demo_scrape_data")
def demo_scrape_data():
    print("scraping demo 1")
    data = download_scraping_script_demo()
    return data
