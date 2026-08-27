from pathlib import Path
from app.schemas.analysis import StockAnalysis

data = StockAnalysis(ticker="NVDA",company_name="Nvidia Corporation", 
                     sector="Halbleiter",pe_ratio=32.5,
                     summary="Führender Entwickler von Grafikprozessoren und KI-Beschleunigern für Rechenzentren.",
                     tags=["aktie", "ki", "tech"],
                     related_nodes=["KI-Infrastruktur", "Rechenzentren", "TSMC"])
vaultPath = Path.home()/"Desktop"/"Aether"/"Aether-Intelligence"/f"{data.ticker}.md"
links_str = ", ".join([f"[[{node}]]" for node in data.related_nodes])
content=f"""---
ticker: {data.ticker}
name: {data.company_name}
sector: {data.sector}
pe_ratio: {data.pe_ratio}
tags: {data.tags}
created_at: {data.created_at}
---

## Vernetzte Themen
{links_str}
## Zusammenfassung 
{data.summary}
"""


target_file = vaultPath.write_text(content, encoding="utf-8")