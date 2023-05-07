#CTI-110
#P4HW2 - Salary Calculator
#Cory Campbell
#27 April 2023

#Global variables
numOfEmp = 0               
totalOverTimePay = 0       
totalRegPay = 0            
totalGrossPay = 0          

#Loop
while True:
    
    
    name = input("Enter employee's name or \"Done\" to terminate: ")
    
    
    if name == "Done":
        break
    else:
        
        
        numOfEmp += 1
    
    hours = float(input("How many hours did " + name + " work? "))
    rate = float(input("What is " + name + "\'s pay rate? "))
    
    
    overtime = 0
    overtimePay = 0
    regularPay = 0
    grossPay = 0
    
    
    if hours > 40:
        
        
        overtime = hours - 40
        
        
        overtimePay = overtime * rate * 1.5
        
        
        regularPay = 40*rate
        
        
        grossPay = regularPay + overtimePay
    else:
        
        
        regularPay = hours*rate
        grossPay = regularPay
    
    
    totalOverTimePay += overtimePay
    
    
    totalRegPay += regularPay
    
    
    totalGrossPay += grossPay
    
    #employee name
    print("\nEmployee name: " + name + "\n")
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours, rate, overtime, overtimePay, regularPay, grossPay))
    print()

print()
print("Total number of employees entered:", numOfEmp)
print("Total amount paid for over time: $" + '{:.2f}'.format(totalOverTimePay))
print("Total amount paid for regular hours: $" + '{:.2f}'.format(totalRegPay))
print("Total amount paid in gross: $" + '{:.2f}'.format(totalGrossPay))
