
def q1():
  #Write Assignment code here
  bool1 = "True"
  bool2 = "False"
  print(bool1 and bool2)
  print (bool1 or bool2)
def q2():
  #Write Assignment code here
  num = int(input("Input a integer: "))
  print (num < 0 or num > 0)
def q3():
  #Write Assignment code here
  num = int(input("Enter a number: "))
  print (num > 0 and num < 10)
def q4():
  #Write Assignment code here
  food = input ("Input food: ")
  drink = input("Input drink: ")
  print (food > "pizza"  or food < "pizza" and drink > "pop" or drink < "pop")
def q5():
  #Write Assignment code here
  num = int(input("Enter a integer: "))
  print (f"The integer {num} is {num % 2 == 0}.")
#Do not edit code after this
#Comment out the followwing code when running tests

q1()
q2()
q3()
q4()
q5()
         