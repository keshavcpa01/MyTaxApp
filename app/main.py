from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import TaxSubmission
from app.database import SessionLocal, engine
from app.schemas import TaxForm
from app.crud import save_submission

from sqlalchemy.exc import SQLAlchemyError

# Create tables automatically
from app.database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

def calculate_tax(income: float, filing_status: str) -> float:
    tax = 0

    if filing_status.lower() == 'single':
        brackets = [
            (11600, 0.10),
            (47150, 0.12),
            (100525, 0.22),
            (191950, 0.24),
            (243725, 0.32),
            (609350, 0.35),
            (float('inf'), 0.37)
        ]
    elif filing_status.lower() == 'married':
        brackets = [
            (23200, 0.10),
            (94300, 0.12),
            (201050, 0.22),
            (383900, 0.24),
            (487450, 0.32),
            (731200, 0.35),
            (float('inf'), 0.37)
        ]
    else:
        brackets = [
            (11600, 0.10),
            (47150, 0.12),
            (100525, 0.22),
            (191950, 0.24),
            (243725, 0.32),
            (609350, 0.35),
            (float('inf'), 0.37)
        ]

    previous_limit = 0
    for limit, rate in brackets:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estimate-tax")
def estimate_tax(form: TaxForm, db: Session = Depends(get_db)):
    try:
        estimated_tax_due = calculate_tax(form.taxable_income, form.filing_status)
        submission = save_submission(db, form, estimated_tax_due)

        return {
            "name": submission.name,
            "ssn": submission.ssn,
            "filing_status": form.filing_status,
            "taxable_income": submission.taxable_income,
            "estimated_tax_due": round(submission.estimated_tax_due, 2)
        }
    except SQLAlchemyError as e:
        return {"error": str(e)}

