from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List, Optional, Any


@dataclass
class KeyEvent:
    ts: str            # ISO timestamp
    event: str         # "press" or "release"
    key: str           # e.g., "a", "BackSpace", "Return"
    ctrl: bool
    alt: bool
    shift: bool


class TypingAnalyzer:
    """
    Logs key events ONLY from within the app window.
    Computes basic typing stats (safe, consent-based).
    """

    def __init__(self) -> None:
        self.events: List[KeyEvent] = []
        self.started_at: Optional[datetime] = None
        self.ended_at: Optional[datetime] = None

        self.total_key_presses: int = 0
        self.backspaces: int = 0
        self.enters: int = 0
        self.spaces: int = 0

        self.char_freq: Dict[str, int] = {}
        self._buffer: List[str] = []

    @staticmethod
    def _iso_now() -> str:
        return datetime.now().isoformat(timespec="milliseconds")

    def start(self) -> None:
        self.events.clear()
        self.started_at = datetime.now()
        self.ended_at = None

        self.total_key_presses = 0
        self.backspaces = 0
        self.enters = 0
        self.spaces = 0
        self.char_freq.clear()
        self._buffer = []

    def stop(self) -> None:
        self.ended_at = datetime.now()

    def log_event(self, *, event: str, key: str, ctrl: bool, alt: bool, shift: bool) -> None:
        self.events.append(
            KeyEvent(
                ts=self._iso_now(),
                event=event,
                key=key,
                ctrl=ctrl,
                alt=alt,
                shift=shift,
            )
        )

        if event == "press":
            self.total_key_presses += 1

            if key == "BackSpace":
                self.backspaces += 1
                if self._buffer:
                    self._buffer.pop()
            elif key == "Return":
                self.enters += 1
                self._buffer.append("\n")
            elif key == "space":
                self.spaces += 1
                self._buffer.append(" ")
            else:
                if len(key) == 1 and key.isprintable():
                    self.char_freq[key] = self.char_freq.get(key, 0) + 1
                    self._buffer.append(key)

    @property
    def typed_text(self) -> str:
        return "".join(self._buffer)

    def stats(self) -> Dict[str, Any]:
        duration_s: Optional[float] = None
        if self.started_at and self.ended_at:
            duration_s = (self.ended_at - self.started_at).total_seconds()

        net_chars = len(self.typed_text)

        kpm: Optional[float] = None
        if duration_s and duration_s > 0:
            kpm = (self.total_key_presses / duration_s) * 60.0

        return {
            "started_at": self.started_at.isoformat(timespec="seconds") if self.started_at else None,
            "ended_at": self.ended_at.isoformat(timespec="seconds") if self.ended_at else None,
            "duration_seconds": duration_s,
            "total_key_presses": self.total_key_presses,
            "net_characters": net_chars,
            "backspaces": self.backspaces,
            "spaces": self.spaces,
            "enters": self.enters,
            "keys_per_minute": kpm,
            "top_chars": sorted(self.char_freq.items(), key=lambda kv: kv[1], reverse=True)[:10],
            "event_count": len(self.events),
        }

    def export_payload(self) -> Dict[str, Any]:
        return {
            "meta": self.stats(),
            "events": [asdict(e) for e in self.events],
            "typed_text": self.typed_text,
        }