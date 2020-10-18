# Start at 20.
# Divide by 7, 8, 9, 10, 11, 12.

# Search space starts at 20. Goes up by 10. (Outer)

#for x in range(20,30001,10):
for x in range(1, 30000, 1):
    if x%2!=0:
        continue
    if x%3!=0:
        continue
    if x%4!=0:
        continue
    if x%5!=0:
        continue
    if x%6!=0:
        continue
    if x%7!=0:
        continue
    if x%8!=0:
        continue
    if x%9!=0:
        continue
    if x%10!=0:
        continue
    if x%11!=0:
        continue
    if x%12==0:
      print(x, "is divisible by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ")



