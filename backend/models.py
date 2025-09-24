from pydantic import BaseModel
from typing import List

class CreditInstitution(BaseModel):
    name: str
    country: str
    founding_year: int
    total_portfolio: float
    credit_risk_score: float
    product_type: str
    website_url: str
    contacts: List[str]

class Loan(BaseModel):
    generated_for_date: str
    country: str
    loan_originator_id: int
    loan_id: str
    loan_no: str
    loan_type: str
    loan_date: str
    loan_last_date: str
    principal_open: float
    principal_open_eur: float
    status: str
    interest_daily: float
    due_day_of_month: int
    risk_category: str
    currency: str
    exchange_rate: float
    listing_status: str
    loan_url: str
    institution_id: str
