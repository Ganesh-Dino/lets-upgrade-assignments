#simple intrest program written by Ganesh
g=input("enter F for female and M for male")
age=int(input("enter age"))
p=int(input("enter amount"))
t=int(input("enter time period in months"))
'''iam taking senior citizen age 60 or 60+ for both male and female
and iam taking 18 or 18+ for both male and female for non senior citizen'''
if age==18 or age>=18 and g=='F':
    si=(p*t*6)/100
    print(f"simple intrest is {si}")
elif age==18 or age>=18 and g=='M':
    si=(p*t*5)/100
    print(f"simple intrest is {si}")
elif age==60 or age>=60 and g=='F':
    si=(p*t*8)/100
    print(f"simple intrest is {si}")
elif age==60 or age>=60 and g=='M':
    si=(p*t*7)/100
    print(f"simple intrest is {si}")
else:
    print("Your information must be entered accurately")




    
