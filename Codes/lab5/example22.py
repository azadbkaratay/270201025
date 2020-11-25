b = "yes"
x = 0
y = 0
while b == "yes":
 a = int(input("enter a number : "))
 y += a 
 x +=1
 b = str(input("do you have more integer ? (yes/no)"))
 if b != "no" or b!= "yes":
   print("please enter no or yes")
   b = str(input("do you have more integer ? (yes/no)"))
 if b == "no":
   print (y/x)
