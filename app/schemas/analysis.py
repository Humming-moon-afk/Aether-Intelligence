from pydantic import BaseModel, Field
from datetime import datetime


class StockAnalysis(BaseModel):
    ticker: str
    company_name: str
    sector: str