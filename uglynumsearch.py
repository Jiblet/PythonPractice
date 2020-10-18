# Divide by 7, 8, 9, 10, 11, 12.
divisors=[2,3]

# Search space starts at 20. Goes up by 10. (Outer)

#for x in range(20,30001,10):

""" here is a way to iterate around and over:
for x in range(1, 30, 1):
    for d in divisors:
        print(x, "/", d)
"""

"""
for x in range(1, 10, 1):
    for d in divisors:
        print(x, "%", d, "= ", x%d)
        if x%d!=0:
            continue
print(x, "is divisible by: ", divisors)
"""
for x in range(1, 30000, 1):
    if (x%1==0) and (x%2==0) and x%3==0 and x%4==0 and x%5==0 and x%6==0 and x%7==0 and x%8==0 and x%9==0 and x%10==0 and x%11==0 and x%12==0:
        print(x)




















