b=int(input("beş yazarız abi: "))
x=1
y=1
a=[1,1]
for i in range(b-2) :
  z=x+y
  a.append(z)
  (z,x)=(x,z)
  (y,z)=(z,y)
print(a)