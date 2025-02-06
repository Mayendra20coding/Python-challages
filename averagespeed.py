a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
sum=a+b+c
average=sum/3
print(average)
if average > a and average > b and average > c:
 print('%d is higher than %d,%d,%d'%(average,a,b,c))
elif average > a and average > b:
 print('%d is higher than %d,%d'%(average,a,b))
elif average > a and average > c:
 print('%d is higher than %d,%d'%(average,a,c))
elif average > b and average > c:
 print('%d is higher than %d,%d'%(average,b,c))
elif average > a:
  print('%d is just higher than %d'%(average,a))
elif average > b:
  print('%d is just higher than %d'%(average,b))
elif average > c:
  print('%d is just higher than %d'%(average,c))
else:
 print('invalid input')
 