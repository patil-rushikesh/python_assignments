a,b,c,i,sum = 0,1,0,1,0
print(f"{a} \n{b}")
while i<=8:
    c = a + b
    print(f"{c} ")
    sum = sum + c
    a = b
    b = c
    i += 1
avg = sum/i
print(f"{avg}")
