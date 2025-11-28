#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
checker = number % 10
checker2 =(-1*number) % 10
if number < 0:
   if checker2 > 5:
    print(f"Last digit of {number} is -{checker2} and is greater than 5")
   elif checker2 == 0:
    print(f"Last digit of {number} is -{checker2} and is 0")
   else:
    print(f"Last digit of {number} is -{checker2} and is less than 6 and not 0")
else:
    if checker > 5:
     print(f"Last digit of {number} is {checker} and is greater than 5")
    elif checker == 0:
     print(f"Last digit of {number} is {checker} and is 0")
    else:
     print(f"Last digit of {number} is {checker} and is less than 6 and not 0")
