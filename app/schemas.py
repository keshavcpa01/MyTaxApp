from pydantic import BaseModel

class TaxForm(BaseModel):
    name: str
    ssn: str
    taxable_income: float
    filing_status: str

