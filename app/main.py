from fastapi import FastAPI
from app.routes.invoice import router as invoice_router

app = FastAPI()

app.include_router(invoice_router, prefix="/invoice")