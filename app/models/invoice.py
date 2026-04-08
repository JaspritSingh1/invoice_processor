from pydantic import BaseModel
from typing import List, Optional


class InvoiceItem(BaseModel):
    description: Optional[str] = None
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    total: Optional[float] = None


class Invoice(BaseModel):
    invoice_number: Optional[str] = None
    date: Optional[str] = None
    vendor_name: Optional[str] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    items: List[InvoiceItem] = []