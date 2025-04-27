from fastapi import FastAPI, Form, Depends
from sqlalchemy.orm import Session
from models import TaxSubmission, SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estimate-tax")
def estimate_tax(
    name: str = Form(...),
    ssn: str = Form(...),
    taxable_income: float = Form(...),
    db: Session = Depends(get_db)
):
    tax_rate = 0.20
    estimated_tax_due = taxable_income * tax_rate

    submission = TaxSubmission(
        name=name,
        ssn=ssn,
        taxable_income=taxable_income,
        estimated_tax_due=estimated_tax_due
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return {
        "name": name,
        "ssn": ssn,
        "taxable_income": taxable_income,
        "estimated_tax_due": estimated_tax_due
    }
