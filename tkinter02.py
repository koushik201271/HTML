import tkinter as tk 
from tkinter import ttk, messagebox 

def submit_form():
    # Fixed variable names from .ver to _var
    name = name_var.get().strip()
    age = age_var.get().strip()

    if not name:
        messagebox.showerror("Validation Error", "Name is required")
        return
    
    if not age.isdigit():
        messagebox.showerror("Validation Error", "Age must be numeric")
        return
    
    languages = []
    if python_var.get():
        languages.append("Python")
    
    if java_var.get():
        languages.append("Java")

    if js_var.get():
        languages.append("JavaScript")

    # Fixed syntax: gander_var -> gender_var and used () instead of {}
    info = (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Gender: {gender_var.get()}\n"
        f"Languages: {', '.join(languages) if languages else 'None'}\n"
        f"Country: {country_var.get() or 'Not selected'}"
    )

    messagebox.showinfo("Submitted Information", info)


def clear_form():
    # Fixed function name and variable references
    name_var.set("")
    age_var.set("")
    gender_var.set("Not Specified")
    python_var.set(False)
    java_var.set(False)
    js_var.set(False)
    country_var.set("")

root = tk.Tk()
root.title("User Information Form")
root.geometry("420x450") # Slightly increased height to prevent cutoff
root.resizable(False, False)

style = ttk.Style()
style.theme_use("default")

style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TEntry", padding=4)
style.configure("TButton", padding=6)
style.configure("TLabelframe", padding=10)
style.configure("TLabelframe.Label", font=("Segoe UI", 10, "bold"))

# Fixed typo: 'both' needs to be the string "both" or tk.BOTH
container = ttk.Frame(root, padding=20)
container.pack(fill="both", expand=True)

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar(value="Not Specified")
country_var = tk.StringVar()

ttk.Label(container, text="Name:", width=15, anchor="e").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(container, textvariable=name_var, width=30).grid(row=0, column=1)

ttk.Label(container, text="Age:", width=15, anchor="e").grid(row=1, column=0, padx=5, pady=5)
ttk.Entry(container, textvariable=age_var, width=30).grid(row=1, column=1)

gender_frame = ttk.Labelframe(container, text="Gender")
gender_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=12)

# Fixed grid positioning (columns were overlapping)
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").grid(row=0, column=0, padx=10)
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").grid(row=0, column=1, padx=10)
ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").grid(row=0, column=2, padx=10)

lang_frame = ttk.Labelframe(container, text="Languages Known")
lang_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=12)

# Fixed typo: pyton_var -> python_var
python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
js_var = tk.BooleanVar()

ttk.Checkbutton(lang_frame, text="Python", variable=python_var).grid(row=0, column=0, padx=10)
ttk.Checkbutton(lang_frame, text="Java", variable=java_var).grid(row=0, column=1, padx=10)
ttk.Checkbutton(lang_frame, text="JavaScript", variable=js_var).grid(row=0, column=2, padx=10)

ttk.Label(container, text="Country:", width=15, anchor="e").grid(row=4, column=0, padx=5, pady=6)
ttk.Combobox(
    container,
    textvariable=country_var,
    values=["USA", "Canada", "UK", "Australia", "Other"],
    state="readonly",
    width=28
).grid(row=4, column=1)

button_frame = ttk.Frame(container)
button_frame.grid(row=5, column=0, columnspan=2, pady=20)

ttk.Button(button_frame, text="Submit", width=14, command=submit_form).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Clear", width=14, command=clear_form).grid(row=0, column=1, padx=10)

root.mainloop()