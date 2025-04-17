#Question 1
#a)defining an function that calculates employees net salaries
inputhourly_rate = input()
inputhours_worked = input()
def calculate_salary (hourly_rate,hours_worked,tax_rate=0.15):
    """This function calculates the net salary of an employee by multiplying the
hourly rate of work by the hours worked then it returms this amount after tax deduction"""
    hourly_rate = input("Enter hourly rate:")
    hours_worked = input("Enter hours worked:")
    gross_salary = hourly_rate * hours_worked
    tax_cut = gross_salary  * tax_rate
    return f"Net Salary:{tax_cut}"
    
#b)code that accepts user input
hourly_rate = int(input("Enter hourly rate:"))
hours_worked = int(input("Enter hours worked:"))
print(calculate_salary(hourly_rate,hours_worked))

