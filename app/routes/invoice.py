from fastapi import APIRouter, UploadFile, File
from app.tasks import parse_pdf_task

router = APIRouter()


@router.post("/parse-invoice")
async def parse_invoice(file: UploadFile = File(...)):
    file_bytes = await file.read()

    task = parse_pdf_task.delay(file_bytes)

    return {
        "task_id": task.id,
        "status": "processing"
    }