from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import TaxSubmission, SessionLocal

app = FastAPI()

class TaxData(BaseModel):
    name: str
    ssn: str
    taxable_income: float

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estimate-tax")
def estimate_tax(data: TaxData, db: Session = Depends(get_db)):
    tax_rate = 0.20
    estimated_tax_due = data.taxable_income * tax_rate

    submission = TaxSubmission(
        name=data.name,
        ssn=data.ssn,
        taxable_income=data.taxable_income,
        estimated_tax_due=estimated_tax_due
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return {
        "name": data.name,
        "ssn": data.ssn,
        "taxable_income": data.taxable_income,
        "estimated_tax_due": estimated_tax_due
    }
