import datetime

x=datetime.datetime.now()
print(x)

#The datetime object has a method for formatting date objects into readable strings
print(x.year)  #Returns Year
print(x.strftime("%A"))  #Returns Weekday name

a=datetime.datetime(2020,10,24)
print(a.year)
print(a.strftime("%B"))  #Guess and Returns Month
print(a.strftime("%A"))  #Guess and Returns Day