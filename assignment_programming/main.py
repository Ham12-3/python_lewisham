import tkinter as tk
from tkinter import messagebox

class SupercarExperienceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supercar Experience Days")

        # Header
        self.header_label = tk.Label(self.root, text="Supercar Experience Days", font=("Helvetica", 18, "bold"), pady=10)
        self.header_label.pack()

        # Customer Details Section
        self.customer_frame = tk.LabelFrame(self.root, text="Customer Details", font=("Helvetica", 12, "bold"))
        self.customer_frame.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="both", expand="yes")
        tk.Label(self.customer_frame, text="Customer Name:", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.customer_frame, font=("Helvetica", 10))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.customer_frame, text="Address:", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w")
        self.address_entry = tk.Entry(self.customer_frame, font=("Helvetica", 10))
        self.address_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self.customer_frame, text="Phone Number:", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w")
        self.phone_entry = tk.Entry(self.customer_frame, font=("Helvetica", 10))
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        # Car Selection Section
        self.car_frame = tk.LabelFrame(self.root, text="Car Selection", font=("Helvetica", 12, "bold"))
        self.car_frame.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="both", expand="yes")
        self.car_vars = []
        self.car_choices = ["Car 1", "Car 2", "Car 3", "Car 4", "Car 5"]
        for i, car in enumerate(self.car_choices):
            var = tk.IntVar()
            self.car_vars.append(var)
            tk.Checkbutton(self.car_frame, text=car, variable=var, font=("Helvetica", 10)).grid(row=i, column=0, sticky="w")

        # Additional Laps Section
        self.laps_frame = tk.LabelFrame(self.root, text="Additional Laps", font=("Helvetica", 12, "bold"))
        self.laps_frame.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="both", expand="yes")
        tk.Label(self.laps_frame, text="Number of Laps:", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w")
        self.laps_entry = tk.Entry(self.laps_frame, font=("Helvetica", 10))
        self.laps_entry.grid(row=0, column=1, padx=10, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Generate Bill", font=("Helvetica", 12), command=self.generate_bill)
        self.submit_button.pack(pady=20, padx=20, ipadx=20, ipady=10, fill="both", expand="yes")

    def generate_bill(self):
        # Retrieve customer details
        customer_name = self.name_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_entry.get()

        # Retrieve selected cars
        selected_cars = [self.car_choices[i] for i, var in enumerate(self.car_vars) if var.get() == 1]

        # Retrieve additional laps
        additional_laps = self.laps_entry.get()

        # Validate inputs
        if not customer_name or not address or not phone_number:
            messagebox.showerror("Error", "Please fill in all customer details.")
            return

        if not selected_cars:
            messagebox.showerror("Error", "Please select at least one car.")
            return

        # Calculate total cost
        # Dummy calculation for demonstration
        total_cost = len(selected_cars) * 100  # Dummy cost calculation, replace with actual logic

        # Generate bill
        bill_text = f"Customer Name: {customer_name}\n"
        bill_text += f"Address: {address}\n"
        bill_text += f"Phone Number: {phone_number}\n"
        bill_text += f"Selected Cars: {', '.join(selected_cars)}\n"
        bill_text += f"Additional Laps: {additional_laps}\n"
        bill_text += f"Total Cost: ${total_cost:.2f}"

        # Display bill in message box
        messagebox.showinfo("Bill Generated", bill_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SupercarExperienceApp(root)
    root.mainloop()
