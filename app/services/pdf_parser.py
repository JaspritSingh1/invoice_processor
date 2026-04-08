import pdfplumber
import io
from typing import Any


def parse_invoice_pdf(file_bytes: bytes) -> dict[str, Any]:
    result = {
        "total_pages": 0,
        "raw_text": "",
        "pages": [],
        "tables": []
    }

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        result["total_pages"] = len(pdf.pages)

        for i, page in enumerate(pdf.pages):
            try:
                text = page.extract_text()
                tables = page.extract_tables()
            except Exception:
                text = None
                tables = []

            page_tables = []

            if tables:
                for table in tables:
                    table_data = {
                        "page_number": i + 1,
                        "data": table
                    }
                    page_tables.append(table_data)
                    result["tables"].append(table_data)

            result["pages"].append({
                "page_number": i + 1,
                "text": text,
                "tables": page_tables
            })

            result["raw_text"] += (text or "") + "\n"

    return result