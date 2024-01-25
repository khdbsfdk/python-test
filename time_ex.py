import time

print(time.time())
print()

print(time.gmtime(),"\n",time.localtime(),"\n")

from datetime import *

d1 = date(2024, 2, 10)
print(d1,"\n")

d2 = date.today()
print(d2,"\n")

print(datetime.now(),"\n")
