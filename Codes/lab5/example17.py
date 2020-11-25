x= int(input("first num:"))
y= int(input("second num:"))
ss=0
while x>0 and y>0:
  if x % 10== y %10:
   ss+=1
  x//= 10 
  y//= 10
print(ss)