ini = int(input("plz input initial value:"))
fns = int(input("plz input fns value:"))
def summation(ini,fns):
    q = 0
    for i in range(ini,fns+1):
        q = q + i
    return q
print("sum is :",summation(ini,fns))