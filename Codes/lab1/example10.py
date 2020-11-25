normal_price =3
age=int(input("How old are you ?"))
if age<=6 or age>=60 :
  print("You can use bus for free")
elif age>=6 and age<=18 :
 print("You will pay 1.5 TL ")
else :
 print("You are gonna pay 3 TL")