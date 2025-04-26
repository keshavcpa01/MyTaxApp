
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/submit")
async def calculate_tax(
    name: str = Form(...),
    ssn: str = Form(...),
    income: float = Form(...),
    deductions: float = Form(...)
):
    taxable_income = income - deductions
    estimated_tax = taxable_income * 0.20  # Example flat 20% tax rate

    return JSONResponse({
        "name": name,
        "ssn": ssn,
        "taxable_income": taxable_income,
        "estimated_tax_due": estimated_tax
    })
