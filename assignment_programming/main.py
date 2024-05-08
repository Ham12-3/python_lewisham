import tkinter as tk
from tkinter import messagebox

class SupercarExperienceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supercar Experience Days")
        
        # Customer Details
        self.customer_frame = tk.Frame(self.root)
        self.customer_frame.pack(pady=10)
        tk.Label(self.customer_frame, text="Customer Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.customer_frame)
        self.name_entry.grid(row=0, column=1)
        # Add more fields for address and phone number
        
        # Car Selection
        self.car_frame = tk.Frame(self.root)
        self.car_frame.pack(pady=10)
        tk.Label(self.car_frame, text="Select Cars:").grid(row=0, column=0, sticky="w")
        self.car_var1 = tk.IntVar()
        self.car_var2 = tk.IntVar()
        # Add more IntVars for each car
        tk.Checkbutton(self.car_frame, text="Car 1", variable=self.car_var1).grid(row=0, column=1, sticky="w")
        tk.Checkbutton(self.car_frame, text="Car 2", variable=self.car_var2).grid(row=1, column=1, sticky="w")
        # Add more Checkbuttons for each car
        
        # Additional Laps
        self.laps_frame = tk.Frame(self.root)
        self.laps_frame.pack(pady=10)
        tk.Label(self.laps_frame, text="Additional Laps:").grid(row=0, column=0, sticky="w")
        self.laps_entry = tk.Entry(self.laps_frame)
        self.laps_entry.grid(row=0, column=1)
        
        # Submit Button
        self.submit_button = tk.Button(self.root, text="Generate Bill", command=self.generate_bill)
        self.submit_button.pack(pady=10)

    def generate_bill(self):
        # Retrieve customer details
        customer_name = self.name_entry.get()
        # Retrieve selected cars
        selected_cars = []
        if self.car_var1.get() == 1:
            selected_cars.append("Car 1")
        if self.car_var2.get() == 1:
            selected_cars.append("Car 2")
        # Retrieve additional laps
        additional_laps = self.laps_entry.get()
        
        # Validate inputs
        if not customer_name:
            messagebox.showerror("Error", "Please enter customer name")
            return
        # Perform further validation if needed
        
        # Calculate total cost
        # Implement your calculation logic here
        
        # Display bill
        bill_message = f"Customer Name: {customer_name}\n"
        bill_message += f"Selected Cars: {', '.join(selected_cars)}\n"
        bill_message += f"Additional Laps: {additional_laps}\n"
        # Add total cost calculation
        messagebox.showinfo("Bill Generated", bill_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = SupercarExperienceApp(root)
    root.mainloop()
