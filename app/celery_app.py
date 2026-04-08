from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

celery_app = Celery(
    "invoice_processor",
    broker=os.getenv("BROKER_URL"),
    backend=os.getenv("BACKEND_URL"),
    include=["app.tasks"]
)