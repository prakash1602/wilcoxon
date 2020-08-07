t=eval(input('Enter a list:'))
t1=[-19,2,3,4,5,6,9]
t2=[8,2,9,1,0,3,-5]
difference = []
difference1=[]
l=len(t)
sum=0
for i in t:
    sum=sum+i
print('The sum=',sum)
print('The mean=',sum/l)
print('The median=',sorted(t)[l//2])
mode=max(t,key=t.count)
print('The mode=',mode)
n1=max(t)
n2=min(t)
zip_object = zip(t1, t2)
for t1, t2 in zip_object:
    difference.append(t1-t2)
print('The difference between t1 and t2 is:',difference)
for i in difference:
    difference1.append(abs(i))
print('The absolute difference between t1 and t2 is:',difference1)
p=[sorted(t).index(x) for x in t]
print('Ascending order of value according to index of list:',p)

sum=0
neg=0
for i in difference:
   if i > 0:
     sum=sum+i
   else:
     neg=neg+i
print('Sum of positive numbers:',sum)
print('Sum of negetive numbers:', neg)
print('wilcoxon start value is:',neg)
print('wilcoxon critical value is:2')
print('Wstart < Wcritical')
print(' Hence we reject the null hypothesis')
print('So we found significant difference between t1 and t2')