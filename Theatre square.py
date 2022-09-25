
dims=input().split()
n=int(dims[0])
m=int(dims[1])
a=int(dims[2])

x = int(n/a)
y = int(m/a)


if n % a != 0:
    x=x+1
if m % a != 0:
    y=y+1

sum=x*y
print(sum)