from pydantic import BaseModel, Field
from datetime import datetime


class StockAnalysis(BaseModel):
    ticker: str
    company_name: str
    sector: str
    pe_ratio: float | None = None
    summary: str
    tags: list[str] = Field(default_factory=list)
    related_nodes: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)