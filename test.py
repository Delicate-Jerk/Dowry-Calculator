import tkinter as tk
from tkinter import messagebox

def calculate_worth():
    income = int(income_entry.get())
    profession = profession_var.get()
    employment_status = employment_var.get()
    location = location_var.get()

    profession_weights = {
        "engineer": 0.3,
        "doctor": 0.4,
        "businessman": 0.5,
        "unemployed": 0.1
    }

    employment_weights = {
        "employed": 0.2,
        "unemployed": 0.1
    }

    location_weights = {
        "India": 0.2,
        "USA": 0.4,
        "Australia": 0.3,
        # Add more locations and weights as needed
    }

    profession_worth = profession_weights.get(profession, 0)
    employment_worth = employment_weights.get(employment_status, 0)
    location_worth = location_weights.get(location, 0)

    total_worth = (
        0.2 * profession_worth +
        0.2 * employment_worth +
        0.2 * location_worth
    )

    if profession == "doctor":
        total_worth += 400000
    elif profession == "engineer":
        total_worth += 300000
    elif profession == "unemployed":
        total_worth += 100000

    final_worth = total_worth + income * 10
    messagebox.showinfo("Result", f"Your calculated worth in rupees: {final_worth}")

# Create GUI window
root = tk.Tk()
root.title("Worth Calculator")

# Labels and Entries
income_label = tk.Label(root, text="Monthly Income (in rupees):")
income_label.pack()

income_entry = tk.Entry(root)
income_entry.pack()

profession_label = tk.Label(root, text="Profession:")
profession_label.pack()

profession_var = tk.StringVar()
profession_var.set("engineer")  # Default value
profession_option_menu = tk.OptionMenu(root, profession_var, "engineer", "doctor", "businessman", "unemployed")
profession_option_menu.pack()

employment_label = tk.Label(root, text="Employment Status:")
employment_label.pack()

employment_var = tk.StringVar()
employment_var.set("employed")  # Default value
employment_option_menu = tk.OptionMenu(root, employment_var, "employed", "unemployed")
employment_option_menu.pack()

location_label = tk.Label(root, text="Location:")
location_label.pack()

location_var = tk.StringVar()
location_var.set("India")  # Default value
location_option_menu = tk.OptionMenu(root, location_var, "India", "USA", "Australia")
location_option_menu.pack()

calculate_button = tk.Button(root, text="Calculate Worth", command=calculate_worth)
calculate_button.pack()

root.mainloop()
