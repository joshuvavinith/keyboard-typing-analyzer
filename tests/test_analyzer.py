import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from analyzer import TypingAnalyzer


def test_analyzer_initial_state():
    analyzer = TypingAnalyzer()
    stats = analyzer.stats()

    assert stats["total_key_presses"] == 0
    assert stats["net_characters"] == 0
    assert stats["backspaces"] == 0