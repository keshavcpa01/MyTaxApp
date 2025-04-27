from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class TaxSubmission(Base):
    __tablename__ = "tax_submissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ssn = Column(String, unique=True, index=True)
    taxable_income = Column(Float)
    estimated_tax_due = Column(Float)

