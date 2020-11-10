print("Enter a, b, c values ​​according to ax'2+bx +c=0 for learn how many roots does your equation has. ")
a =float(input("Enter a value:"))
b =float(input("Enter b value:"))
c =float(input("Enter c value:"))
hint = b**2-4*a*c
if hint > 0 :
 print("There are two real roots")
 x1=((-b)+(b**2-4*a*c)**0.5)/(2*a)
 x2=((-b)-(b**2-4*a*c)**0.5)/(2*a)
 print("These are",x1,x2)
elif hint == 0 :
 print("There is one real root ")
 x1=((-b)+(b**2-4*a*c)**0.5)/(2*a)
 print("This is",x1 )
  
else :
 print("There are two complex roots")
