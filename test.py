def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
mytenneroon = myfunc(10)

print(mydoubler(11))
print(mytripler(11))
print(mytenneroon(11))



x = lambda a : a % d