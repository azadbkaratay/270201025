x = []
y = 'again'
z = []
while y == 'again':
 grades = [int(input("Midterm1 ")),int(input("Midterm2 ")),int(input("Final "))]
 average = (grades[0]*30/100)+ (grades[1]*30/100)+(grades[2]*40/100)
 print("Avarge for student is :",average) 
 y = str(input("If you want to calcute another student avarge write 'again' if you don't want please press enter "))
 z.append(average)
 x.append(grades)
print(x)
print(z)