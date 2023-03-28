from function import *
n=input('n=')
copy = function()

x= 2
s =0
for count in range(int(n)) :
    
    if count % 2 ==1:
      s = s - (function.fact(count))/(function.power(x,count))
    else :
     
      s = s + (function.fact(count+2))/(function.power(x,count+2))


print(s)    