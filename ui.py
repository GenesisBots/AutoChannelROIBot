import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from pathlib import Path

import bot
import strategy_engine as se

ROOT = Path(__file__).parent


def open_folder(path: Path):
    path.mkdir(exist_ok=True)
    if sys.platform.startswith("win"):
        os.startfile(str(path))
    elif sys.platform == "darwin":
        os.system(f"open '{path}'")
    else:
        os.system(f"xdg-open '{path}'")


def show_main_window():
    app = tk.Tk()
    app.title("AutoChannelROIbot — The Genesis System")
    app.configure(bg="#05060a")
    app.geometry("720x520")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

    title = tk.Label(
        app,
        text="AutoChannelROIbot",
        font=("Segoe UI", 18, "bold"),
        fg="#00e0ff",
        bg="#05060a"
    )
    title.grid(row=0, column=0, pady=(20, 4))

    subtitle = tk.Label(
        app,
        text="A calm, strategic ROI assistant for YouTube creators",
        font=("Segoe UI", 10),
        fg="#9fa4b8",
        bg="#05060a"
    )
    subtitle.grid(row=1, column=0, pady=(0, 10))

    main_frame = tk.Frame(app, bg="#05060a")
    main_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    main_frame.columnconfigure(0, weight=0)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)

    # Left panel: profile inputs + action buttons
    left = tk.Frame(main_frame, bg="#05060a")
    left.grid(row=0, column=0, sticky="ns", padx=(0, 10))

    def add_field(parent, label, default):
        frame = tk.Frame(parent, bg="#05060a")
        frame.pack(pady=6, anchor="w")

        tk.Label(
            frame,
            text=label,
            font=("Segoe UI", 10, "bold"),
            fg="#4cf2ff",
            bg="#05060a"
        ).pack(anchor="w")

        entry = tk.Entry(
            frame,
            width=32,
            bg="#151722",
            fg="#e5e7f0",
            insertbackground="#e5e7f0",
            relief="flat"
        )
        entry.insert(0, default)
        entry.pack()
        return entry

    niche = add_field(left, "Channel Niche:", "AI Dogs / Travel / Motivation")
    goals = add_field(left, "Main Goal:", "More views, more subs, better retention")
    cadence = add_field(left, "Videos per Week:", "3")
    pain = add_field(left, "Biggest Struggle:", "Consistency and packaging")

    btn_style = {
        "font": ("Segoe UI", 10, "bold"),
        "fg": "#05060a",
        "bg": "#00e0ff",
        "activebackground": "#00b0c8",
        "activeforeground": "#05060a",
        "relief": "flat",
        "width": 28,
        "height": 1,
        "cursor": "hand2",
        "anchor": "center",
        "padx": 4,
        "pady": 2,
    }

    tk.Label(
        left,
        text="Profile & Actions",
        font=("Segoe UI", 10, "bold"),
        fg="#9fa4b8",
        bg="#05060a"
    ).pack(pady=(10, 4), anchor="w")

    def on_save_profile():
        try:
            bot.run_bot_interactive(
                niche.get(),
                goals.get(),
                cadence.get(),
                pain.get()
            )
            messagebox.showinfo(
                "Profile Saved",
                "Channel profile saved to channel_profile.json"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Could not save profile.\n\n{e}")

    tk.Button(left, text="Save / Update Channel Profile", command=on_save_profile, **btn_style).pack(pady=4)

    tk.Label(
        left,
        text="Strategy & Tools",
        font=("Segoe UI", 10, "bold"),
        fg="#9fa4b8",
        bg="#05060a"
    ).pack(pady=(12, 4), anchor="w")

    # Right panel: output console
    right = tk.Frame(main_frame, bg="#05060a")
    right.grid(row=0, column=1, sticky="nsew")
    right.rowconfigure(0, weight=1)
    right.columnconfigure(0, weight=1)

    output = tk.Text(
        right,
        bg="#0b0d14",
        fg="#e5e7f0",
        insertbackground="#e5e7f0",
        relief="flat",
        wrap="word"
    )
    output.grid(row=0, column=0, sticky="nsew")

    scrollbar = tk.Scrollbar(right, command=output.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    output.config(yscrollcommand=scrollbar.set)

    def set_output(text):
        output.delete("1.0", tk.END)
        output.insert(tk.END, text)

    # Button handlers using strategy_engine
    def on_niche_breakdown():
        res = se.niche_breakdown()
        set_output(res)

    def on_weekly_plan():
        res = se.weekly_plan()
        set_output(res)

    def on_optimize_title():
        title = simpledialog.askstring("Optimize Title", "Enter your current title:")
        if not title:
            return
        res = se.optimize_title(title)
        set_output(res)

    def on_optimize_description():
        desc = simpledialog.askstring("Optimize Description", "Paste your current description:")
        if not desc:
            return
        res = se.optimize_description(desc)
        set_output(res)

    def on_analyze_stats():
        stats = simpledialog.askstring("Analyze Stats", "Paste your recent stats or notes:")
        if not stats:
            return
        res = se.analyze_stats(stats)
        set_output(res)

    def on_promotion_tools():
        res = se.promotion_scripts()
        set_output(res)

    tk.Button(left, text="Niche Breakdown", command=on_niche_breakdown, **btn_style).pack(pady=3)
    tk.Button(left, text="Generate Weekly Plan", command=on_weekly_plan, **btn_style).pack(pady=3)
    tk.Button(left, text="Optimize Title", command=on_optimize_title, **btn_style).pack(pady=3)
    tk.Button(left, text="Optimize Description", command=on_optimize_description, **btn_style).pack(pady=3)
    tk.Button(left, text="Analyze Stats", command=on_analyze_stats, **btn_style).pack(pady=3)
    tk.Button(left, text="Promotion Tools", command=on_promotion_tools, **btn_style).pack(pady=3)

    tk.Button(left, text="Open Bot Folder", command=lambda: open_folder(ROOT), **btn_style).pack(pady=(10, 3))

    footer = tk.Label(
        app,
        text="The Genesis System — Creator Edition",
        font=("Segoe UI", 9),
        fg="#5b6070",
        bg="#05060a"
    )
    footer.grid(row=3, column=0, pady=(4, 10))

    app.mainloop()


def show_hud_then_main():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.configure(bg="#05060a")

    w, h = 520, 260
    sw = splash.winfo_screenwidth()
    sh = splash.winfo_screenheight()
    x = int((sw - w) / 2)
    y = int((sh - h) / 2)
    splash.geometry(f"{w}x{h}+{x}+{y}")

    title = tk.Label(
        splash,
        text="THE GENESIS SYSTEM",
        font=("Segoe UI", 18, "bold"),
        fg="#00e0ff",
        bg="#05060a"
    )
    title.pack(pady=(40, 4))

    subtitle = tk.Label(
        splash,
        text="AutoChannelROIbot",
        font=("Segoe UI", 13),
        fg="#c3c7d6",
        bg="#05060a"
    )
    subtitle.pack(pady=(0, 10))

    tagline = tk.Label(
        splash,
        text="A calm, strategic HUD for multi‑niche YouTube growth.",
        font=("Segoe UI", 10),
        fg="#8b90a0",
        bg="#05060a"
    )
    tagline.pack(pady=(0, 20))

    loading = tk.Label(
        splash,
        text="Initializing Creator ROI HUD...",
        font=("Segoe UI", 9),
        fg="#00e0ff",
        bg="#05060a"
    )
    loading.pack(pady=(0, 10))

    def transition():
        splash.destroy()
        show_main_window()

    splash.after(2000, transition)
    splash.mainloop()


if __name__ == "__main__":
    show_hud_then_main()
