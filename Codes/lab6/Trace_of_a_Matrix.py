a = []
f = 0
n = int(input("matrix square :"))
for i in range(n):
  b= []
  for j in range(n):
    x = int(input("enter your numbers "))
    b.append(x)
  a.append(b)
  f = f + a[i][i] 
  print("continue")

#for matrx in range(len(a)):
  #print(a[matrx])
print(f)
 