n=4
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

print("")

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
fact(5)