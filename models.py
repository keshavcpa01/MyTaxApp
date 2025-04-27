from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./tax.db"

Base = declarative_base()

class TaxSubmission(Base):
    __tablename__ = "tax_submissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ssn = Column(String, index=True)
    taxable_income = Column(Float)
    estimated_tax_due = Column(Float)

# Setup the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

