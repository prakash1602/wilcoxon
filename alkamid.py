difference=[1,-9,6,-5,4,9]
sum=neg=0

for i in difference:
   if i > 0:
    sum=sum+i
   else:
    neg=neg+i
print('Sum of positive number:',sum)
print('Sum of negetive number:', neg)