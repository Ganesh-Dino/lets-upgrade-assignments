#count even and odd numbers from the list l=[ 2,3,4,55,56,78,75,69,66,101,100 ]
l=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(l),1):
    if l[i]%2==0:
        even+=1
    else:
        odd+=1
print(f'even count={even}')
print(f'odd count={odd}')
        
