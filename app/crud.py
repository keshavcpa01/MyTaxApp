from sqlalchemy.orm import Session
from app import models, schemas

def save_submission(db: Session, form: schemas.TaxForm, estimated_tax_due: float):
    submission = models.TaxSubmission(
        name=form.name,
        ssn=form.ssn,
        taxable_income=form.taxable_income,
        estimated_tax_due=estimated_tax_due
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return submission

