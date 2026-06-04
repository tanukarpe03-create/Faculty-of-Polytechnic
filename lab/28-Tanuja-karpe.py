#problem1
t=1
n=0
while n<=10:
  t+=n
  n+=1
print(t)
  
#problem2 
a=4
b=9
c=19
def even_or_odd(n):
    if(n%2==0):
      print("even")
    else:
      print("odd")
  
even_or_odd(a)
even_or_odd(b)
even_or_odd(c)

#problem3
a=4
b=9
c=19
def even_or_odd(n):
    if(n%3==0):
      print("even")
    else:
      print("odd")
  
even_or_odd(a)
even_or_odd(b)
even_or_odd(c)

#problem4
n=[1,2,3]
def display(n=list):
    for x in n:
      print(x)
display(n)

#problem5
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l.pop(0)
print(l)

#problem6
l=[1,2,3,4,5,6]
l.pop(0)
l.pop(1)
l.pop(2)
print(l)

#problem7
d={"Ram":30,"Vijay":40,"Radha":60}
print (d["Vijay"])

#problem7
d={"Ram":30,"Vijay":40,"Radha":60}
d.update({"Tom":2,"Don":10})
print(d)

