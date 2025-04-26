from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define the structure of the form data
class TaxForm(BaseModel):
    name: str
    ssn: str
    income: float
    deductions: float

# 2. Define an API endpoint to receive tax form data
@app.post("/submit")
def calculate_tax(form: TaxForm):
    taxable_income = form.income - form.deductions

    # Let's assume a very simple tax rate: 20%
    estimated_tax = taxable_income * 0.20

    return {
        "name": form.name,
        "ssn": form.ssn,
        "taxable_income": taxable_income,
        "estimated_tax_due": estimated_tax
    }
