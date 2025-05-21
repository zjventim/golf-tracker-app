import tkinter as tk
from tkinter import messagebox
from db import get_connection
from handicap import calculate_handicap

def submit_score():
    try:
        score = int(score_entry.get())
        rating = float(rating_entry.get())
        slope = int(slope_entry.get())
        handicap = calculate_handicap(score, rating, slope)
        messagebox.showinfo("Handicap", f"Your handicap differential is: {handicap}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def run_ui():
    global score_entry, rating_entry, slope_entry

    root = tk.Tk()
    root.title("Golf Tracker")

    tk.Label(root, text="Score:").pack()
    score_entry = tk.Entry(root)
    score_entry.pack()

    tk.Label(root, text="Course Rating:").pack()
    rating_entry = tk.Entry(root)
    rating_entry.pack()

    tk.Label(root, text="Slope Rating:").pack()
    slope_entry = tk.Entry(root)
    slope_entry.pack()

    tk.Button(root, text="Submit", command=submit_score).pack()

    root.mainloop()
