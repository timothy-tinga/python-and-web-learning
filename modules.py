# import math

# print(math.sqrt(84))
# print(math.pow(2,4))
# print(math.factorial(4))

#random modules. it gives different random numbers;

# import random
# print(random.randint(1,20))
# print(random.randrange(2,15))

#shuffle
# import random

# a= [23,43,56,34,68]
# random.shuffle(a)
# print(a)

#choice... choses any number in variable.
# import random
# wrt="4503nt,:Dxn567>,mxx"
# print(random.choice(wrt))

#DATE/TIME MODULE

# import datetime
# s=datetime.datetime.now()
# print(s)

# import datetime
# y=datetime.datetime.now().year

# m=datetime.datetime.now().month
# d=datetime.datetime.now().day
# t=datetime.datetime.now().hour
# print(y,m,d,t)
       # OR

# Fetch the current time once

# import datetime

# now = datetime.datetime.now()

# y = now.year
# m = now.month
# d = now.day
# t = now.hour

# print(y, m, d, t)
# import datetime
# x=datetime.datetime.now()
# print(x)

#USING.. STRFTIME.

# %d – Day of the month (e.g., 15)
# %m – Month as a number (e.g., 10)
# %Y – Full 4-digit Year (e.g., 2026)
# %H – Hour in 24-hour format (e.g., 22)
# %I – Hour in 12-hour format (e.g., 10)
# %M – Minute (e.g., 42)
# %p – AM or PM
# %A – Full weekday name (e.g., Thursday)
# %B – Full month name (e.g., October)


# import datetime

# m=datetime.datetime.now()

# print(datetime.datetime.now().strftime("%Y-%B-%A-%d-%H:%M %p"))
