from pydantic import BaseModel
from typing import List
from typing import Optional

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
    generated_for_date: Optional[str] = None
    country: Optional[str] = None
    loan_originator_id: Optional[int] = None
    loan_id: str
    loan_no: str
    loan_type: str
    loan_date: str
    loan_last_date: str
    principal_open: float
    principal_open_eur: float
    status: str
    interest_daily: Optional[float] = None
    due_day_of_month: Optional[int] = None
    risk_category: Optional[str] = None
    currency: Optional[str] = None
    exchange_rate: Optional[float] = None
    listing_status: Optional[str] = None
    loan_url: str
    institution_id: str
