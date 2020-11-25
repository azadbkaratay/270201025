b = "yes"
a = []
z = int(input("How many numbers will you enter: "))
for i in range(z) :
 c = int(input("Numbers: "))
 a.append(c)
a = set(a)
a = list(a)
a.sort(reverse = True)
print(a)
