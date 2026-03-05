from __future__ import annotations
import json
import csv
from pathlib import Path
from typing import Any, Dict


def export_json(payload: Dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def export_csv_events(payload: Dict[str, Any], path: str | Path) -> None:
    events = payload.get("events", [])
    path = Path(path)

    fieldnames = ["ts", "event", "key", "ctrl", "alt", "shift"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in events:
            w.writerow({k: row.get(k) for k in fieldnames})