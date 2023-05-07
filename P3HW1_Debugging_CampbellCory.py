print('This program takes a number grade , determines average and displays letter grade for average.')
print('04/20/2023')
print('CTI-110 P3HW1 - Debugging')
print('Cory Campbell')
print()
mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))
print()
print('------------Results------------')
all_scores = [mod1, mod2, mod3, mod4, mod5, mod6]
lowest_grade = min(all_scores)
highest_grade = max(all_scores)
sum_grade = sum(all_scores)
avg_grade = sum_grade / 6
print(f'{"Lowest Grade:":<20}{lowest_grade:<6.1f}')
print(f'{"Highest Grade:":<20}{highest_grade:<6.1f}')
print(f'{"Sum of Grade:":<20}{sum_grade:<6.1f}')
print(f'{"Average:":<20}{avg_grade:<6.2f}')
print('---------------------------------------')
if avg_grade >= 90:
  print('Your grade is: A')
elif avg_grade >= 80:
  print('Your grade is: B')
elif avg_grade >= 70:
  print('Your grade is: C')
elif avg_grade >= 60:
  print('Your grade is: D')
else:
  print('Your grade is: F')
