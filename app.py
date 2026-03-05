from __future__ import annotations
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

from analyzer import TypingAnalyzer
from export_utils import export_json, export_csv_events


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Typing Analyzer (In-App Key Events Only)")
        self.geometry("760x520")

        self.analyzer = TypingAnalyzer()
        self.is_running = False

        self._build_ui()
        self._bind_keys()

    def _build_ui(self) -> None:
        top = ttk.Frame(self, padding=12)
        top.pack(fill="both", expand=True)

        header = ttk.Label(
            top,
            text="Typing Analyzer (safe: captures keys ONLY in this window)",
            font=("Segoe UI", 14, "bold"),
        )
        header.pack(anchor="w")

        self.disclaimer_var = tk.BooleanVar(value=False)
        disclaimer = ttk.Checkbutton(
            top,
            text="I understand this records my keystrokes only inside this app window (consent).",
            variable=self.disclaimer_var,
        )
        disclaimer.pack(anchor="w", pady=(8, 10))

        controls = ttk.Frame(top)
        controls.pack(fill="x", pady=(0, 10))

        self.start_btn = ttk.Button(controls, text="Start", command=self.start)
        self.start_btn.pack(side="left")

        self.stop_btn = ttk.Button(controls, text="Stop", command=self.stop, state="disabled")
        self.stop_btn.pack(side="left", padx=(8, 0))

        self.export_json_btn = ttk.Button(controls, text="Export JSON", command=self.save_json, state="disabled")
        self.export_json_btn.pack(side="right")

        self.export_csv_btn = ttk.Button(controls, text="Export CSV (events)", command=self.save_csv, state="disabled")
        self.export_csv_btn.pack(side="right", padx=(0, 8))

        paned = ttk.Panedwindow(top, orient="horizontal")
        paned.pack(fill="both", expand=True)

        left = ttk.Frame(paned, padding=(0, 0, 8, 0))
        right = ttk.Frame(paned)
        paned.add(left, weight=3)
        paned.add(right, weight=2)

        ttk.Label(left, text="Type here:").pack(anchor="w")
        self.text = tk.Text(left, height=16, wrap="word")
        self.text.pack(fill="both", expand=True, pady=(4, 0))

        ttk.Label(right, text="Live stats:").pack(anchor="w")
        self.stats_box = tk.Text(right, height=16, wrap="word", state="disabled")
        self.stats_box.pack(fill="both", expand=True, pady=(4, 0))

        footer = ttk.Label(
            top,
            text="Portfolio-safe: no global/background capture.",
            foreground="#555",
        )
        footer.pack(anchor="w", pady=(10, 0))

    def _bind_keys(self) -> None:
        self.text.bind("<KeyPress>", self._on_key_press, add=True)
        self.text.bind("<KeyRelease>", self._on_key_release, add=True)

    def _mods(self, event: tk.Event) -> tuple[bool, bool, bool]:
        state = int(getattr(event, "state", 0))
        shift = bool(state & 0x0001)
        ctrl = bool(state & 0x0004)
        alt = bool(state & 0x0008)
        return ctrl, alt, shift

    def _tk_key_name(self, event: tk.Event) -> str:
        return str(getattr(event, "keysym", "")) or str(getattr(event, "char", ""))

    def _on_key_press(self, event: tk.Event) -> None:
        if not self.is_running:
            return
        ctrl, alt, shift = self._mods(event)
        key = self._tk_key_name(event)
        self.analyzer.log_event(event="press", key=key, ctrl=ctrl, alt=alt, shift=shift)
        self._render_stats()

    def _on_key_release(self, event: tk.Event) -> None:
        if not self.is_running:
            return
        ctrl, alt, shift = self._mods(event)
        key = self._tk_key_name(event)
        self.analyzer.log_event(event="release", key=key, ctrl=ctrl, alt=alt, shift=shift)

    def _render_stats(self) -> None:
        stats = self.analyzer.stats()
        lines = [
            f"Running: {self.is_running}",
            f"Total key presses: {stats['total_key_presses']}",
            f"Net characters: {stats['net_characters']}",
            f"Backspaces: {stats['backspaces']}",
            f"Spaces: {stats['spaces']}",
            f"Enters: {stats['enters']}",
            f"Keys/min: {stats['keys_per_minute']:.2f}" if stats["keys_per_minute"] else "Keys/min: -",
            "",
            "Top chars:",
        ]
        for ch, n in stats["top_chars"]:
            lines.append(f"  {repr(ch)} : {n}")

        self.stats_box.configure(state="normal")
        self.stats_box.delete("1.0", "end")
        self.stats_box.insert("1.0", "\n".join(lines))
        self.stats_box.configure(state="disabled")

    def start(self) -> None:
        if not self.disclaimer_var.get():
            messagebox.showwarning("Consent required", "Please check the consent box before starting.")
            return

        self.analyzer.start()
        self.is_running = True

        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.export_json_btn.configure(state="disabled")
        self.export_csv_btn.configure(state="disabled")

        self.text.focus_set()
        self._render_stats()

    def stop(self) -> None:
        if not self.is_running:
            return

        self.analyzer.stop()
        self.is_running = False

        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.export_json_btn.configure(state="normal")
        self.export_csv_btn.configure(state="normal")

        self._render_stats()

    def save_json(self) -> None:
        payload = self.analyzer.export_payload()
        default = Path.cwd() / "typing_session.json"
        path = filedialog.asksaveasfilename(
            title="Save JSON",
            defaultextension=".json",
            initialfile=default.name,
            filetypes=[("JSON", "*.json")],
        )
        if not path:
            return
        export_json(payload, path)
        messagebox.showinfo("Saved", f"Exported JSON to:\n{path}")

    def save_csv(self) -> None:
        payload = self.analyzer.export_payload()
        default = Path.cwd() / "typing_events.csv"
        path = filedialog.asksaveasfilename(
            title="Save CSV",
            defaultextension=".csv",
            initialfile=default.name,
            filetypes=[("CSV", "*.csv")],
        )
        if not path:
            return
        export_csv_events(payload, path)
        messagebox.showinfo("Saved", f"Exported CSV to:\n{path}")


if __name__ == "__main__":
    App().mainloop()