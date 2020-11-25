gpa = float(input("GPA:"))
number_of = float(input("Number of your Lectures:"))
if gpa<2.0 and number_of<47 :
  print("Not enough number of lectures and GPA!")
elif gpa<2.0 and number_of>=47 :
 print("Not enough GPA!")
elif gpa>=2.0 and number_of<47 :
  print("Not enough number of lectures!")
else :
  print("GRADUATED!!!")
