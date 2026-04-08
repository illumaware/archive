from datetime import datetime

def days_until(date_str):
    try:
        target = datetime.strptime(date_str, "%d/%m/%Y").date()
        diff = (target - datetime.now().date()).days
        print(f"{diff} days left\n")
    except ValueError:
        print("Wrong format, use dd/mm/yyyy\n")

while True:
    user_input = input("Enter a date (dd/mm/yyyy) [c to exit]: ")
    if user_input.lower() == "c":
        break
    days_until(user_input)

input("Press Enter to close...")
