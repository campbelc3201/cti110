Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('This program calculates and displays travel expenses')
This program calculates and displays travel expenses
print('04/06/2023')
04/06/2023
print('CTI-110 P1HW1 - Travel Expense')
CTI-110 P1HW1 - Travel Expense
print('Cory Campbell')
Cory Campbell
>>> 
>>> print('Enter budget:', end=' ')
Enter budget: 
>>> budget = int()
>>> 
>>> print('Enter your travel destination:', end=' ')
Enter your travel destination: 
>>> trav_dest = input()

>>> print('How much do you think you will spend on gas?', end=' ')
How much do you think you will spend on gas? 
>>> gas = int()
>>> 
>>> print('Approximately, how much do you think you will need for accomodation/hotel?', end=' ')
Approximately, how much do you think you will need for accomodation/hotel? 
>>> accom = int()
>>> 
>>> print('Last, how much do you need for food?', end=' ')
Last, how much do you need for food? 
>>> food = int()
>>> 
>>> print('------------Travel Expenses------------')
------------Travel Expenses------------
>>> print('Location:', trav_dest)
Location: 
>>> print('Initial Budget:', budget)
Initial Budget: 0
>>> 
>>> print('Fuel:', gas)
Fuel: 0
>>> print('Accomodation:', accom)
Accomodation: 0
>>> print('Food:', food)
Food: 0
>>> 
>>> rem_bal = budget - gas - accom - food
>>> print('Remaining Balance:', rem_bal)
Remaining Balance: 0
