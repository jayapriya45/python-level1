print("JAYAPRIYA INTERNATIONAL LTD")
print("No.15,agra dist,bangolore")
print("-------------------------")
print("Employee payroll system")
print("------------------------")
id=input("Enter the employee id:")
str1=input("Enter the employee name:")
salary=int(input("Enter the salary:"))
print("income")
bonus=salary*20/100
print("Bonus(20 percentage):",bonus)
overtime=salary*10/100
print("Overtime(10 percentagr):",overtime)
travel=salary*5/100
print("Travel allowance(15 percentage):",travel)
grasspay=salary+bonus+overtime+travel
print("Grasspay in rupees:",grasspay)
