print("JAYAPRIYA SUPERMARKET")
print("no.44,middle street,pondycherry")
print("---------------------------")
print("Bill number")
print("--------------------------")
str1=int(input("Enter the serial number:"))
particulars=input(" Enter the particulars:")
rate=int(input("Enter the rate:"))
quantity=int(input("Enter the quantity:"))
total=rate*quantity
print("Total :",total)
gst=total *10/100
print("GST(10%):",gst)
paid=total+gst
print("Amount to be paid:",paid)
