from pathlib import Path

nvdaFile = "NVDA.md"
obsidianFile_path = Path.home()/"Desktop"/"Aether"/"Aether-Intelligence"/nvdaFile

content ="""
---
ticker: "NVDA"
sector: "Halbleiter"
tags: [aktie, ki]
---
Branche: [[Halbleiter]] | Fokus: [[KI-Infrastruktur]]
"""

obsidianFile_path.write_text(content,encoding="utf-8")