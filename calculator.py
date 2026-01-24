import tkinter as tk
from tkinter import messagebox

# Configuration
DENOMINATIONS = [1000, 500, 200, 100, 50, 20, 10]

COLOR_MAP = {
    1000: "#FFD700",
    500: "#FF8C00",
    200: "#FF2F66",
    100: "#FF69BA",
    50: "#ADFF2F",
    20: "#BA55D3",
    10: "#87CEFA",
}

def calculate_denominations():
    try:

        val = entry_amount.get()
        if not val:
            return
            
        amount = int(val)
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        for widget in frame_result.winfo_children():
            widget.destroy()

        remaining = amount
        

        for note in DENOMINATIONS:
            count = remaining // note
            if count > 0:
                lbl = tk.Label(
                    frame_result, 
                    text=f"{note} Taka x {count} = {note * count} Taka", 
                    bg=COLOR_MAP[note], 
                    fg="black", 
                    font=("Arial", 11, "italic"), 
                    width=35
                )
                lbl.pack(pady=3)
                remaining %= note # 

        if remaining > 0:
            tk.Label(
                frame_result, 
                text=f"Remaining: {remaining} Taka (No matching notes)", 
                fg="red", 
                bg="#e6f2ff",
                font=("Arial", 11, "bold")
            ).pack(pady=5)

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e if str(e) else 'Please enter a valid number'}")

root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x550")
root.config(bg="#f0f8ff")

tk.Label(root, text="Taka Denominator", font=("Arial", 16, "bold"), fg="#2f4f4f", bg="#f0f8ff").pack(pady=15)

tk.Label(root, text="Enter Amount in Taka:", font=("Arial", 12), bg="#f0f8ff").pack()
entry_amount = tk.Entry(root, font=("Arial", 12), justify="center")
entry_amount.pack(pady=10)

btn_calculate = tk.Button(
    root, text="Calculate Notes", font=("Arial", 12, "bold"), 
    bg="#4682b4", fg="white", command=calculate_denominations
)
btn_calculate.pack(pady=10)

# The frame where color-coded labels will appear
frame_result = tk.Frame(root, bg="#e6f2ff", bd=2, relief="ridge")
frame_result.pack(pady=10, fill="both", expand=True, padx=20)

root.mainloop()