
age=int(input("Enter Age: "))
weight=float(input("Enter Weight IN Kgs: "))
if age < 30:
  index=40
elif age < 56:
  index=35
else: 
  index=30
water=weight*2.20462*index/(2.2*28.3)
print("Water In Litres: ",round(water*0.0295735,1))
print("Water In Cups: ",round(water/8,1))