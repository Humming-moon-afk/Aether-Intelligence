from pathlib import Path
from app.schemas.analysis import StockAnalysis


class VaultWriter:
    def __init__(self, vault_path: Path):
        self.vault_path = vault_path
        self.vault_path.mkdir(parents=True, exist_ok=True)

    def _build_markdown(self, data: StockAnalysis) -> str:
        links_str = ", ".join(f"[[{node}]]" for node in data.related_nodes)
        content = f"""---
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
        return content
    def save_analysis(self, data: StockAnalysis) -> str:
        content = self._build_markdown(data)
        target_file = self.vault_path/f"{data.ticker}.md"
        target_file.write_text(content, encoding="utf-8")
        return target_file


if __name__ == "__main__":
    vault = Path.home()/"Desktop"/"Aether"/"Aether-Intelligence"
    writer = VaultWriter(vault_path=vault)
    data = StockAnalysis(
        ticker="NVSA",
        company_name="Nvidia Corporation",
        sector="Halbleiter",
        pe_ratio=32.5,
        summary="Führender Entwickler von Grafikprozessoren und KI-Beschleunigern für Rechenzentren.",
        tags=["aktie", "ki", "tech"],
        related_nodes=["KI-Infrastruktur", "Rechenzentren", "TSMC"],
    )
    saved = writer.save_analysis(data)
    print(f"Erfolgreich gespeichert unter: {saved}")