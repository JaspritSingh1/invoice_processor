from app.celery_app import celery_app
from app.services.pdf_parser import parse_invoice_pdf


@celery_app.task
def parse_pdf_task(file_bytes: bytes):
    result = parse_invoice_pdf(file_bytes)

    # 👇 ADD THIS HERE
    print(f"RAW TEXT LENGTH: {len(result["raw_text"])}")

    return result