
def isleapYear(Year):
 if(Year%4==0&Year%100!=0)/ Year%400==0:
   return true
 else:
   return False

Year=int(input("Enter a Year:"))

if isleapYear(Year):
  print("{}is a leap Year.".format(Year))
else:
   print("{}is not a leap Year.". format (Year))
