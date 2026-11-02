def calculate_bill(units):
    bill=0
    if(units<=100):
        bill=units*1.5
    elif(units<=200):
         bill=100*1.5+(units-100)*2.5
    elif(units<=500):
        bill=(100*1.5)+(100*2.5)+(units-200)*4.0
    else:
        bill=(100*1.5)+(100*2.50)+(300*4.0)+(units-500)*6.0
    return bill
n=int(input("enter number of customer:"))
for i in range(1,n+1):
    print(f"\n customer{i} ")
    name= input("enter customer name:")
    units=float(input("enter unit consumed:"))
    bill=calculate_bill(units)
    print("customer name:",name)
    print("unit",units)
    print("bill amount RS:",round(bill,2))
