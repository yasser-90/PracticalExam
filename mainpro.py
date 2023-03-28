from operation import operations as oper
n=int(input('n='))
for num in range(n):
    result= oper.fact(num)/oper.pow(n,num)
print(result)