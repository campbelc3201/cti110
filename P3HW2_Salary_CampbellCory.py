# CTI-110
# P3HW2 - Salary
# Cory Campbell
# 4/20/2023


emp_name = input("Enter employee's name: ")
hours_worked= float(input("Enter number of hours worked: "))
pay_rate= float(input("Enter employee's pay rate: "))

ot_pay = 0.0
over_time = 0.0
if hours_worked > 40:
	over_time = hours_worked - 40
	ot_rate = pay_rate + (pay_rate * 0.5)
	ot_pay = over_time * ot_rate
	reg_pay = 40 * pay_rate
else:
	reg_pay = hours_worked * pay_rate


gross_pay = reg_pay + ot_pay


print("-"*36)
print("Employee name: ",emp_name)
print()
print("Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay")
print("-"*90)
print(hours_worked," \t\t ",pay_rate," \t ",over_time," \t\t ",ot_pay," \t  ",reg_pay," \t ",gross_pay)
