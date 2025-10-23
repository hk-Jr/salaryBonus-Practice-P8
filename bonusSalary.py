
salary = float(input("Enter employee salary: "))
print("Original Salary:", salary)

#10%
bonus_salary = salary + (salary * 0.10)
print("Bonus Added:", bonus_salary)

# 5%
final_salary = bonus_salary - (bonus_salary * 0.05)
print("After Tax Deduction:", final_salary)
