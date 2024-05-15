import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        self.style = Style(theme="cyborg")
        self.style.master = root

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill="both", padx=100, pady=100)

        self.label_username = ttk.Label(self.frame, text="Username:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_username.pack(pady=10)
        self.entry_username = ttk.Entry(self.frame, width=50, style="primary.TEntry")
        self.entry_username.pack(pady=10)

        self.label_password = ttk.Label(self.frame, text="Password:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_password.pack(pady=10)
        self.entry_password = ttk.Entry(self.frame, show="*", width=50, style="primary.TEntry")
        self.entry_password.pack(pady=10)

        self.btn_login = ttk.Button(self.frame, text="Login", command=self.login, style="primary.TButton", width=50)
        self.btn_login.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "admin":
            self.open_main_screen()
        else:
            self.show_error_message("Invalid username or password")

    def open_main_screen(self):
        self.root.withdraw()  # Hide login window
        self.main_screen = tk.Toplevel(self.root)
        self.main_screen.geometry("800x800")
        app = SupercarExperienceApp(self.main_screen)

    def show_error_message(self, message):
        ttk.messagebox.showerror("Error", message)

class SupercarExperienceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supercar Experience Calculator")
        
        self.style = Style(theme="cyborg")
        self.style.master = root

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill="both", padx=100, pady=100)

        self.label_name = ttk.Label(self.frame, text="Customer Name:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_name.pack(pady=10)
        self.entry_name = ttk.Entry(self.frame, width=50, style="primary.TEntry")
        self.entry_name.pack(pady=10)

        self.label_address = ttk.Label(self.frame, text="Address:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_address.pack(pady=10)
        self.entry_address = ttk.Entry(self.frame, width=50, style="primary.TEntry")
        self.entry_address.pack(pady=10)

        self.label_phone = ttk.Label(self.frame, text="Phone Number:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_phone.pack(pady=10)
        self.entry_phone = ttk.Entry(self.frame, width=50, style="primary.TEntry")
        self.entry_phone.pack(pady=10)

        self.label_cars = ttk.Label(self.frame, text="Number of Cars:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_cars.pack(pady=10)
        self.spin_cars = ttk.Spinbox(self.frame, from_=1, to=5, width=50, style="primary.TSpinbox")
        self.spin_cars.pack(pady=10)

        self.label_car_choices = ttk.Label(self.frame, text="Car Choices:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_car_choices.pack(pady=10)
        self.entry_car_choices = ttk.Entry(self.frame, width=50, style="primary.TEntry")
        self.entry_car_choices.pack(pady=10)

        self.label_extra_laps = ttk.Label(self.frame, text="Additional Laps:", font=("Helvetica", 19), style="primary.TLabel")
        self.label_extra_laps.pack(pady=10)
        self.spin_extra_laps = ttk.Spinbox(self.frame, from_=0, to=100, width=50, style="primary.TSpinbox")
        self.spin_extra_laps.pack(pady=10)

        self.btn_calculate = ttk.Button(self.frame, text="Calculate Cost", command=self.calculate_cost, style="primary.TButton", width=50)
        self.btn_calculate.pack(pady=20)

    def calculate_cost(self):
        name = self.entry_name.get()
        address = self.entry_address.get()
        phone = self.entry_phone.get()
        num_cars = int(self.spin_cars.get())
        car_choices = self.entry_car_choices.get()
        extra_laps = int(self.spin_extra_laps.get())

        base_cost_per_car = 500
        extra_laps_cost = 50
        total_cost = base_cost_per_car * num_cars + extra_laps_cost * extra_laps

        self.display_result(name, address, phone, num_cars, car_choices, extra_laps, total_cost)

    def display_result(self, name, address, phone, num_cars, car_choices, extra_laps, total_cost):
        for widget in self.frame.winfo_children():
            widget.destroy()

        result_text = f"Customer Details:\nName: {name}\nAddress: {address}\nPhone: {phone}\n\n"
        result_text += f"Number of Cars: {num_cars}\nCar Choices: {car_choices}\n"
        result_text += f"Additional Laps: {extra_laps}\n\nTotal Cost: £{total_cost:.2f}"

        self.label_result = ttk.Label(self.frame, text="Receipt", font=("Helvetica", 22, "bold"), style="primary.TLabel")
        self.label_result.pack(pady=10)

        self.text_receipt = tk.Text(self.frame, height=10, width=60, font=("Helvetica", 16))
        self.text_receipt.insert(tk.END, result_text)
        self.text_receipt.config(state=tk.DISABLED)
        self.text_receipt.pack(pady=10)

        self.meter = ttk.Meter(
            self.frame,
            metersize=180,
            padding=5,
            amountused=min(total_cost / 100, 100),  # Assuming a max value of $10,000 for the meter
            metertype="semi",
            subtext="Total Cost",
            interactive=False,
        )
        self.meter.pack(pady=20)

        self.gauge = ttk.Floodgauge(
            self.frame,
            bootstyle=INFO,
            font=(None, 24, 'bold'),
            mask='Cost: £{}%',
            value=min(total_cost / 100, 100)
        )
        self.gauge.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

        self.btn_back = ttk.Button(self.frame, text="Back", command=self.create_widgets, style="primary.TButton", width=50)
        self.btn_back.pack(pady=20)

def main():
    root = tk.Tk()
    root.geometry("800x800")
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
