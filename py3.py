print("GOVERNMENT OF TAMILNADU")
print("Electricity Boad")
print("----------------------")
str1=input("Enter the EB no:")
str2=input("Enter the custamer name:")
previous=int(input("Reading of previous month:"))
current=int(input("Reading for current month:"))
total=current-previous
print("total unit consumed:",total)
paid=total*5
print("Amount to be paid:",paid)
