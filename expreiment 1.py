name=input("enters student name:")
n=int(input("enter number of subject"))
total=0
for i in range(1,n+1):
    mark=float(input(" enter mark for subject{i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="outstanding"
elif percentage>=80:
    grade="A+"
    performance="excellent"
elif percentage>=70:
    grade+"B"
    performance="Very good"
elif percentage>=60:
    grade="C"
    performance="good"
elif percentage>=60:
    grade="D"
    performance="average"
else:
    grade="F"
    performance="need improvement"
print("\n ---Academic performance---")
print("Student name",name)
print("total mark",total)
print("percentage",round(percentage,2),"%")
print("grade",grade)
print("performance",performance)
    
    
