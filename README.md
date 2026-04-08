# Invoice PDF Processor (Prototype)

This is a simple prototype built using:

- FastAPI → API layer
- Celery → background task processing
- Redis → message broker + result backend
- pdfplumber → PDF parsing

---

## 🚀 Features

- Upload PDF invoices
- Parse text and tables from PDF
- Process files asynchronously using Celery
- Return a task ID for tracking

---

## 🧱 Project Structure
