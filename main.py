import tkinter as tk
from tkinter import messagebox
from analyzer import analyze_python_code
import pandas as pd
import os

def analyze_code():
    code = text_input.get("1.0", tk.END)
    if not code.strip():
        messagebox.showwarning("Warning", "Please enter some code.")
        return
    
    feedback = analyze_python_code(code)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, feedback)

    # Save to CSV using pandas
    if not os.path.exists("data"):
        os.makedirs("data")

    df = pd.DataFrame([[code, feedback]], columns=["Code", "Feedback"])
    csv_path = "data/review_history.csv"
    if not os.path.exists(csv_path):
        df.to_csv(csv_path, index=False)
    else:
        df.to_csv(csv_path, mode="a", header=False, index=False)

    messagebox.showinfo("Done", "Code reviewed successfully!")

def clear_all():
    text_input.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("AI-Powered Code Review Assistant")
root.geometry("900x600")
root.config(bg="#f8f9fa")

tk.Label(root, text="Enter your Python code:", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(pady=5)
text_input = tk.Text(root, height=15, width=100, font=("Consolas", 11))
text_input.pack(pady=5)

tk.Button(root, text="Analyze Code", command=analyze_code, bg="#007bff", fg="white", font=("Arial", 11, "bold")).pack(pady=5)
tk.Button(root, text="Clear", command=clear_all, bg="#dc3545", fg="white", font=("Arial", 11, "bold")).pack(pady=5)

tk.Label(root, text="Feedback:", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(pady=5)
output_box = tk.Text(root, height=15, width=100, bg="#e9ecef", font=("Consolas", 10))
output_box.pack(pady=5)

root.mainloop()
