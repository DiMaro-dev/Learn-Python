# Age Calculator, from date of birth to current age
# This program calculates the age of a person based on their date of birth.
from datetime import datetime

birth_input = input("Enter your date of birth (YYYY-MM-DD): ") # input date in YYYY-MM-DD format

try:
    # Convert input string to datetime object
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d")
    now = datetime.now()

    # Calculate the difference between now and birth_date
    if birth_date > now:
        print("Birth date cannot be in the future.")
        exit()
    
    diff = now - birth_date

    # Calculate age in years
    age_years = now.year - birth_date.year
    if (now.month, now.day) < (birth_date.month, birth_date.day):
        age_years -= 1

    # Calculate months difference
    # This is a rough estimate, not accounting for exact month lengths
    months_diff = (now.year - birth_date.year) * 12 + (now.month - birth_date.month)
    if now.day < birth_date.day:
        months_diff -= 1

    # Dettagli precisi
    total_days = diff.days
    total_seconds = diff.total_seconds()
    total_minutes = total_seconds // 60
    total_hours = total_minutes // 60

    print("\nYour current age is approximately:")
    print(f"Years: {age_years}")
    print(f"Months (approx): {months_diff}")
    print(f"Days: {total_days}")
    print(f"Hours: {int(total_hours)}")
    print(f"Minutes: {int(total_minutes)}")
    print(f"Seconds: {int(total_seconds)}")

except ValueError:
    print("Invalid format. Please use YYYY-MM-DD")
