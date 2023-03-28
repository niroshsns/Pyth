salary = 0
tax = 0
salary = float(input("Enter Salary"))
if salary <= 100000:
    tax = 0
elif salary <=141667:
    tax = 0.06
elif salary <=183333:
    tax = 0.12
elif salary <=225000:
    tax = 0.18
elif salary <=266667:
    tax = 0.24
elif salary <=308333:
    tax = 0.30
else:
    tax = 0.36
print("Your Tax: ", tax)
print("Your Amount: ", salary*tax/12)
