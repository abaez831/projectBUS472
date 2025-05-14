from tkinter import *  # Import everything from the Tkinter library
import datetime  # Import the datetime module for date calculations
import calendar  # Import calendar to handle month name conversion

root = Tk()  # Create the main application window
root.title("Age Calculator")  # Set the window title
root.geometry("400x250")  # Increased window size for better spacing


# Function to convert month names to numbers
def convert_month(month_input):
    try:
        # Check if the input is a number (valid month)
        if month_input.isdigit():
            month = int(month_input)
        else:
            # Convert full or abbreviated month names to numbers
            month = list(calendar.month_name).index(month_input.capitalize())
            if month == 0:
                raise ValueError  # Handle invalid month names
        return month
    except ValueError:
        return None  # Return None if the input is invalid


# Function to calculate the age
def calculateage():
    try:
        birth_year = int(YearVariable.get())
        birth_month = convert_month(MonthVariable.get())  # Convert month input
        birth_day = int(DayVariable.get())

        # Validate inputs
        if birth_month is None or not (1 <= birth_month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= birth_day <= 31):
            raise ValueError("Invalid day")

        birthdate = datetime.datetime(birth_year, birth_month, birth_day)
        age = datetime.datetime.now() - birthdate
        convertdays = int(age.days)
        ageyears = round(convertdays / 365, 2)

        result_label.config(text=f"{NameVariable.get()}, your age is {ageyears}", fg='blue')
    except ValueError:
        result_label.config(text="Please enter valid numeric values!", fg='red')


# Labels and Entry Fields
Label(root, text="Your Name").grid(row=1, column=1, padx=90)
Label(root, text="Year").grid(row=2, column=1, padx=90)
Label(root, text="Month").grid(row=3, column=1, padx=90)
Label(root, text="Day").grid(row=4, column=1, padx=90)

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()
Entry(root, textvariable=NameVariable).grid(row=1, column=2)
Entry(root, textvariable=YearVariable).grid(row=2, column=2)
Entry(root, textvariable=MonthVariable).grid(row=3, column=2)
Entry(root, textvariable=DayVariable).grid(row=4, column=2)

# Submit button to calculate age
button1 = Button(root, text="Submit", command=calculateage)
button1.grid(row=5, column=1)

# Label to display results dynamically
result_label = Label(root, text="", fg="black")  # Initially empty
result_label.grid(row=6, column=1, columnspan=2)

root.mainloop()  # Run the Tkinter event loop
